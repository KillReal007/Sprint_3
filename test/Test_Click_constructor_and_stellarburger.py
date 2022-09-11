from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructorAndStellarburgers():

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_switching_from_your_personal_account_to_the_constructor_and_click_stellarburgers(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('jessica04@example.com')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/header/nav/a/p')))
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//button[contains(text(),"Сохранить")]')))
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        self.driver.find_element(By.XPATH, '//header/nav[1]/div[1]/a[1]/*[1]').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        self.driver.quit()