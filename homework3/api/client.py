import requests


class ApiClient:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = requests.Session()
        self.csrf_token = None

    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=False, params=None,
                 json=None, files=None):
        url = location
        response = self.session.request(method=method, url=url, headers=headers, data=data, params=params, json=json,
                                        files=files)
        if response.status_code != expected_status:
            raise Exception(f'Got {response.status_code} {response.reason} for URL "{url}"')
        if jsonify:
            return response.json()
        return response

    def get_token(self):
        location = 'https://target-sandbox.my.com/csrf/'
        res = self._request('GET', location, jsonify=False)
        headers = res.headers['Set-Cookie'].split(';')
        token_header = [c for c in headers if 'csrftoken' in c]
        if not token_header: raise Exception('csrf_token not found')
        token_header = token_header[0]
        csrf_token = token_header.split('=')[-1]
        return csrf_token

    def post_login(self):
        url = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        headers = {
            'Origin': 'https://target-sandbox.my.com',
            'Referer': 'https://target-sandbox.my.com/',
        }
        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target-sandbox.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }
        result = self._request('POST', url, headers=headers, data=data, expected_status=200, jsonify=False)
        try:
            self.csrf_token = self.get_token()
        except KeyError as exc:
            raise AssertionError(...) from exc
        return result

    def post_create_segment(self, name, relations_json, pass_condition=1):
        location = 'https://target-sandbox.my.com/api/v2/remarketing/segments.json'
        headers = {
            'X-CSRFToken': self.csrf_token}
        json = {
            "name": f"{name}",
            "pass_condition": pass_condition,
            "relations": relations_json
        }
        response = self.session.post(url=location, headers=headers, json=json)
        response_data = response.json()
        segment_id = response_data['id']
        return segment_id

    def delete_segment(self, segment_id):
        location = f'https://target-sandbox.my.com/api/v2/remarketing/segments/{segment_id}.json'

        headers = {
            'Origin': 'https://target-sandbox.my.com',
            'Referer': 'https://target-sandbox.my.com/segments/segments_list',
            'X-CSRFToken': self.csrf_token,
            'X-Requested-With': 'XMLHttpRequest'
        }

        self._request('DELETE', location, headers, expected_status=204)

    def get_segment(self, segment_id):
        location = 'https://target-sandbox.my.com/api/v2/remarketing/segments.json'

        headers = {
            'X-Requested-With': 'XMLHttpRequest'
        }

        params = {
            "limit": "50"
        }

        response = self._request('GET', location, headers=headers, params=params, expected_status=200)
        return str(segment_id) in response.text

    def post_add_club_source(self, club_id):
        club_source_id = self.get_vk_source(club_id) #проверяем, есть ли группа в списке источников
        if club_source_id is None:
            print('Группы еще нет в списке, добавляем')
            location = 'https://target-sandbox.my.com/api/v2/remarketing/vk_groups/bulk.json'
            headers = {
                'Origin': 'https://target-sandbox.my.com',
                'Referer': 'https://target-sandbox.my.com/segments/groups_list',
                'X-CSRFToken': self.csrf_token,
                'X-Requested-With': 'XMLHttpRequest'
            }
            json = {
                'items': [{"object_id": club_id}]
            }
            response = self._request('POST', location, headers=headers, json=json, expected_status=201, jsonify=True)
            club_source_id = response['items'][0]['id']
            print(f'Группу добавили, id источника = {club_source_id}')
        else:
            print(f'Группа в списке, ничего не добавляем id = {club_source_id}')

        return club_source_id

    def delete_club_source(self, club_source_id):
        location = f'https://target-sandbox.my.com/api/v2/remarketing/vk_groups/{club_source_id}.json'
        headers = {
            'Origin': 'https://target-sandbox.my.com',
            'Referer': 'https://target-sandbox.my.com/segments/groups_list',
            'X-CSRFToken': self.csrf_token,
            'X-Requested-With': 'XMLHttpRequest'
        }
        self._request('DELETE', location, headers, expected_status=204)

    def get_vk_source(self, club_id):
        club_source_id = None
        location = 'https://target-sandbox.my.com/api/v2/remarketing/vk_groups.json'
        headers = {
            'X-Requested-With': 'XMLHttpRequest'
        }
        params = {
            "limit": "50"
        }
        response = self._request('GET', location, headers=headers, params=params, expected_status=200, jsonify=False)

        if str(club_id) in response.text:
            #Если группа уже есть, превращаем результат запроса в JSON и ищем в нём id источника (4-зн. на таргете)
            response_json = response.json()
            for i in range(len(response_json['items'])):
                if response_json['items'][i]['object_id'] == club_id:
                    club_source_id = response_json['items'][i]['id']
                    break
        return club_source_id
