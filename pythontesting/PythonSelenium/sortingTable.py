from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service_obj = Service(r"C:\Users\itsra\Downloads\chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

browserSortedVeggies = []

#click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

#collect all veggie names
veggieWebElement = driver.find_elements(By.XPATH, "//tr/td[1]")
for veggie in veggieWebElement:
    browserSortedVeggies.append(veggie.text)
print(browserSortedVeggies)
originalBrowserSortedList = browserSortedVeggies.copy()

#sort veggielist
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList
