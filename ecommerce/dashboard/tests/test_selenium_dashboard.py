import pytest
from selenium.webdriver.common.keys import Keys

@pytest.mark.selenium
def test_dashboard_admin_login(live_server, chrome_browser_instance):

    browser = chrome_browser_instance

    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element()