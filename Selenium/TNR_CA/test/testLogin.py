from selenium import webdriver
import unittest
import time
from src.pages.CuraHomePage import HomePage
from src.pages.Menu import Menu
from src.pages.CuraLoginPage import LoginPage
from src.pages.CuraAppointmentPage import AppointmentPage


class LoginTest(unittest.TestCase):

    def test_ft1_ct1_login_acd_valid(self):
        driver = webdriver.Firefox()

        # Accéder à l'URL du site
        driver.get("http://credit-auto.qsiconseil.ma/")
        driver.maximize_window()

        homepage = HomePage(driver)
        side_bar = Menu(driver)
        login_page = LoginPage(driver)
        appointment_page = AppointmentPage(driver)

        homepage.get_page_assertion()

        homepage.click_side_bar()

        side_bar.click_login_btn()

        login_page.select_username("John Doe")
        login_page.select_password("ThisIsNotAPassword")
        login_page.click_login()

        appointment_page.get_page_assertion()

        time.sleep(2)
        driver.quit()

    def test_ft1_ct2_login_gcd_valid(self):
        driver = webdriver.Firefox()

        # Accéder à l'URL du site
        driver.get("http://credit-auto.qsiconseil.ma/")
        driver.maximize_window()

        homepage = HomePage(driver)
        side_bar = Menu(driver)
        login_page = LoginPage(driver)

        homepage.get_page_assertion()

        homepage.click_side_bar()

        side_bar.click_login_btn()

        login_page.select_username("John Doe")
        login_page.select_password("ThisIsAPassword")
        login_page.click_login()

        login_page.get_page_assertion()

        time.sleep(2)
        driver.quit()

    def test_ft1_ct3_login_lcd_valid(self):
        driver = webdriver.Firefox()

        # Accéder à l'URL du site
        driver.get("http://credit-auto.qsiconseil.ma/")
        driver.maximize_window()

        homepage = HomePage(driver)
        side_bar = Menu(driver)
        login_page = LoginPage(driver)

        homepage.get_page_assertion()

        homepage.click_side_bar()

        side_bar.click_login_btn()

        login_page.select_username("Jack")
        login_page.select_password("ThisIsNotAPassword")
        login_page.click_login()

        login_page.get_page_assertion()

        time.sleep(2)
        driver.quit()

    def test_ft1_ct4_login_rcd_valid(self):
        driver = webdriver.Firefox()

        # Accéder à l'URL du site
        driver.get("http://credit-auto.qsiconseil.ma/")
        driver.maximize_window()

        homepage = HomePage(driver)
        side_bar = Menu(driver)
        login_page = LoginPage(driver)

        homepage.get_page_assertion()

        homepage.click_side_bar()

        side_bar.click_login_btn()

        login_page.select_username("Jack")
        login_page.select_password("ThisIsNotAPassword")
        login_page.click_login()

        login_page.get_page_assertion()

        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    unittest.main()
