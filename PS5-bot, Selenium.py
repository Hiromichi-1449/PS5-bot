from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager

import time

options = Options()
options.set_preference("geo.prompt.testing", True)
options.set_preference("geo.prompt.testing.allow", False)
options.set_preference("geo.enabled", False)  # Disables geolocation

# declare email address & password:
username = "your email account"
password = "your password"


# Launch the BestBuy: https://www.bestbuy.com/?intl=nosplash ; Amazon: https://www.amazon.com/
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
driver.maximize_window()
driver.get("https://www.bestbuy.com/?intl=nosplash")
wait = WebDriverWait(driver, 10)

# Locate the search bar & enter the search term: gh-search-input (bestbuy); twotabsearchtextbox (Amazon)
search_bar = driver.find_element(By.ID, "gh-search-input")
search_bar.send_keys("rog ally x" + Keys.ENTER)
# Submit the search
search_bar.send_keys(Keys.RETURN)

# Find the merchandise:
wait = WebDriverWait(driver, 10)
rog_allyx = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/main/div[4]/div/div/div/div/div/div/div[2]/div[2]/div[5]/div/div[4]/ol/li[1]/div/div/div/div/div/div/div/div/div/div/div[2]/h4/a")))
rog_allyx.click()
print("roy_allyx clicked")

# Select spec (2TB drive):
spec = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/main/div[6]/div/div/div/div/div/div/div[7]/div[2]/div/div[7]/div/div/div/section/div/div/div[2]/div[2]/div/div/ul/li[2]/button")))
spec.click()
print("spec  clicked")

# Add to the cart:
add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/main/div[6]/div/div/div/div/div/div/div[7]/div[2]/div/div[15]/div[1]/div/div/div/div/div/button")))
add_to_cart.click()
print("cart clicked")

# inspect the cart:
cart_inspection = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/header/div[3]/div/div[3]/div/div[1]/div/div/div/div/a/span")
cart_inspection.click()
print("inspection clicked")

# Checkout:
checkout = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div[1]/div/div[2]/div[1]/section[2]/div/div/div[3]/div/div[1]/button")))
checkout.click()
print("check-out clicked")

# log-in:
emailAddress = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fld-e")))
emailAddress.send_keys(username + Keys.RETURN)

# log-in, password:
# Select "Use Password" option
passwordsOption = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "password-radio")))
if passwordsOption:
    passwordsOption[0].click()  # Click the first element in the list
else:
    print("No elements found with the specified ID")
password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "fld-pl")))
password_field.send_keys("your_password" + Keys.RETURN)

# Close the browser
driver.quit()

# Allow time for the product page to load
# time.sleep(3)
