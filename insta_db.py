import pymysql
from datetime import date, timedelta


# 방문할 계정 선정하기
def search_list ( number ) :

    # DB 연결
    conn = pymysql.connect(host='localhost', user='root', password='qwe123',
                            db = 'instagram', charset = 'utf8' )
    curs = conn.cursor()

    # 오늘 검색할 아이디 불러와서 변수에 저장하기
    sql = """SELECT id, username, register_date FROM `userinfo` WHERE `register_date`
        LIKE '0000-00-00' LIMIT %s;"""
    curs.execute(sql, number)

    instaids = curs.fetchall()
    curs.close()

    return instaids


# 팔로워수 저장
def save_followernum (followernum, instaid ) :

    # DB 연결
    conn = pymysql.connect(host='localhost', user='root', password='qwe123',
                            db = 'instagram', charset = 'utf8' )
    curs = conn.cursor()

    update_followernum = """UPDATE `userinfo` SET `follower_num` = %s, `register_date` = %s  WHERE `userinfo`.`id` = %s;"""

    # 날짜 부르기
    td = date.today()

    # 팔로워 DB에 저장
    curs.execute(update_followernum, ( int(followernum), td,  instaid))
    conn.commit()

    conn.close()

def arrange_id() :

    # DB 연결
    conn = pymysql.connect(host='localhost', user='root', password='qwe123',
                            db = 'instagram', charset = 'utf8' )
    curs = conn.cursor()

    sql = """DELETE n1 FROM userinfo n1, userinfo n2 WHERE n1.id > n2.id AND n1.username = n2.username"""

    # 팔로워 DB에 저장
    curs.execute( sql )
    conn.commit()

    conn.close()


def save_followid ( instaid ) :
    # DB 연결
    conn = pymysql.connect(host='localhost', user='root', password='qwe123',
                            db = 'instagram', charset = 'utf8' )
    curs = conn.cursor()

    insert_follow = """INSERT INTO `userinfo` (`id`, `username`, `sex`, `follower_num`, `country`, `register_date`, `needless`)
                    VALUES (NULL, %s, 'n', '0', 'n', '0000-00-00', '0');"""

    # 팔로워 리스트 DB에 저장
    curs.execute(insert_follow, instaid )
    conn.commit()

    conn.close()
