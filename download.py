from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
import time
import pyautogui

chrome_options = Options()

is_headless = 0

if (is_headless == 1):
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("window-size=1920x1080")

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome('/home/ardy/python/chromedriver', options=chrome_options)
watch_cartoon_url = "https://www.thewatchcartoononline.tv/"
driver.get( watch_cartoon_url + "star-wars:-the-clone-wars-season-2-episode-22-lethal-trackdown")

to_download = 0
while to_download < 6:
	time.sleep(2)
	title = driver.find_element_by_class_name("video-title").text

	print("downloading " + title +" ...")
	
	write_title = open("titles.txt", "a")
	string = title.lower()
	new_link = string.replace(" ","-")

	write_title.write(new_link +"\n")
	write_title.close()

	pyautogui.moveTo(1865,525)
	pyautogui.click()
	pyautogui.scroll(-10)

	pyautogui.moveTo(1180,525)
	pyautogui.click()
	time.sleep(1)
	pyautogui.click(button='right')

	pyautogui.moveTo(1250,630)
	time.sleep(2)

	pyautogui.click()
	time.sleep(15)
	pyautogui.write(title)
	pyautogui.press('enter')

	time.sleep(2)
	driver.find_element_by_css_selector(".prev-fln .prev-next:nth-child(2)").click()

	write_title = open("titles.txt", "a")
	string = title.lower()
	new_link = string.replace(" ","-")

	to_download += 1


