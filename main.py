from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

dr = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")  # указать путь к вебдрайверу

num_xpath = '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[1]/input'
but_xpath = '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/button/span'
ne_pomnu_xpath = '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/span[3]'


def wait_of_element_located(xpath):
    element = WebDriverWait(dr, 3).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def check_correct(xpath):
    dr.get("https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983")
    wait_of_element_located(xpath)
    dr.find_element(By.XPATH, xpath).send_keys("х940се790")
    dr.find_element(By.XPATH, but_xpath).click()

    try:
        wait_of_element_located('//*[@id="input-26"]')
        print("success")

    except TimeoutException:
        if dr.find_element(By.XPATH, xpath).get_attribute("style") in "background-color: rgb(254, 212, 203);":
            print("failed")
        else:
            print("success")


def check_incorrect(xpath, *keys):
    dr.get("https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983")
    element = wait_of_element_located(xpath)

    if keys is not None:
        dr.find_element(By.XPATH, xpath).send_keys(keys)

    if element.get_attribute("value") != keys:
        print("success")
    else:
        print("failed")


def check_ne_pomnu():
    dr.get("https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983")
    element = wait_of_element_located(ne_pomnu_xpath)
    element.click()
    try:
        wait_of_element_located('//*[@id="input-24"]')
        print("success")
    except TimeoutException:
        print("failed")


if __name__ == '__main__':
    check_correct(num_xpath)
    check_incorrect(num_xpath, "1ххх11ххх")
    check_incorrect(num_xpath, "         ")
    check_incorrect(num_xpath, "!!!!!!!!!")
    check_incorrect(num_xpath)
    check_ne_pomnu()
    dr.quit()


