
from selenium import webdriver #webdriver is a class present in selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# not to close the browser immediately
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\itsra\Downloads\chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# find element by locator-> ID, name, Xpath, css selector, class name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("adidas")
driver.find_element(By.ID, "exampleCheck1").click()

# create Xpath locator for any element
# //tagname[@atribute="value"] //input[@type=attribute]

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

# create css locator for any element
# tagname[atribute="value"] //input[@type=attribute] or #id, or .classname

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("radhika")

assert "Success" in message
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#static dropdown
dropdown_obj = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown_obj.select_by_index(1)
dropdown_obj.select_by_visible_text("Female")
#dropdown_obj.select_by_value()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


