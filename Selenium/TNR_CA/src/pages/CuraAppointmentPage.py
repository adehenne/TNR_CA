from seleniumpagefactory.Pagefactory import PageFactory


class AppointmentPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "sideBar": ("ID", "menu-toggle"),
        "pageTitle": ("CSS", "#appointment > div > div > div > h2"),
        "facility": ("ID", "combo_facility"),
        "applyReadmission": ("ID", "chk_hospotal_readmission"),
        "healthCareProgramMedicare": ("ID", "radio_program_medicare"),
        "healthCareProgramMedicaid": ("ID", "radio_program_medicaid"),
        "healthCareProgramNone": ("ID", "radio_program_none"),
        "visitDate": ("ID", "txt_visit_date"),
        "comment": ("ID", "txt_comment"),
        "bookBtn": ("ID", "btn-book-appointment")
    }

    def click_side_bar(self):
        self.sideBar.click()

    def select_facility(self, facility):
        self.facility.select_element_by_value(facility)

    def select_readmission(self, readmission):
        if readmission == "Yes":
            self.applyReadmission.click()

    def select_program(self, program):
        if program == "Medicare":
            self.healthCareProgramMedicare.click()
        elif program == "Medicaid":
            self.healthCareProgramMedicaid.click()
        elif program == "None":
            self.healthCareProgramNone.click()

    def select_date(self, date):
        self.visitDate.send_keys(date)

    def select_comment(self, comment):
        self.comment.set_text(comment)

    def click_book_appointment(self):
        self.bookBtn.click()

    def get_page_assertion(self):
        assert self.pageTitle.get_text() == "Make Appointment"
