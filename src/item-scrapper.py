from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def init_mannequin():
  init_button = driver.find_element(By.XPATH, '//button[text()="프리셋 초기화"]')
  init_button.click()

  wait.until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="초기화"]'))
  ).click()


if __name__ == '__main__':
  driver.get('https://meaegi.com/dressing-room')

  init_mannequin()

  driver.quit()