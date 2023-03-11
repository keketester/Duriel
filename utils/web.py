from selenium.webdriver import *
from selenium.webdriver.common.keys import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
options = ChromeOptions()
options.binary_location = r"C:\Program Files (x86)\ChromeCore\ChromeCore.exe"
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# 88以上版本
options.add_argument('--disable-blink-features=AutomationControlled')

driver = Chrome(chrome_options=options)

# 88以下版本
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    navigator.webdriver = undefined
    Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
    })
    """
})
