from pymysql import connect
from Django_items.xicidaili_Django.xici.models.py import DaiLi

class Show_View():
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '123456'
        self.dbname = 'xicidaili'
        self.table = 'xici'
        self.port = 3306
        self.db = connect(host=self.host, user=self.user, password=self.password, db=self.dbname, port=self.port)
        self.cursor = self.db.cursor()

    def high_data(self):
        highs = []

        sql = 'select * from {} where isanonymous="高匿"'.format(self.table)
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        # print(highs)
        for item in items:
            highs.append(item[1:])

        return highs

    def lucency_data(self):
        lucency_list = []
        sql = 'select * from {} where isanonymous="透明"'.format(self.table)
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        # print(highs)
        for item in items:
            lucency_list.append(item[1:])

        return lucency_list

    def https_data(self):
        https_list = []
        sql = 'select * from {} where type="https"'.format(self.table)
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        for item in items:
            https_list.append(item[1:])

        return https_list

    def http_data(self):
        http_list = []
        sql = 'select * from {} where type="http"'.format(self.table)
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        for item in items:
            http_list.append(item[1:])

        return http_list

    def socket_data(self):
        socket_list = []
        sql = 'select * from {} where type="socks4/5"'.format(self.table)
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        for item in items:
            socket_list.append(item[1:])

        return socket_list

    def all_data(self):

        datas = []
        sql = 'select * from {}'.format(self.table)
        self.cursor.execute(sql)
        items = self.cursor.fetchall()
        for item in items:
            datas.append(item[1:])

        return datas


def insert_data():
    data = Show_View()
    items = data.all_data()


    for item in items:
        mode = DaiLi()
        mode.country = item[0]
        mode.ipaddress = item[1]
        mode.port = item[2]
        mode.serveraddr = item[3]
        mode.isanonymous = item[4]
        mode.type = item[5]
        mode.alivetime = item[6]
        mode.verifitiontime = item[7]
        mode.save()


insert_data()
