from selenium import webdriver
import pywhatkit
import datetime

op = webdriver.ChromeOptions()
op.add_argument('headless')

current = datetime.datetime.now()

hour = current.hour
minutes = current.minute

driver = webdriver.Chrome(options=op)
driver.get("https://www.youtube.com/channel/UCBo6rx7NFjFCpBhILuOCQqA/videos")

k = driver.find_element_by_xpath('//*[@id="metadata-line"]/span[2]').text.split()
link = driver.find_element_by_xpath('//*[@id="video-title"]').get_attribute('href')

if 'Streamed' in k:
    pywhatkit.sendwhatmsg("+ receivers number ", f"Hai,Watch my Friend's Latest Video {link}", hour, minutes + 1)
else:
    print("Error")
