from seleniumpagefactory.Pagefactory import PageFactory


class PageAccueil(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "menu": ("CLASS_NAME", "navbar-toggler navbar-toggler-right"),
        "acces_auth": ("ID", "lnkAccesCreditAuto")
    }

    def click_menu(self):
        self.menu.click()

    def click_acces_auth(self):
        self.acces_auth.click()

    def get_page_assertion(self):
        assert self.driver.title == "Crédit Auto | QSI Conseil"