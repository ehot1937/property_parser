from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from parser_app.models.marketing import Marketing
from parser_app.parsing_app import marketing_connector


def parce_from_links_and_save_in_db(driver: Chrome, links_list: list):
    space_info_list = []
    for link in links_list:
        try:
            driver.get(link)
            driver.find_element(By.XPATH, '//span[@class="show-phone-span"]').click()
            driver.implicitly_wait(1.0)
            phone_element = driver.find_element(By.XPATH, '//a[contains(@href, "tel:")]')
            name_element = driver.find_element(
                By.XPATH, '//span[@id="plh1" and @data-code="Title"]'
            )
            phone_dict = {"name": name_element.text, "phone": phone_element.text}
            marketing_connector.save(Marketing(**phone_dict))
        except Exception as e:
            print(e)
            continue
