from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructor():

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_go_to_the_sauces_section(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('jessica04@example.com')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')
        self.driver.quit()

    def test_go_to_the_fillings_section(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('jessica04@example.com')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')
        self.driver.quit()

    def test_go_to_the_rolls_section(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('jessica04@example.com')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')))
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')
        self.driver.quit()