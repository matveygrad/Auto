from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
import time

@allure.suite("Тесты формы регистрации")
class TestRegistrationForm:
    @pytest.fixture(scope="function")
    def setup(self):
        # Инициализация драйвера
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://ru.hexlet.io/session/new")

        yield self.driver

        # Закрытие браузера после теста
        with allure.step("Закрытие браузера"):
            self.driver.quit()

    def test_successful_registration(self, setup):
        driver = setup

        # Заполнение формы
        with allure.step("Заполнение поля email"):
            first_name = driver.find_element("xpath", "//input[@type='email']")
            first_name.send_keys("aaaaa@mail.ru")
        time.sleep(2)

        with allure.step("Заполнение поля password"):
            last_name = driver.find_element("xpath", "//input[@type='password']")
            last_name.send_keys("12344556")
        time.sleep(2)

        #Капчу нажать не получается, нужно нажать вручную
        #Следующие строки написаны, если б это был чекбокс

        #with allure.step("Активация чекбокса"):
            #WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", "//input[@type='checkbox']"))).click()
            #checkbox = driver.find_element("xpath", "//input[@type='checkbox']")
            #checkbox.click()

        with allure.step("Нажатие кнопки войти"):
            register_button = driver.find_element("xpath", "//input[@type='submit']")
            register_button.click()

        #Проверка успешности входа, вариант поиска приветственного слова
        #Для просмотра отчета в Allure эти стркоки надо закоментить или удалить
        try:
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "success-message"))
            )
            assert "Добро пожаловать" in success_message.text
        except:
            pytest.fail("Регистрация не прошла успешно")

        #Для проверки входа можно сравнить ожидаемый URL и полученный driver.current_url
