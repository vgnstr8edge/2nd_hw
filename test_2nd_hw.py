from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def browser_settings():
    browser.config.browser_name = 'firefox'
    browser.config.hold_browser_open = True
    browser.open('https://google.com')
    browser.config.window_height = 1000
    browser.config.window_width = 1500
    return browser


def test_positive(browser_settings):
    browser.element('.RNNXgb input[name=q]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative(browser_settings):
    browser.element('.RNNXgb input[name=q]').should(be.blank).type('зщкзхух').press_enter()
    browser.element('[id=center_col]').should(have.text('ничего не найдено'))

