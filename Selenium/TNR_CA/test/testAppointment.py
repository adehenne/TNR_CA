from selenium import webdriver
import unittest
import time
from src.pages.CuraHomePage import HomePage
from src.pages.CuraSidebarMenu import SideBarMenu
from src.pages.CuraLoginPage import LoginPage
from src.pages.CuraAppointmentPage import AppointmentPage
from src.pages.CuraAppointmentSummaryPage import AppointmentSummaryPage
import csv
from datetime import date
from datetime import datetime
from datetime import timedelta


class AppointmentTest(unittest.TestCase):

    def test_ft2_ct1_appointment_valid(self):
        driver = webdriver.Firefox()

        # Accéder à l'URL du site
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.maximize_window()

        homepage = HomePage(driver)
        side_bar = SideBarMenu(driver)
        login_page = LoginPage(driver)
        appointment_page = AppointmentPage(driver)
        appointment_summary_page = AppointmentSummaryPage(driver)

        homepage.get_page_assertion()

        homepage.click_side_bar()

        side_bar.click_login_btn()

        login_page.select_username("John Doe")
        login_page.select_password("ThisIsNotAPassword")
        login_page.click_login()

        appointment_page.get_page_assertion()

        appointment_page.select_facility("Hongkong CURA Healthcare Center")
        appointment_page.select_readmission("Yes")
        appointment_page.select_program("Medicaid")

        today = date.today()
        delta = timedelta(days=7)
        appointment_date = today + delta
        appointment_date = appointment_date.strftime("%d/%m/%Y")
        appointment_page.select_date(appointment_date)

        appointment_page.select_comment("Ceci est un commentaire valide.")

        appointment_page.click_book_appointment()

        appointment_summary_page.get_page_assertion()

        time.sleep(2)
        appointment_summary_page.click_side_bar()
        side_bar.click_logout_btn()
        time.sleep(2)
        driver.quit()

    def test_ft2_ct2_appointments_pairwise_valid(self):
        driver = webdriver.Firefox()

        # Accéder à l'URL du site
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.maximize_window()

        homepage = HomePage(driver)
        side_bar = SideBarMenu(driver)
        login_page = LoginPage(driver)
        appointment_page = AppointmentPage(driver)
        appointment_summary_page = AppointmentSummaryPage(driver)

        homepage.get_page_assertion()

        homepage.click_side_bar()

        side_bar.click_login_btn()

        login_page.select_username("John Doe")
        login_page.select_password("ThisIsNotAPassword")
        login_page.click_login()

        appointment_page.get_page_assertion()

        with open(
                'D:\\_Formation Testeur Logiciel ISTQB\\Supports de cours\\12-Automatiser avec Selenium et '
                'Webdriver\\TP\\TP1\\TP01_Selenium_Webdriver\\TP1_Exo4\\Pairwise_CURAHealthcare_RDV.csv',
                newline='') as csvfile:
            appointments = csv.reader(csvfile, delimiter=',', quotechar='"')

            # On passe la première ligne d'en-tête
            next(appointments)

            # On parcourt le fichier
            for row in appointments:

                # On récupère uniquement le nom de la ville sans "Cura"
                facility = row[1].split()[0]

                appointment_page.select_facility(facility + " CURA Healthcare Center")
                appointment_page.select_readmission(row[2])
                appointment_page.select_program(row[3])

                this_year = datetime.now().year
                this_month = datetime.now().month

                if row[4] == 'current Month':
                    appointment_date = datetime(this_year, this_month, 15)
                    appointment_date = appointment_date.strftime("%d/%m/%Y")
                    appointment_page.select_date(appointment_date)
                elif row[4] == 'Past month':
                    appointment_date = datetime(this_year, this_month - 1, 15)
                    appointment_date = appointment_date.strftime("%d/%m/%Y")
                    appointment_page.select_date(appointment_date)
                elif row[4] == 'Next month':
                    appointment_date = datetime(this_year, this_month + 1, 15)
                    appointment_date = appointment_date.strftime("%d/%m/%Y")
                    appointment_page.select_date(appointment_date)

                if row[5] == 'With':
                    appointment_page.select_comment("Ceci est un commentaire valide.")

                appointment_page.click_book_appointment()

                appointment_summary_page.get_page_assertion()

                time.sleep(2)

                appointment_summary_page.click_homepage_btn()

                homepage.click_make_appointment()

        appointment_summary_page.click_side_bar()
        side_bar.click_logout_btn()
        time.sleep(2)
        driver.quit()

    def test_ft2_ct3_appointment_invalid(self):
        driver = webdriver.Firefox()

        # Accéder à l'URL du site
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.maximize_window()

        homepage = HomePage(driver)
        side_bar = SideBarMenu(driver)
        login_page = LoginPage(driver)
        appointment_page = AppointmentPage(driver)
        appointment_summary_page = AppointmentSummaryPage(driver)

        homepage.get_page_assertion()

        homepage.click_side_bar()

        side_bar.click_login_btn()

        login_page.select_username("John Doe")
        login_page.select_password("ThisIsNotAPassword")
        login_page.click_login()

        appointment_page.get_page_assertion()

        appointment_page.select_facility("Hongkong CURA Healthcare Center")
        appointment_page.select_readmission("Yes")
        appointment_page.select_program("Medicaid")

        appointment_page.select_comment("Ceci est un commentaire valide.")

        appointment_page.click_book_appointment()

        appointment_page.get_page_assertion()

        time.sleep(2)
        appointment_summary_page.click_side_bar()
        side_bar.click_logout_btn()
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    unittest.main()
