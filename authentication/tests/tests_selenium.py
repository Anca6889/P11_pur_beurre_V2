"""This module will use selenium for testing with Google Chrome Navigator"""
from P8_pur_beurre.settings import BASE_DIR
from selenium import webdriver
from selenium.webdriver.support.select import Select
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from app.models import Product
import random
import string

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920x1080')


class BrowserTests(StaticLiveServerTestCase):
    """This class will test a registering, logout and login an user"""

    def setUp(self):
        """setup the webdriver with Google Chrome driver"""

        self.driver = webdriver.Chrome(
            executable_path=str(BASE_DIR / 'webdrivers' / 'chromedriver'),
            options=chrome_options,
        )

        self.mock_product = Product.objects.create(
            id='1',
            product_name_fr='testname',
            brands='testbrand', nutriscore_grade="e",
            stores='teststore',
            url='test/url.com',
            image='testimage'
        )

    def test_login_logout_signin_rate(self):
        """This method will do all the actions, check comments below"""

        # create a random string of 10 letters used for generate an random
        # email
        letters = string.ascii_lowercase
        stringmail = (''.join(random.choice(letters) for i in range(10)))

        # go to main page
        self.driver.get(self.live_server_url)

        # click on the registration page
        sign_in = self.driver.find_element_by_link_text("S'inscrire")
        self.driver.execute_script("arguments[0].click();", sign_in)

        # feel the form fields and click on registration
        self.driver.find_element_by_name(
            "email").send_keys(stringmail+"@test.com")
        self.driver.find_element_by_name("username").send_keys(stringmail)
        self.driver.find_element_by_name("password1").send_keys("Def741852")
        self.driver.find_element_by_name("password2").send_keys("Def741852")
        self.driver.find_element_by_id("registration_button").click()
        self.assertIn("{}/authentication/sign_in".format(self.live_server_url),
                      self.driver.current_url)

        # click on logout
        log_out = self.driver.find_element_by_link_text("Se déconnecter")
        self.driver.execute_script("arguments[0].click();", log_out)

        # click on login
        log_in = self.driver.find_element_by_link_text("Se connecter")
        self.driver.execute_script("arguments[0].click();", log_in)

        # feel the form fields with previous data for check login
        self.driver.find_element_by_name(
            "email").send_keys(stringmail+"@test.com")
        self.driver.find_element_by_name("password").send_keys("Def741852")
        self.driver.find_element_by_id("login_button").click()
        self.assertIn("{}/authentication/login".format(self.live_server_url),
                      self.driver.current_url)

        # rate and comment product
        search = self.driver.find_element_by_name("search")
        top_search_button = self.driver.find_element_by_id("top-search-button")
        search.send_keys("testname")
        top_search_button.click()
        rate_button = self.driver.find_element_by_id("rate-button")
        rate_button.click()
        rate = self.driver.find_element_by_id("id_rate")
        rate.click()
        select = Select(rate)
        random_option = random.choice(select.options)
        random_option.click()
        text = self.driver.find_element_by_id("id_text")
        text.click()
        text.send_keys("This is a test comment based on my random rate note")
        valid_button = self.driver.find_element_by_id("rate_button")
        valid_button.click()
