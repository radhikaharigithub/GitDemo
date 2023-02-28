from selenium import webdriver #webdriver is a class present in selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# not to close the browser immediately
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service(r"C:\Users\itsra\Downloads\chromedriver_win32.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# //a[contains(@href, 'shop')] a[href*= 'shop']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

cards = driver.find_element(By.CSS_SELECTOR, ".card-title a")

i = -1
card = []
cards = []
for card in cards:
    i = i+1
    cardText = card.text
    print(cardText)
    if cardText == "Blackberry":
        card.find_element(By.CSS_SELECTOR, ".card-footer button")[i].click()

driver.find_element(By.CSS_SELECTOR, "a[class*=btn-primary]").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText
driver.close()
