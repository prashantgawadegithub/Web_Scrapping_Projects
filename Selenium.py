## Python Silenium - Find Elements_by_XPath

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys

s=Service("C:/Users/PRASHANT GAWADE/Desktop/Silenium/chromedriver.exe")
driver=webdriver.Chrome(service=s)
# driver.get("https://www.datacouncil.in/")

## Python Selenium - Find Element_by_XPath

# driver.find_element_by_xpath("""/html/body/div[3]/div[2]/div[1]/div/div[1]/img""")

# driver.find_element_by_xpath("""/html/body/section[2]/div[1]/div/div[2]/div/div[3]/a""")

# # Python Selenium - Click a Button

# driver.get("https://www.tutorialsfreak.com/")
# time.sleep(5)
# driver.find_element_by_xpath("""/html/body/div/div[2]/div/section[1]/div/div[1]/div/div/div/div[2]/button""").click()
#
# time.sleep(2)
# driver.find_element_by_xpath("""/html/body/div/div[2]/div/section/div/div[2]/div[1]/div/ul/li[7]/a""").click()

# # Python Selenium - Taking User Input

# driver.get("https://www.google.com/")
#
# time.sleep(2)
# search=driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea""")
# time.sleep(1)
# search.send_keys("datacouncil")
# search.send_keys(Keys.ENTER)

# driver.get("https://twitter.com/i/flow/login?lang=en")
#
# time.sleep(10)
# ph_no=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
# ph_no.send_keys("123456")
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]").click()


# # Python Selenium - Taking Screenshot

# driver.get("https://www.tutorialsfreak.com/")
# time.sleep(3)
# driver.save_screenshot("C:/Users/PRASHANT GAWADE/Desktop/Silenium/full-page.png")

# driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/section[1]/div/div[1]/div/div/div/div[3]/span/img").screenshot("C:/Users/PRASHANT GAWADE/Desktop/Silenium/girl.png")

# # Python Selenium - Scrolling a Webpage
# # search pandas images

# driver.get("https://www.google.com/search?sca_esv=557053058&q=pandas&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiSoeufqN6AAxXua2wGHejEBVUQ0pQJegQIDRAB&biw=1366&bih=606&dpr=1")
# time.sleep(5)
# height=driver.execute_script("return document.body.scrollHeight")
# print(height)
# while True:
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


# # Python Selenium - Wait Times

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# driver.get("https://twitter.com/i/flow/login?lang=en")
#
# # time.sleep(10)
# element=WebDriverWait(driver,5).until(ec.presence_of_element_located((By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/div[2]/span/span")))
# ph_no=driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
# ph_no.send_keys("123456")
# time.sleep(5)
# driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]").click()

# # Project on House of the Dragon

# driver.get("https://www.google.com/")
# time.sleep(2)
# search=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
# search.send_keys("House of the dragon")
# search.send_keys(Keys.ENTER)
# time.sleep(3)
# driver.find_element_by_xpath("""/html/body/div[6]/div/div[13]/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[4]/div/div/div/div/div/div[1]/div/div/a/h3""").click()
# time.sleep(4)
# driver.save_screenshot("C:/Users/PRASHANT GAWADE/Desktop/Silenium/dragon.png")

# # Websites with Infinite Scrolling
# # Nike, AJIO

# # How to Scroll Infinitely - Ajio Inida
# # ajio -women footware - sneakers

# driver.get("""https://www.ajio.com/s/footwear-4792-56592?query=%3Arelevance%3Al1l3nestedcategory%3AWomen%20-%20Sneakers&curated=true&curatedid=footwear-4792-56592&gridColumns=3""")
# time.sleep(10)
# height = driver.execute_script("return document.body.scrollHeight")
# print(height)
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# while True:
#     height=driver.execute_script("return document.body.scrollHeight")
#     print(height)
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(10)
#     new_height=driver.execute_script("return document.body.scrollHeight")
#     if height==new_height:
#         break


# # Sales - mens shoes

driver.get("https://www.nike.com/in/w/mens-sale-shoes-3yaepznik1zy7ok")
time.sleep(10)
while True:
    height=driver.execute_script("return document.body.scrollHeight")
    print(height)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)
    new_height=driver.execute_script("return document.body.scrollHeight")
    if height==new_height:
        break