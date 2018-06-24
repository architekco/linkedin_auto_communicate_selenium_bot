import os

import pymysql

insert_contacts_query = "INSERT INTO messenger_inbox (`company`, `industry`, `location`,\
 `title`, `linkedin_id`, `name`, `latest_activity`,`status`, `is_connected`, `connected_date`,\
  `owner_id`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"


def add_to_db(cur, getcontacts_query, *values):
    # may check record exists
    sql = getcontacts_query % values 
    print('sql:', sql)
    # print('add to db:', insert_contacts_query, values)
    try:        
        cur.execute(sql)
    except Exception as err:
        print('Insert inbox error:', err)


def add_to_db2(cur, getcontacts_query, *values):
    # may check record exists
    sql = getcontacts_query % values 
    print('sql:', sql)
    # print('add to db:', insert_contacts_query, values)
    try:
        cur.execute(getcontacts_query, values)
    except Exception as err:
        print('Insert inbox error:', err)


def get_cursor():
    db_user = os.environ.get('dbuser', 'jetbuzz')
    db_pw = os.environ.get('dbpw', 'tech123$')
    db_host = os.environ.get('dbhost', "localhost")
    # db_user = os.environ.get('dbuser', 'root')
    # db_pw = os.environ.get('dbpw', '')
    # db_host = os.environ.get('dbhost', "localhost")
    # previous_rows_count = 0

    try:
        connect = pymysql.connect(
            host=db_host, user=db_user, password=db_pw, db="sq_jetbuzz_db", autocommit=True)
    except Exception as err:
        print("Could not open database:", err)
        exit(-1)
    cur = connect.cursor() 
    #connect.set_character_set('utf8')
    # cur.execute('SET NAMES utf8;')
    # cur.execute('SET CHARACTER SET utf8;')
    # cur.execute('SET character_set_connection=utf8;')
        
    
    
    return cur
