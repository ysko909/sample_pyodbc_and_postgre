import pyodbc


def login(server, db, uid, pw):
    s = 'DRIVER={PostgreSQL};SERVER=' + server\
        + ';DATABASE=' + db\
        + ';UID=' + uid\
        + ';PWD=' + pw

    return pyodbc.connect(s)


def sql_execute(cnn, sql):
    cursor = cnn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()

    return rows


cnn = login('localhost', 'test_db', 'test', 'test')

sql = '''select * from users'''

res = sql_execute(cnn, sql)

if res != []:
    for l in res:
        print(l)
