from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#사용하고자 하는 브라우저
driver = webdriver.Safari()

#접근하고자 하는 URL
url = 'https://app.modusign.co.kr'

#URL 접근하기
driver.get(url)

#name 요소 찾기
Email = driver.find_element_by_name("email")
#요소 내용 초기화
Email.clear()
#요소 내용 입력
Email.send_keys("sh.shin@modusign.co.kr")

Password = driver.find_element_by_name("password")
Password.clear()
Password.send_keys("1234qwer!!")
#Enter key (Keys.ENTER)로 작성해도 됨
Password.send_keys(Keys.RETURN)
