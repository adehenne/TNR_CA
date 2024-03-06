from seleniumpagefactory.Pagefactory import PageFactory

class SideBarMenu(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "home_btn": ("LINK_TEXT", "Home"),
        "login_btn": ("LINK_TEXT", "Login"),
        "history_btn": ("LINK_TEXT", "History"),
        "profile_btn": ("LINK_TEXT", "Profile"),
        "logout_btn": ("LINK_TEXT", "Logout")
    }

    def click_home_btn(self):
        self.home_btn.click()

    def click_login_btn(self):
        self.login_btn.click()

    def click_history_btn(self):
        self.history_btn.click()

    def click_profile_btn(self):
        self.profile_btn.click()

    def click_logout_btn(self):
        self.logout_btn.click()
