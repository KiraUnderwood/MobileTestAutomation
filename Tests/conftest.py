import pytest
import configparser

from appium import webdriver
from ConfigsForTests.Capability import FillCapabilities

'''
parsing the BaseOptions.ini file to get capabilities
'''
config = configparser.RawConfigParser()
config.optionxform = lambda option: option
config.read('../ConfigsForTests/BaseOptions.ini')
appium_server = config['AppiumServer']['server']

'''
pytest fixtures representing test setup and teardown
test creator should only use driver_for_native or driver_for_web fixtures 
'''


@pytest.fixture(scope="function")
def params_for_native():
    """
    fixture checking the passed dict and determining if it is for Native apps
    :return: checked dict appropriate for native Apps
    """
    options = FillCapabilities(**config['NativeApp'])
    if not options.is_native():
        raise Exception('The capabilities are not for native app!')
    return options


@pytest.fixture(scope="function")
def driver_for_native(params_for_native):
    """
       Pytest fixture to initialize the driver for testing native app
       :param params_for_native:  key=value dict with capabilities already checked by the named fixture
       :return: driver
    """
    if isinstance(appium_server, str) and isinstance(params_for_native, dict):
        driver = webdriver.Remote(appium_server, params_for_native)
        yield driver
        driver.quit()


@pytest.fixture(scope="function")
def params_for_web():
    """
    fixture checking the passed dict and determining if it is for Web apps
    :return: checked dict appropriate for web Apps
    """
    options = FillCapabilities(**config['WebApp'])
    if not options.is_web():
        raise Exception('The capabilities are not for web app!')
    return options


@pytest.fixture(scope="function")
def driver_for_web(params_for_web):
    """
       Pytest fixture to initialize the driver for testing web apps
       :param params_for_web:  key=value dict with capabilities already checked by the named fixture
       :return: driver
    """
    if isinstance(appium_server, str) and isinstance(params_for_web, dict):
        driver = webdriver.Remote(appium_server, params_for_native)
        yield driver
        driver.quit()




