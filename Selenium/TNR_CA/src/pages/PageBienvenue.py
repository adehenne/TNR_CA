from seleniumpagefactory.Pagefactory import PageFactory


class PageBienvenue(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    locators = {
        "menu": ("CLASS_NAME", "navbar-toggler navbar-toggler-right"),
        "verifier_admissibilite_btn": ("ID", "lnkVerifierAdmissibilite"),
        "consulter_liste_credits_btn": ("ID", "lnkConsulterListeCredit"),
        "simulation_btn": ("ID", "lnkSimulation")
    }

    def click_menu(self):
        self.menu.click()

    def click_verifier_admissibilite_btn(self):
        self.verifier_admissibilite_btn.click()

    def click_consulter_liste_credits_btn(self):
        self.consulter_liste_credits_btn.click()

    def click_simulation_btn(self):
        self.simulation_btn.click()

