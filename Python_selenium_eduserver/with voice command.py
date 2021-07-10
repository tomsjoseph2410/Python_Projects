import speech_recognition as sr
from selenium import webdriver

record = sr.Recognizer()

with sr.Microphone() as source2:


    record.adjust_for_ambient_noise(source2, duration=0.2)
    audio2 = record.listen(source2)


    MyText = record.recognize_google(audio2)
    MyText = MyText.lower()

    if MyText=="attendance":


        driver = webdriver.Chrome()

        url = 'https://eduserver.nitc.ac.in/login/index.php'

        driver.get(url)




        driver.find_element_by_xpath('//*[@id="username"]').send_keys('Userid')
        driver.find_element_by_xpath('//*[@id="password"]').send_keys('Password')
        driver.find_element_by_xpath(
            '//*[@id="region-main"]/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/button').click()

    else:
        print("Sorry I cant hear You")
