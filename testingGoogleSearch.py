from selenium import webdriver
options = webdriver.ChromeOptions()

#options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.google.com")

driver.implicitly_wait(10)
searchBar = driver.find_element_by_name("q")
driver.find_element_by_id
searchBar.click()
searchBar.send_keys("Selenium")


driver.close()