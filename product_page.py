from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket"))
        )
        button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        """Возвращает название товара со страницы"""
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text

    def get_product_price(self):
        """Возвращает цену товара со страницы"""
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text

    def should_be_add_to_basket_message(self):
        """Проверяет, что название товара в сообщении совпадает с названием на странице"""
        product_name = self.get_product_name()
        message_name = self.browser.find_element(
            By.CSS_SELECTOR, "#messages .alertinner strong"
        ).text
        assert product_name == message_name, \
            f"Название товара не совпадает: {product_name} != {message_name}"

    def should_be_basket_price_message(self):
        """Проверяет, что цена в сообщении совпадает с ценой товара"""
        product_price = self.get_product_price()
        basket_price = self.browser.find_element(
            By.CSS_SELECTOR, "#messages .alertinner p strong"
        ).text
        assert product_price == basket_price, \
            f"Цена не совпадает: {product_price} != {basket_price}"