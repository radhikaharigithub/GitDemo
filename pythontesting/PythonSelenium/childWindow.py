from selenium import webdriver #webdriver is a class present in selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# not to close the browser immediately
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\itsra\Downloads\chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(windowsopened[0])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(windowsopened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
