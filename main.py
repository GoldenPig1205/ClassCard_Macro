from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, traceback

options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(2)

ID = ''
PW = ''
path = ''

driver.get("https://www.classcard.net/Login")
driver.find_element(By.XPATH, '//*[@id="login_id"]').send_keys(ID)
driver.find_element(By.XPATH, '//*[@id="login_pwd"]').send_keys(PW)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[3]/button').click()

driver.find_element(By.XPATH, path).click()

left_card = ['//*[@id="left_card_0"]/div/div[1]', '//*[@id="left_card_1"]/div/div[1]',
             '//*[@id="left_card_2"]/div/div[1]', '//*[@id="left_card_3"]/div/div[1]']
right_card = ['//*[@id="right_card_0"]/div/div', '//*[@id="right_card_1"]/div/div',
              '//*[@id="right_card_2"]/div/div', '//*[@id="right_card_3"]/div/div']

word_dict = {}

driver.find_element(By.XPATH, '//*[@id="is_show_back"]').click()

for i in range(1, 1001):
    try:
        mp3 = driver.find_element(By.XPATH, f'//*[@id="tab_set_section"]/div/div[2]/div/div[{i}]/div[4]/div[1]/div[3]/a').get_attribute('data-src')
        word_dict[mp3] = driver.find_element(By.XPATH, f'//*[@id="tab_set_section"]/div/div[2]/div/div[{i}]/div[4]/div[2]').text
    except Exception:
        break

driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div[5]').click()
driver.find_element(By.XPATH, '//*[@id="wrapper-learn"]/div[1]/div[1]/div/div/div[2]/div[4]/a').click()
time.sleep(2)

t = int(time.time())

while True:
    try:
        while t + 180 > int(time.time()):
            for target_word in left_card:
                for result_word in right_card:
                    if word_dict[driver.find_element(By.XPATH, target_word + '/div/a/i').get_attribute('data-src')] == \
                            driver.find_element(By.XPATH, result_word + '/div/div').text:
                        driver.find_element(By.XPATH, target_word).click()
                        driver.find_element(By.XPATH, result_word).click()
                        time.sleep(0.6)
                        continue

    except:
        traceback.print_exc()
