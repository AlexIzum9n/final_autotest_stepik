from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    LOGIN_LINK_LOCATOR = '#login_link'
    
    def __init__(self, browser, url):
        super().__init__(browser, url)
        
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, self.LOGIN_LINK_LOCATOR), "Login link is not presented"
