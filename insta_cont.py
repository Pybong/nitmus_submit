from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 팔로워수 저장
def change_followernum (followernum) :

    # 팔로워 숫자 저장
    if "천" in followernum :
        followernum = float(followernum[:-1]) * 1000

    elif "백만" in followernum :
        followernum = float(followernum[:-2]) * 1000000

    elif "," in followernum :
        followernum = followernum.replace(",", "")


    return followernum
