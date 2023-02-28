from selenium import webdriver #webdriver is a class present in selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# not to close the browser immediately
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\itsra\Downloads\chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr") # switch to frames
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)



