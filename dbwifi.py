import os
import pymysql
import dbconfig
import datetime

class DbWifi():
    def connect(self, database="wifi"):
        return pymysql.connect(host='localhost',
        user=dbconfig.db_user,
        password=dbconfig.db_password,
        db=dbconfig.db_database)

    def get_user(self, user):
        pass