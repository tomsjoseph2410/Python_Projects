import pandas as pd
from selenium import webdriver
import pywhatkit
import datetime

current = datetime.datetime.now()
hour = current.hour
minutes = current.minute

driver = webdriver.Chrome()

#to collect the video details
url = 'https://www.youtube.com/channel/UCBo6rx7NFjFCpBhILuOCQqA/videos'

driver.get(url)
videos = driver.find_elements_by_class_name(
    'style-scope ytd-grid-video-renderer')

dictlist = []

for video in videos:
    link = video.find_element_by_xpath('.//*[@id="video-title"]').get_attribute('href')
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath(
        './/*[@id="metadata-line"]/span[1]').text
    time = video.find_element_by_xpath(
        './/*[@id="metadata-line"]/span[2]').text
    dicti = {"title": title, "views": views, "time": time,"link":link}
    print(f"Saving  :  {title}")

    dictlist.append(dicti)
df = pd.DataFrame(dictlist)


pywhatkit.sendwhatmsg('Phone number',f" WATCH THESE  {df} ",hour,minutes+1)

print(df)
