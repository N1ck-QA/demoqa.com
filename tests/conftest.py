import pytest
from webdriver import WebDriver
from utils.data_loader import DataLoader


@pytest.fixture(autouse=True)
def driver():
    WebDriver()
    yield
    WebDriver().quit_driver()


@pytest.fixture(params=DataLoader.load_test_data())
def user_data(request):
    return request.param
