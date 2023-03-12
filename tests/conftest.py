import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

from framework.demoqa_with_env import DemoQaWithEnv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope='session')
def demoshop(request):
    env = request.config.getoption("--env")
    return DemoQaWithEnv(env)


@pytest.fixture(scope='function')
def app(demoshop):
    browser.config.base_url = demoshop.url_demoqa
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    response = demoshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.open("Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    return browser


@pytest.fixture(scope='session')
def reqres(request):
    env = request.config.getoption("--env")
    return DemoQaWithEnv(env).session_reqres
