from selenium import webdriver

driver=webdriver.Chrome()

url='https://eduserver.nitc.ac.in/login/index.php'

driver.get(url)


driver.find_element_by_xpath('//*[@id="username"]').send_keys('Your USER ID')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('Your PASSWORD')
driver.find_element_by_xpath('//*[@id="region-main"]/div[2]/div[2]/div[1]/div/div[2]/form/div[3]/button').click()

driver.implicitly_wait(5)
driver.find_element_by_link_text('Attendance').click()
driver.implicitly_wait(5)
driver.find_element_by_link_text('Go to activity').click()

driver.implicitly_wait(3)
driver.find_element_by_link_text('Submit attendance').click()

driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="id_status_3318"]').click()
driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()





