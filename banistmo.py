import unittest
from selenium import webdriver

class Banistmo(unittest.TestCase):


    def setUp(self):
            self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
            driver = self.driver
            driver.get('https://www.banistmo.com/wps/portal/banistmo/personas/')
            driver.maximize_window()      

    def test_Okta(self):
        driver = self.driver
        productoservicios = diver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/section/div[3]/div/div/div/div[2]/ul/li[3]').click()
        prestamos = driver.find_element_by_xpath('//*[@id="navbar-collapse-grid"]/ul/li[3]/ul/li/div[1]/div[1]/ul/li[4]/a').click()
        prestamosauto = driver.find_element_by_xpath('//*[@id="none"]/div/div/div[2]/div[3]/div/div[2]/div/a').click()
        tasastarifas = driver.find_element_by_xpath('//*[@id="filialTabs"]/li[4]/a').click()
        pdf = driver.find_element_by_xpath('//*[@id="tab4"]/table/tbody/tr[2]/td[2]/span/a/img').click()

    def tearDown(self):
    self.driver.quit()       