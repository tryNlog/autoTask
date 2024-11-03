# In[1]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from makeChasuMail import chasuMail

# 메일 주소 업로드
callAdd = ', '.join(chasuMail().values)

# 메일 본문 업로드
callCon = open('IPATH/.html', 'r')
writeCon = callCon.read()

# Chrome 웹 드라이버 생성
driver = webdriver.Chrome('IPATH/chromedriver.exe')

# url 로딩
driver.get('https://mail.url.co.kr')

# 해당 사이트의 제목 확인
assert "Title" in driver.title

# 메인페이지의 로그인 버튼 클릭
# elem = driver.find_element_by_class_name('lg_global_btn')
# elem.click()

# id 입력
elem = driver.find_element_by_id("m_id")
elem.send_keys("ID")

#pwd 입력
elem = driver.find_element_by_id("m_pwd")
elem.send_keys("PWD")

# 로그인 버튼 클릭
elem = driver.find_element_by_class_name("btn-success")
elem.click()

# 편지 쓰기 버튼 클릭
elem = driver.find_element_by_class_name("navbar-link")
elem.click()

#수신자 이메일 입력
elem = driver.find_element_by_id("mf_to")
elem.send_keys(callAdd, ", recipient1, recipient2, recipient3")

#iframe 우회
driver.switch_to_frame("mf_body_html_ifr")

#이메일 본문 입력
elem = driver.find_element_by_class_name("mceContentBody")
elem.send_keys(writeCon)
# %%
