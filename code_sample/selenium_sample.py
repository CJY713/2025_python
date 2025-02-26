## 參考: https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/first_script/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select    # 下拉式選單使用

## Step 1:
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
#driver = webdriver.Safari()

## Step 2:
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

## Step 4:
driver.implicitly_wait(2)
print("driver already wait 2 secs")

## Step 5:
# text_box = soup.find(name='my-text')  # bs4的寫法
text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = soup.find('button')   # bs4的寫法
submit_button = driver.find_element(by=By.TAG_NAME, value="button")
# submit_button = soup.css.select('button')   # bs4的寫法
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

## Step 5.1: 找到其他text_box
password_text_box = driver.find_element(by=By.NAME, value="my-password")
textarea_text_box = driver.find_element(by=By.NAME, value="my-textarea")

## Step 5.2: 找到Dropdown, 選擇Two
number_dropdown = driver.find_element(By.XPATH, "//select[@class='form-select' and @name='my-select']")
number_select = Select(number_dropdown)
number_select.select_by_visible_text('Two')

## Step 6:
text_box.send_keys("XXXXXX")
password_text_box.send_keys("123456789")
textarea_text_box.send_keys("Hello World")
time.sleep(5)
submit_button.click()

## Step 7:
message = driver.find_element(by=By.CLASS_NAME, value="container")
print(message.text)



time.sleep(10)
driver.quit()

