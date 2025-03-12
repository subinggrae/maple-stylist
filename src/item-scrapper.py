from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)


def init_mannequin():
  init_btn = driver.find_element(By.XPATH, '//button[text()="프리셋 초기화"]')
  init_btn.click()

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


def dye_hair(base_color, mix_color=None, mix_ratio=0):
  dye_mode_btn = driver.find_element(By.XPATH, '//button[text()="염색모드"]')
  dye_mode_btn.click()

  base_color_img = wait.until(
    EC.presence_of_element_located((By.XPATH, f'//img[@alt="{base_color}"]'))
  )
  base_color_img.click()

  if mix_color:
    mix_color_img = driver.find_elements(By.XPATH, f'//img[@alt="{mix_color}"]')[1]
    driver.execute_script('arguments[0].scrollIntoView(true)', mix_color_img)
    mix_color_img.click()
    mix_ratio_input = driver.find_elements(By.XPATH, '//input[@inputmode="numeric"]')[1]
    mix_ratio_input.send_keys(Keys.CONTROL + 'a')
    mix_ratio_input.send_keys(mix_ratio)


if __name__ == '__main__':
  driver.get('https://meaegi.com/dressing-room')

  init_mannequin()
  choose_beauty_item('데이즈 헤어(여)', '조용한 눈 얼굴(여)')
  dye_hair('초', '갈', 59)

  input('아무거나 입력하세요.')

  driver.quit()