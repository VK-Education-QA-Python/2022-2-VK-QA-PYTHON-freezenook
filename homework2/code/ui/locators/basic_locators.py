from selenium.webdriver.common.by import By


class BasePageLocators:
    # Локаторы разделов
    PROFILE_SECTION = (By.XPATH, './/*[contains(@class, "center-module-profile")]')
    TOOLS_SECTION = (By.XPATH, './/*[contains(@class, "center-module-tools")]')
    PROFILE_SECTION_LOCATOR = (By.XPATH, './/*[contains(@class, "profile-contact-info")]')
    TOOLS_SECTION_LOCATOR = (By.XPATH, './/*[contains(@class, "feeds-module-page")]')

    # Локаторы для внесения контактной информации
    FIO_FIELD = (By.XPATH, '//*[@data-name="fio"]//child::input')
    INN_FIELD = (By.XPATH, '//*[@data-name="ordInn"]//child::input')
    PHONE_FIELD = (By.XPATH, '//*[@data-name="phone"]//child::input')
    SUBMIT_INFO_BUTTON = (By.CLASS_NAME, 'button__text')
    SUBMIT_INFO_WRAPPER = (By.XPATH, './/*[@data-class-name="SuccessView"]')


class LoginPageLocators(BasePageLocators):
    #Локаторы для авторизации
    LOGIN_BUTTON = (By.XPATH, './/*[contains(@class, "responseHead-module-button")]')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    AUTH_BUTTON = (By.XPATH, './/*[contains(@class, "authForm-module-button")]')
    AUTH_NOTIFY_WRAPPER = (By.XPATH, './/*[contains(@class, "notify-module-wrapper")]')
    #Локаторы для логаута
    PROFILE_BUTTON = (By.XPATH, './/*[contains(@class, "right-module-rightWrap")]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')


class CampaignPageLocators(BasePageLocators):
    CREATE_CAMPAIGN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "button-module-textWrapper")]')
    TRAFFIC_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "_traffic")]')

    LOAD_CONTENT_PAGE_LOCATOR = (By.XPATH, '//div[contains(@class, "js-target-content")]')
    TRAFFIC_LOCATOR = (By.XPATH, '//div[contains(@class, "_traffic")]')
    FIELD_FOR_URL_LOCATOR = (By.XPATH, '//input[contains(@class, "mainUrl-module-searchInput")]')
    # CAMPAIGN_NAME_TITLE_LOCATOR = (By.XPATH, '//div[@class="base-settings__campaign-name-wrap '
    #                                                 'js-base-setting-campaign-name-wrap"]')

    CAMPAIGN_TITLE = (By.XPATH, '//div[@class="base-settings__campaign-name-wrap js-base-setting-campaign-name-wrap"]')
    CAMPAIGN_NAME_FIELD_LOCATOR = (By.XPATH, '//div[contains(@class, "input_campaign-name")]//child::input')
    TEASER_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@id, "patterns_teaser")]')
    SAVE_UPLOAD_PICTURE = (By.XPATH, '//input[contains(@class, "image-cropper__save js-save")]')

    UPLOAD_IMAGE_BUTTON_LOCATOR = (By.XPATH, '//input[contains(@data-test, "image_90x75")]')
    FIELD_FOR_AD_TITLE_LOCATOR = (By.XPATH, '//input[contains(@data-name, "title")]')
    FIELD_FOR_AD_TEXT_LOCATOR = (By.XPATH, '//textarea[contains(@data-name, "text")]')
    SAVE_CAMPAIGN_BUTTON_LOCATOR = (By.XPATH, '//button[@data-service-readonly="true"]')
    SUCCESS_NOTIFY_LOCATOR = (By.XPATH, '//div[contains(@class, "notify-module-content")]')


class SegmentsPageLocators(BasePageLocators):
    #Локаторы для создания нового сегмента
    APPS_AND_GAMES_SEGMENT_TYPE = (By.XPATH, '//div[contains(@class, "adding-segments-item")][8]')
    OK_AND_VK_SEGMENT_TYPE = (By.XPATH, '//div[contains(@class, "adding-segments-item")][10]')
    PLAYING_AND_PAYING_CHECKBOX = (By.XPATH, './/input[contains(@class, "adding-segments-source__checkbox ")]')
    ADD_SEGMENT_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "js-add-button")]//child::button')
    FIELD_FOR_NAME_OF_NEW_SEGMENT = (By.XPATH, '//div[contains(@class, "input_create-segment-form")]//child::input')
    SAVE_SEGMENT_BUTTON_LOCATOR = (By.XPATH, '//button[@data-service-readonly="true"]')
    TITLE_SEGMENT_LOCATOR = '//a[@title="{}"]'
    SEGMENTS_HEADER_LOCATOR = (By.XPATH, '//div[contains(@class, "label-module-labelWrapper")]')

    #Локаторы для удаления сегмента
    SEGMENT_TITLE_LOCATOR = '//a[@title="{}"]'
    DELETE_SEGMENT_LOCATOR = '//div/a[contains(@title, "{}")]//following::div[9]'
    SUBMIT_DELETE_SEGMENT_LOCATOR = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')

    #Локаторы для добавления группы VK в источники
    GROUP_URL_FIELD_LOCATOR = (By.XPATH, './/input[contains(@class, "multiSelectSuggester-module-searchInput")]')
    SELECT_ALL_GROUPS_BUTTON_LOCATOR = (By.XPATH, './/*[@data-test="select_all"]')
    ADD_GROUP_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "bubbleComponent-module-submit")]')
    SUCCESS_INFO_WRAPPER = (By.XPATH, './/*[@data-class-name="SuccessView"]')

    #Локаторы для удаления группы из источника
    DELETE_SOURCE_LOCATOR = '//td/a[contains(@href, "{}")]//following::div[2]'
    SUBMIT_DELETE_SOURCE_LOCATOR = (By.XPATH, '//button[contains(@class, "button_confirm-remove")]')
    TITLE_SOURCE_LOCATOR = '//a[@href="{}"]'
