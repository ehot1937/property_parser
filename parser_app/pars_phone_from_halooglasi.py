from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from parser_app.models.marketing import Marketing


def get_phone_and_spacename_list(driver: Chrome, links_list: list) -> list:
    space_info_list = []
    for link in links_list:
        driver.get(link)
        driver.find_element(By.XPATH, '//span[@class="show-phone-span"]').click()
        driver.implicitly_wait(1.0)
        phone_element = driver.find_element(By.XPATH, '//a[contains(@href, "tel:")]')
        name_element = driver.find_element(By.XPATH, '//span[@id="plh1" and @data-code="Title"]')
        phone_dict = {"name": name_element.text, "phone": phone_element.text}
        space_info = Marketing(**phone_dict)
        space_info_list.append(space_info)

    return space_info_list
