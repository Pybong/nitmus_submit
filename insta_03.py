
# 검색명단 검색창에 입력해서 이동 가능
# 팔로워 갯수 DB에 저장 하는 기능 완료!!!!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import insta_db as db
import insta_cont as cont


# 검색할 아이디 리스트로 만들기 (갯수)
instaids = db.search_list (30)

# 시작
driver = webdriver.Chrome('chromedriver')
driver.get('https://www.instagram.com')

time.sleep(2)

login = driver.find_elements_by_css_selector('a._b93kq')
login[0].click()

# 로그인 페이지 접속
uid = driver.find_element_by_name("username")
uid.send_keys('grrrit_official')
upw = driver.find_element_by_name("password")
upw.send_keys('')
time.sleep(2)

# 로그인 크릭
loginbutton = driver.find_element_by_css_selector('button._qv64e')
loginbutton.click()

time.sleep(3)

# 검색창 클릭
searchbar = driver.find_element_by_css_selector('div._eduze._mknn3')
searchbar.click()

rooting = 1

for instaid in instaids :

    # 검색창에 ID입력
    insert_follower = driver.find_element_by_css_selector("input._avvq0._o716c")
    insert_follower.send_keys(instaid[1])

    time.sleep(1)

    # 계정클릭
    follower_click = driver.find_elements_by_css_selector('div._etpgz a._gimca')
    follower_click[0].click()

    time.sleep(2)

    # 팔로우 클릭
    try :
        follow = driver.find_elements_by_css_selector('a._t98z6')
        follow[1].click()

        time.sleep(2)

    except :
        continue


    # 팔로워 리스트 만들기
    text = driver.find_element_by_css_selector('div._lfwfo._euzqy')
    print(text.text)

    # 첫 팔로우 리스트 저장
    ofs = driver.find_elements_by_class_name('_6e4x5')
    ofs_num = len(ofs)

    scr1 = driver.find_element_by_css_selector('div._gs38e')
    last_height = driver.execute_script("return document.body.scrollHeight", scr1)

    while True :

        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        time.sleep(2)


        nfs = driver.find_elements_by_class_name('_6e4x5')
        nfs_num = len(nfs)

        if (rooting % 60) == 0 :
            rooting = rooting + 1

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
            uid.send_keys('b')
            upw = driver2.find_element_by_name("password")
            upw.send_keys('')
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

                time.sleep(1)

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

                # 팔로워의 X버튼 누르기
                #exitbutton = driver.find_element_by_css_selector('button._dcj9f')
                #exitbutton.click()

            driver2.close()

        else :
            rooting = rooting + 1

        # 전 리스트와 스크롤 내린 리스트가 같으면 브레이크
        if nfs_num == ofs_num:

            #아이디 화면에 출력
            for f in nfs :
                a = f.find_element_by_css_selector('._2nunc a')
                print(a.text)

                db.save_followid ( a.text )

            print (nfs_num)
            break

        ofs_num = nfs_num


    # 팔로워의 X버튼 누르기
    exitbutton = driver.find_element_by_css_selector('button._dcj9f')
    exitbutton.click()

    time.sleep(3)
