# author zyy
# time 2024/12/10 18:53
import allure
import pymysql
import requests

from config.base_config import *


@allure.step("发送http请求并返回响应数据")
def send_http(data):
    response=requests.request(**data)
    return response

@allure.step("发送JDBC请求并返回响应数据")
def send_jdbc(sql):

    conn=pymysql.Connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
        charset=DB_CHARSET
    )
    cur=conn.cursor()
    cur.execute(sql)
    res=cur.fetchone()
    cur.close()
    conn.close()
    return res

def send_jdbc_del(sql):

    conn=pymysql.Connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
        charset=DB_CHARSET
    )
    cur=conn.cursor()
    cur.execute(sql)
    res=cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return res