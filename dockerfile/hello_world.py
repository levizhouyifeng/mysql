# -*- coding: UTF-8 -*-
import random
import time


i = 0
list1 = ['毛致富', '毛二蛋']
a, b = list1
while i <= 10:
    pre = random.choice(list1)
    end = a if pre == b else b
    print('{}就是{}'.format(pre, end))
    i += 1
    time.sleep(20)


# import pymysql

# class TestDb:
#     def run(self):
#         conn = pymysql.connect(host='mysql', port=3306, database='db', user='root', password='password')
#         print(conn)

# if __name__ == "__main__":
#     TestDb().run()