import pandas as pd
from selenium import webdriver
driver = webdriver.Chrome()

url = 'https://www.youtube.com/user/PewDiePie/videos'

driver.get(url)
videos = driver.find_elements_by_class_name(
    'style-scope ytd-grid-video-renderer')

dictlist = []

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath(
        './/*[@id="metadata-line"]/span[1]').text
    time = video.find_element_by_xpath(
        './/*[@id="metadata-line"]/span[2]').text
    dicti = {"title": title, "views": views, "time": time}
    print(f"Saving  :  {title}")

    dictlist.append(dicti)
df = pd.DataFrame(dictlist)

print(df)
