from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker

class TestRegistration():

    def setup_class(self):
        fake = Faker()
        self.email = fake.email()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_registration_with_an_incorrect_password(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Kirill')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('1')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
        assert self.driver.find_element(By.XPATH, '//p[contains(text(),"Некорректный пароль")]')
        self.driver.quit()

    def test_registration_with_the_correct_password(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Kirill')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/h2')
        self.driver.quit()


