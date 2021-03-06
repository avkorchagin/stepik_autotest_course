from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome()
    driver.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = driver.find_element_by_css_selector('.first_block .form-group > .first[required]')
    first_name.send_keys('FirstName')

    last_name = driver.find_element_by_css_selector('.first_block .form-group > .second[required]')
    last_name.send_keys('LastName')



    email = driver.find_element_by_css_selector('.first_block .form-group > .third[required]')
    email.send_keys('email@example.com')


    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

    assert "Congratulations! You have successfully registered!" == welcome_text
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()