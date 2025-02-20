import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 下拉式選單使用
from selenium.common.exceptions import NoSuchElementException  # Handle exception
from ocr_component import get_captcha_code


options = webdriver.ChromeOptions()  # 創立 driver物件所需的參數物件
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.get("https://irs.thsrc.com.tw/IMINT/")


# 台灣高鐵網路訂票系統個人資料使用說明, 點擊'我同意'
accept_cookie_button = driver.find_element(By.ID, "cookieAccpetBtn")
accept_cookie_button.click()
# 選擇出發站
start_select= driver.find_element(By.NAME,'selectStartStation')
Select(start_select).select_by_visible_text('台中')
# 選擇抵達站
end_select = driver.find_element(By.NAME, 'selectDestinationStation')
Select(end_select).select_by_visible_text('左營')
# 選擇出發時間
time_select = driver.find_element(By.NAME, 'toTimeTable')
Select(time_select).select_by_visible_text('10:00')
# 選擇出發日期
start_date = '二月 26, 2025'
driver.find_element(By.XPATH, "//input[@class='uk-input' and @readonly='readonly']").click()
driver.find_element(By.XPATH, f"//span[@class='flatpickr-day' and @aria-label='{start_date}']").click()


# 驗證碼
while True:
    captcha_img = driver.find_element(By.ID, 'BookingS1Form_homeCaptcha_passCode')
    captcha_img.screenshot('captcha.png')       # .screenshot 保存當前頁面的螢幕圖像
    captcha_code = get_captcha_code()
    captcha_input = driver.find_element(By.ID, 'securityCode')
    captcha_input.send_keys(captcha_code)
    time.sleep(2)

    # 開始查詢
    submit_button = driver.find_element(By.ID, 'SubmitButton')
    submit_button.click()
    time.sleep(5)

    # Check validation is success or not
    try:
        #driver.find_element(By.CLASS_NAME, 'uk-alert-danger uk-alert')
        driver.find_element(By.ID, 'divErrMSG')
    except NoSuchElementException:
        print("進到第二步驟")
        break


time.sleep(2000)
driver.quit()