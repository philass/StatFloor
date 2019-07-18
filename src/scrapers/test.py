from selenium import webdriver
from time import sleep
driver = webdriver.Firefox(executable_path="/Users/philiplassen/CS/drivers/geckodriver")
url = "https://www.baseball-reference.com/players/split.fcgi?id=troutmi01&year=2019&t=b"
driver.get(url)
sleep(5)
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
print(type(html))
driver.quit()
