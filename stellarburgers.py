from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker

class TestStellarBurgers():

    def setup_class(self):
        fake = Faker()
        self.email = fake.email()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_registration_with_a_blank_name(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        name = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
        assert name is None


    def test_registration_with_an_incorrect_password(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Kirill')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('1')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
        assert self.driver.find_element(By.XPATH, '//p[contains(text(),"Некорректный пароль")]')

    def test_registration_with_the_correct_password(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys('Kirill')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input').send_keys('123456')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Зарегистрироваться")]').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/h2')

    def test_authorization(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Войти")]')))
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()

    def test_authorization_via_the_registration_form(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Войти")]')))
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()

    def test_authorization_via_password_recovery(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Войти")]')))
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()

    def test_authorization_in_via_the_log_in_to_account_button(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти в аккаунт")]').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input').send_keys(self.email)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input').send_keys('123456')
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Войти")]')))
        self.driver.find_element(By.XPATH, '//button[contains(text(),"Войти")]').click()

    def test_transfer_to_your_personal_account(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Сохранить")]')))
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a')

    def test_switching_from_your_personal_account_to_the_constructor_and_click_stellarburgers(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p').click()
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        self.driver.find_element(By.XPATH, '//header/nav[1]/div[1]/a[1]/*[1]').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')

    def test_go_to_the_sauces_section(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span')

    def test_go_to_the_fillings_section(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]').click()
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span')

    def test_go_to_the_rolls_section(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')
        assert self.driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span')

    def test_log_out_of_your_personal_account(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Сохранить")]')))
        self.driver.find_element(By.XPATH, "//button[text()='Выход']").click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, '//h2[contains(text(),"Вход")]')))
        assert self.driver.find_element(By.XPATH, '//h2[contains(text(),"Вход")]')