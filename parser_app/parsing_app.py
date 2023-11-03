from selenium.webdriver import Chrome, ChromeOptions

from parser_app.links_list import links_for_parser
from parser_app.pars_phone_from_halooglasi import get_phone_and_spacename_list
from parser_app.postgres.connectors.marketing_connector import MarketingConnector
from parser_app.postgres.database import get_database

options = ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--window-position=0,0")
options.add_argument("window-size=1920,1080")
options.add_argument("--disableself.proxy-infobars")
options.add_argument("--dns-prefetch-disable")

marketing_connector = MarketingConnector(get_database())
driver = Chrome(options=options)

if __name__ == "__main__":
    space_info = get_phone_and_spacename_list(driver=driver, links_list=links_for_parser)
    for space in space_info:
        marketing_connector.save(space)
