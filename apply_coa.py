from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import getpass
import time

is_headless = 1
chrome_options = Options()

if (is_headless == 1):
	chrome_options.add_argument("window-size=1920x1080")
	chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--start-maximized')


driver = webdriver.Chrome('/home/ardy/python/chromedriver', options=chrome_options)
driver.get("http://localhost/app/application")

# username input
username = raw_input("Enter your username:")
password = getpass.getpass("Your password:")

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME, "username")))
driver.find_element_by_class_name("username").send_keys(username)
driver.find_element_by_class_name("password").send_keys(password)
driver.find_element_by_class_name("submit").click()

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME, "emp_details")))
driver.find_element_by_css_selector("#sidebar-menu li:nth-child(3)").click()

try:
	error = driver.find_element_by_class_name("error-message")
	if (error.is_displayed()):
		log_msg = "Invalid selected date. Maybe you don't have a schedule for the day."
except Exception as e:
	log_msg = "Schedule found."
	today = date(2020, 5, 4)
	i = 0
	x = 0
	while i < 10:
		start_date = today + timedelta(days=i)
		i += 1

		if (i == 6):
			x = i + 1
		start_date = today + timedelta(days=x)
		x += 1

		start_date = start_date.strftime("%Y-%m-%d")
		# open application form
		time.sleep(5)
		WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, "approved")))
		driver.find_element_by_css_selector(".filter_content .btn-primary").click()
		WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, "coa_type")))
		coa_type = Select(driver.find_element_by_id("coa_type"))
		coa_type.select_by_value("others")
		driver.find_element_by_id("shift_date0").clear()
		driver.find_element_by_id("shift_date0").send_keys(start_date);
		driver.find_element_by_id("remarks").click()
		time.sleep(15)
		driver.find_element_by_css_selector("#add_coa .submit").click()
		print(start_date)

print("Done adding coas")
driver.quit()
