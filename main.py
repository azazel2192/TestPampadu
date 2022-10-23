from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

dr = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")  # указать путь к вебдрайверу

correct_num = "х947се790"
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
    dr.find_element(By.XPATH, xpath).send_keys(correct_num)
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

    check_value = element.get_attribute("value") + dr.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div''/div'
                                                                             '[3]''/div/div[1]/div/div/div[2]''/input')\
        .get_attribute("value")
    check_value = "".join(check_value.lower().split(" "))
    check_keys = "".join(keys)
    if check_value != check_keys:
        print("success")
    else:
        try:
            wait_of_element_located('//*[@id="input-24"]')
            print("failed")
        except TimeoutException:
            print("success")


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
    check_correct(num_xpath)  # test case №1
    check_incorrect(num_xpath, "1")  # test case №2
    check_incorrect(num_xpath, "хх")  # test case №3
    check_incorrect(num_xpath, "!")  # test case №4
    check_incorrect(num_xpath)  # test case №5
    check_incorrect(num_xpath, " ")  # test case №6
    check_incorrect(num_xpath, correct_num, " ")  # test case №7
    check_incorrect(num_xpath, correct_num, "0х")  # test case №8
    check_ne_pomnu()  # test case №9
    dr.quit()


