import time
import os
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 下拉式選單使用
from selenium.common.exceptions import NoSuchElementException  # Handle exception
from ocr_component import get_captcha_code


options = webdriver.ChromeOptions()  # 創立 driver物件所需的參數物件
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.get("https://irs.thsrc.com.tw/IMINT/")


"""
第一個頁面 "查詢車次"
"""

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

    # Check validation is success or not
    try:
        time.sleep(5)
        driver.find_element(By.ID, 'BookingS2Form_TrainQueryDataViewPanel')
        print("驗證碼正確,進到第二步驟")
        break
    except NoSuchElementException:
        print("驗證碼錯誤")




"""
第二個頁面 "選擇車次"
"""

trains_info = list()
trains = driver.find_element(By.CLASS_NAME, 'result-listing').find_elements(By.TAG_NAME, 'label')
for train in trains:
    # depart_time = train.find_element(By.ID, 'QueryDeparture').text
    # arrival_time = train.find_element(By.ID, 'QueryArrival').text
    # duration = train.find_element(
    #     By.CLASS_NAME, 'duration').find_elements(By.TAG_NAME, 'span')[1].text
    # train_code = train.find_element(By.ID, 'QueryCode').text
    # radio_box = train.find_element(By.CLASS_NAME, 'uk-radio')
    info = train.find_element(By.CLASS_NAME, 'uk-radio')

    trains_info.append(
        {
            # .get_attribute 從一個元素中提取各種屬性
            'depart_time': info.get_attribute('querydeparture'),
            'arrival_time': info.get_attribute('queryarrival'),
            'duration': info.get_attribute('queryestimatedtime'),
            'train_code': info.get_attribute('querycode'),
            'radio_box': info,
        }
    )

pprint(trains_info)

# Choose train
for idx, train in enumerate(trains_info):
    print(
        f"({idx}) - {train['train_code']}, 行駛時間={train['duration']} | {train['depart_time']} -> {train['arrival_time']}")

which_train = int(input("Choose your train. Enter from 0~9:\n"))
trains_info[which_train]['radio_box'].click()

# Submit booking requests
driver.find_element(By.NAME, 'SubmitButton').click()
print("選擇成功, 進到第三步驟")



"""
第三個頁面 "取票資訊"
"""
print("確認訂票: ")
print(
    f"車次: {trains_info[which_train]['train_code']} | \
    行駛時間: {trains_info[which_train]['duration']} | \
    {trains_info[which_train]['depart_time']} -> \
    {trains_info[which_train]['arrival_time']}"
)
print('您的車票共 ', driver.find_element(By.ID, 'TotalPrice').text, " 元")
driver.find_element(By.CLASS_NAME, 'ticket-summary').screenshot('thsr_summary.png')

id_input = driver.find_element(By.ID, 'idNumber')
id_number = input("請輸入你的身分證: ")
#id_number = os.getenv('Personal_ID')      # 從環境變數拿   # 打開電腦的'編輯系統環境變數'新增'Personal_ID'
id_input.send_keys(id_number)

phone_input = driver.find_element(By.ID, 'mobilePhone')
phone_number = input("請輸入你的手機號碼: ")
#phone_number = os.getenv('Personal_phone')      # 從環境變數拿
phone_input.send_keys(phone_number)

mail_input = driver.find_element(By.ID, 'email')
mail = input("請輸入你的電子郵件: ")
#mail = os.getenv('Personal_email')      # 從環境變數拿
mail_input.send_keys(mail)

# 勾選我已明確了解
driver.find_element(By.NAME, 'agree').click()

# 按完成訂位
driver.find_element(By.ID, 'isSubmit').click()







time.sleep(2000)
driver.quit()