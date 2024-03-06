from seleniumpagefactory.Pagefactory import PageFactory


class PageAuthentification(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
            "menu": ("CLASS_NAME", "navbar-toggler navbar-toggler-right"),
            "champs_username": ("ID", "username"),
            "champs_password": ("ID", "password"),
            "loginBtn": ("CLASS_NAME", "btn btn-dark")
        }

    def select_username(self, username):
        self.champs_username.set_text(username)

    def select_password(self, password):
        self.champs_password.set_text(password)

    def click_login(self):
        self.loginBtn.click()
