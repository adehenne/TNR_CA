from seleniumpagefactory.Pagefactory import PageFactory


class PageSimulation(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
            "menu": ("CLASS_NAME", "navbar-toggler navbar-toggler-right")
        }

    def click_menu(self):
        self.menu.click()

