from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://digitalauto.netlify.app/")
driver.maximize_window()
driver.implicitly_wait(10) # Set timeout = 10s

# Click the Sign in button
driver.find_element(By.XPATH, "//div[text()='Sign in']").click()

# Enter email & password
wrong_pwd = "31280129850"
correct_pwd = "blablabla"
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("vuy4hc@bosch.com")
pwd_input = driver.find_element(By.XPATH, "//input[@type='password']")

# Case 1 wrong password
pwd_input.send_keys(wrong_pwd)
driver.find_element(By.XPATH, "//div[@class='px-2']/div[4]").click()
wait = WebDriverWait(driver, 2)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='text-red-500 text-sm mb-3 pl-1']")))
login_error = driver.find_element(By.XPATH, "//div[@class='text-red-500 text-sm mb-3 pl-1']").text
assert (login_error == "Invalid username or password")
    
# Case 2 correct password
pwd_input.send_keys(Keys.CONTROL,'A')
pwd_input.send_keys(Keys.BACK_SPACE)
pwd_input.send_keys(correct_pwd)
driver.find_element(By.XPATH, "//div[@class='px-2']/div[6]").click()
user_button = driver.find_element(By.XPATH, "//div[@class='flex h-full text-xl items-center px-4 !w-fit max-w-fit text-center text-gray-400 cursor-pointer py-2 border-b-2 border-transparent']//*[name()='svg']")
user_button.click() # Click the user
wait = WebDriverWait(driver, 2)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[text()='User Profile']")))
dropdown_info = driver.find_element(By.XPATH, "//div[text()='User Profile']").text
assert (dropdown_info == "User Profile")

time.sleep(10)