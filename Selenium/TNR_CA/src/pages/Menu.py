from seleniumpagefactory.Pagefactory import PageFactory

class Menu(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "CA": ("LINK_TEXT", "Crédit Auto"),
        "accueil_btn": ("ID", "lnkAccueil"),
        "credit_btn": ("ID", "lnkCredit"),
        "creer_credit_btn": ("ID", "lnkCreerContrat"),
        "location_btn": ("ID", "lnkLocation"),
        "verifier_contrat_btn": ("LINK_TEXT", "Vérifier contrat en cours client"),
        "deconnexion_btn": ("ID", "lnkDeconnexion")

    }

    def click_ca_btn(self):
        self.CA.click()

    def click_accueil_btn(self):
        self.accueil_btn.click()

    def click_credit_btn(self):
        self.credit_btn.click()

    def click_creer_credit_btn(self):
        self.creer_credit_btn.click()

    def click_location_btn(self):
        self.location_btn.click()

    def click_verifier_contrat_btn(self):
        self.creer_credit_btn.click()

    def click_deconnexion_btn(self):
        self.deconnexion_btn.click()
