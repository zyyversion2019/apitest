# author zyy
# time 2024/12/10 17:33
import logging

import allure


@allure.step("初始化allure测试报告")
def allure_init(case):
    allure.dynamic.feature(case["feature"])
    allure.dynamic.story(case["story"])
    allure.dynamic.id(case["id"])
    allure.dynamic.title(case["title"])
    logging.info(str(case["id"])+case["feature"]+case["story"])