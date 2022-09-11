from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAuthorization():

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_authorization(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('jessica04@example.com')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))
        assert self.driver.find_element(By.XPATH, '//button[contains(text(),"Оформить заказ")]')
        self.driver.quit()

    def test_authorization_via_the_registration_form(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('jessica04@example.com')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))
        assert self.driver.find_element(By.XPATH, '//button[contains(text(),"Оформить заказ")]')
        self.driver.quit()

    def test_authorization_via_password_recovery(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('jessica04@example.com')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))
        assert self.driver.find_element(By.XPATH, '//button[contains(text(),"Оформить заказ")]')
        self.driver.quit()

    def test_authorization_in_via_the_log_in_to_account_button(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('jessica04@example.com')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))
        assert self.driver.find_element(By.XPATH, '//button[contains(text(),"Оформить заказ")]')
        self.driver.quit()