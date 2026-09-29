import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_button_add_to_basket_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Ждем, пока кнопка появится на странице
    button = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )

    # Пауза, чтобы визуально проверить язык интерфейса
    time.sleep(30)

    # Проверяем, что кнопка видна
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена"