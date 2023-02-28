from selenium import webdriver #webdriver is a class present in selenium
from selenium.webdriver.edge.service import Service

#service_obj = Service(r"C:\Users\itsra\Downloads\chromedriver_win32.exe");
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com")

#service_obj = Service(r"C:\Users\itsra\Downloads\geckodriver-v0.32.0-win-aarch64.exe");
# driver = webdriver.Firefox(service=service_obj)
# driver.get("https://rahulshettyacademy.com")

service_obj = Service(r"C:\Users\itsra\Downloads\edgedriver_win64.exe");
driver = webdriver.Edge(service=service_obj)
driver.get("https://rahulshettyacademy.com")

print(driver.title)
print(driver.current_url)
driver.maximize_window()
driver.back()
driver.forward()
driver.minimize_window()
driver.close()

