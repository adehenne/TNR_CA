from selenium import webdriver
import unittest
import time
from src.pages.CuraHomePage import HomePage
from src.pages.Menu import Menu
from src.pages.CuraLoginPage import LoginPage
from src.pages.CuraAppointmentPage import AppointmentPage
from src.pages.CuraAppointmentSummaryPage import AppointmentSummaryPage
import csv
from datetime import date
from datetime import datetime
from datetime import timedelta


class CreationContratTest(unittest.TestCase):

    def test_ft2_ct1_contrat_valide(self):
        driver = webdriver.Firefox()

        # Accéder à l'URL du site
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        driver.maximize_window()

        homepage = HomePage(driver)
        side_bar = Menu(driver)
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


if __name__ == "__main__":
    unittest.main()
