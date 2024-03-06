from seleniumpagefactory.Pagefactory import PageFactory


class AppointmentSummaryPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "sideBar": ("ID", "menu-toggle"),
        "pageTitle": ("CSS", "#summary > div > div > div > h2"),
        "homePageBtn": ("LINK_TEXT", "Go to Homepage")
    }

    def click_side_bar(self):
        self.sideBar.click()

    def click_homepage_btn(self):
        self.homePageBtn.click()

    def get_page_assertion(self):
        assert self.pageTitle.get_text() == "Appointment Confirmation"
