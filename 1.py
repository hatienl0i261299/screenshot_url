from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PIL import Image
options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://zingmp3.vn/"
delay = 3
driver.get(url)
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'id')))
except Exception as e:
    pass
driver.save_screenshot("ss.png")
driver.close()
screenshot = Image.open("ss.png")
screenshot.show()
