import os
import signal
import subprocess
import time
from copy import copy
from requests.exceptions import ConnectionError
from fixtures import *

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError('App did not started in 5s!')


def app_configure():
    app_path = os.path.join(repo_root, 'application', 'app.py')

    env = copy(os.environ)
    env.update({'APP_HOST': settings.APP_HOST, 'APP_PORT': settings.APP_PORT})
    env.update({'STUB_HOST': settings.STUB_HOST, 'STUB_PORT': settings.STUB_PORT})
    env.update({'MOCK_HOST': settings.MOCK_HOST, 'MOCK_PORT': settings.MOCK_PORT})

    app_stderr = open('/tmp/stub_stderr', 'w')
    app_stdout = open('/tmp/stub_stdout', 'w')

    app_proc = subprocess.Popen(['python3', app_path], stderr=app_stderr, stdout=app_stdout, env=env)
    wait_ready(settings.APP_HOST, settings.APP_PORT)

    return app_proc, app_stderr, app_stdout


def stub_configure():
    stub_path = os.path.join(repo_root, 'stub', 'flask_stub.py')

    env = copy(os.environ)
    env.update({'STUB_HOST': settings.STUB_HOST, 'STUB_PORT': settings.STUB_PORT})

    stub_stderr = open('/tmp/stub_stderr', 'w')
    stub_stdout = open('/tmp/stub_stdout', 'w')

    stub_proc = subprocess.Popen(['python3', stub_path], stderr=stub_stderr, stdout=stub_stdout, env=env)
    wait_ready(settings.STUB_HOST, settings.STUB_PORT)

    return stub_proc, stub_stderr, stub_stdout


def mock_configure():
    from mock import flask_mock
    flask_mock.run_mock()
    wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        config.app_proc, config.app_stderr, config.app_stdout = app_configure()
        config.stub_proc, config.stub_stderr, config.stub_stdout = stub_configure()
        mock_configure()


def close_process(proc):
    proc.send_signal(signal.SIGINT)
    exit_code = proc.wait()
    assert exit_code == 0


def pytest_unconfigure(config):
    close_process(config.app_proc)
    config.app_stderr.close()
    config.app_stdout.close()

    close_process(config.stub_proc)
    config.stub_stderr.close()
    config.stub_stdout.close()

    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')
