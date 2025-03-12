from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def init_mannequin():
  init_button = driver.find_element(By.XPATH, '//button[text()="프리셋 초기화"]')
  init_button.click()

  wait.until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="초기화"]'))
  ).click()


def choose_beauty_item(hair, face):
  search_box = driver.find_element(By.XPATH, '//input[@placeholder="아이템 이름 검색"]')
  search_box.send_keys(hair)
  hair_name = wait.until(
    EC.presence_of_element_located((By.XPATH, f'//div[normalize-space(text())=""]/span[text()="{hair}"]'))
  )
  hair_item = hair_name.find_element(By.XPATH, '../../..')
  hair_item.click()

  search_box.send_keys(Keys.CONTROL + 'a')
  search_box.send_keys(face)
  face_name = wait.until(
    EC.presence_of_element_located((By.XPATH, f'//div[normalize-space(text())=""]/span[text()="{face}"]'))
  )
  face_item = face_name.find_element(By.XPATH, '../../..')
  face_item.click()

  search_box.send_keys(Keys.CONTROL + 'a')
  search_box.send_keys(Keys.BACK_SPACE)


if __name__ == '__main__':
  driver.get('https://meaegi.com/dressing-room')

  init_mannequin()
  choose_beauty_item('데이즈 헤어(여)', '조용한 눈 얼굴(여)')

  input('아무거나 입력하세요.')

  driver.quit()