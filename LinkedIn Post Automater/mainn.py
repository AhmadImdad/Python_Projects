from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)

# Navigate to LinkedIn login page
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

# Locate and enter email
email = driver.find_element(By.NAME, "session_key")
email.send_keys("")

# Locate and enter password
password = driver.find_element(By.NAME, "session_password")
password.send_keys("")

# Locate and click login button
button = driver.find_element(By.CSS_SELECTOR, "form div button")
button.click()

# Wait until the Jobs link is clickable and then click it
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Jobs"))
).click()

# Wait until the Post a free job link is clickable and then click it
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Post a free job"))
).click()

driver.implicitly_wait(11)
input_post = driver.find_element(By.ID, value="job-title-typeahead-input-ember26")
input_post.send_keys("armad")

company_post = driver.find_element(By.ID, value="company-typeahead-input-ember34")
company_post.send_keys("armadddd")
driver.implicitly_wait(3)
temp_button1 = driver.find_element(By.CSS_SELECTOR, value='div div div section div h1')
temp_button1.click()

viewbox_button = driver.find_element(By.XPATH, value='//*[@id="workplace-type-selection-dropdown-ember38"]/li-icon')
viewbox_button.click()

temp_button = driver.find_element(By.XPATH, value='//*[@id="ember41"]')
temp_button.click()

location = driver.find_element(By.ID, value="location-typeahead-input-ember42")
location.send_keys("Faisalabad")
time.sleep(5)
location.send_keys(Keys.DOWN)
location.send_keys(Keys.ENTER)
temp_button1.click()
save_button = driver.find_element(By.ID, value="ember54")
save_button.click()