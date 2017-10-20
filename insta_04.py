from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import insta_db as db
import insta_cont as cont


# 중복 아이디 정리 하기
db.arrange_id()

# 검색할 아이디 리스트로 만들기 (갯수)
instaids_2nd = db.search_list (600)

# 시작
driver2 = webdriver.Chrome('chromedriver')
driver2.get('https://www.instagram.com')

time.sleep(2)

login = driver2.find_elements_by_css_selector('a._b93kq')
login[0].click()

# 로그인 페이지 접속
uid = driver2.find_element_by_name("username")
uid.send_keys('bbbongerrr')
upw = driver2.find_element_by_name("password")
upw.send_keys('qhdtjr66')
time.sleep(2)

# 로그인 크릭
loginbutton = driver2.find_element_by_css_selector('button._qv64e')
loginbutton.click()

time.sleep(3)

# 검색창 클릭
searchbar = driver2.find_element_by_css_selector('div._eduze._mknn3')
searchbar.click()

for instaid_2nd in instaids_2nd :

    # 검색창에 ID입력
    insert_follower = driver2.find_element_by_css_selector("input._avvq0._o716c")
    insert_follower.send_keys(instaid_2nd[1])

    time.sleep(2)

    # 계정클릭
    follower_click = driver2.find_elements_by_css_selector('div._etpgz a._gimca')
    follower_click[0].click()

    time.sleep(2)

    # 팔로워 스크랩
    list_followernum = driver2.find_elements_by_css_selector("span._fd86t")

    # 팔로워에 천 or 백만이 있으면 걸러주는 함수 텍스트->플로팅
    followernum = cont.change_followernum ( list_followernum[1].text )

    # 팔로워 숫자 저장하는 함수
    db.save_followernum( followernum, instaid_2nd[0])


driver2.close()
