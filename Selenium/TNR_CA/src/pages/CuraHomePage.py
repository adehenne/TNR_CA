from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "sideBar": ("ID", "menu-toggle"),
        "makeAppointment": ("ID", "btn-make-appointment")
    }

    def click_side_bar(self):
        self.sideBar.click()

    def click_make_appointment(self):
        self.makeAppointment.click()

    def get_page_assertion(self):
        assert self.driver.title == "CURA Healthcare Service"
