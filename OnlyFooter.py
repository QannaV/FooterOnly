import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список страниц
pages = [
    "https://only.digital/projects",
    "https://only.digital/company",
    "https://only.digital/fields",
    "https://only.digital/job",
    "https://only.digital/blog",
    "https://only.digital/contacts"
]

driver = webdriver.Chrome()

timeout = 10

for url in pages:
    driver.get(url)
    print(f"\nПроверка страницы: {url}")

    # Ожидаем, что футер станет видимым
    try:
        footer = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/main/footer'))
        )
        print("Футер найден и отображается.")

        # Ожидаем появления Email в футере
        try:
            logo = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/main/footer/div[1]/div[3]/a[1]'))
            )
            print("Email найден.")
        except TimeoutException:
            print("Email не найден.")

        # Ожидаем появления кнопки скачивания презентации
        try:
            download_pdf = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/main/footer/div[1]/div[4]/div/a[1]'))
            )
            print("Кнопка скачивания презентации о компании найдена.")
        except TimeoutException:
            print("Кнопка скачивания презентации о компании не найдена.")

        # Ожидаем появления кнопки "Начать проект"
        try:
            start_project_button = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/main/footer/div[1]/button'))
            )
            print("Кнопка 'Начать проект' найдена.")
        except TimeoutException:
            print("Кнопка 'Начать проект' не найдена.")

    except TimeoutException:
        print("Футер не найден или не загрузился на странице.")
    except NoSuchElementException:
        print("Футер не найден в DOM.")
    except Exception as e:
        print("Произошла ошибка: {e}")

# Закрытие драйвера после завершения проверки
driver.quit()