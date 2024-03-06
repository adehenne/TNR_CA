from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
            "sideBar": ("ID", "menu-toggle"),
            "username": ("ID", "txt-username"),
            "password": ("ID", "txt-password"),
            "loginBtn": ("ID", "btn-login"),
            "pageTitle": ("CSS", "#login > div > div > div > h2")
        }

    def select_username(self, username):
        self.username.set_text(username)

    def select_password(self, password):
        self.password.set_text(password)

    def click_login(self):
        self.loginBtn.click()

    def get_page_assertion(self):
        assert self.pageTitle.get_text() == "Login"
