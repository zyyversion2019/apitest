# author zyy
# time 2024/12/11 13:29
import logging

import allure
import jsonpath

from utils.request_utils import send_jdbc


@allure.step("http响应断言")
def http_assert(res_json,case):
    check = jsonpath.jsonpath(res_json, case["check"])[0]
    expect = case["expected"]
    assert expect == check

@allure.step("jdbc响应断言")
def jdbc_assert(case):
    check_sql = case["sql_check"]
    logging.info(check_sql)
    res=send_jdbc(check_sql)[0]
    expect = case["sql_expected"]
    assert expect == res