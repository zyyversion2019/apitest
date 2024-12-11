# author zyy
# time 2024/12/10 15:06
import logging

import allure
import jsonpath
import pytest
import requests

from jinja2 import Template

from utils.allure_init import allure_init
from utils.analayz_utils import get_req_data
from utils.assert_utils import http_assert, jdbc_assert
from utils.excel_utils import read_excel

{"file":
     ("123up.jpg",
      open("./data/123.jpg","rb"),
      "jpg")
}


class TestRunner:
    # 测试数据
    data1=read_excel("./data/mydata.xlsx")
    all={}
    @pytest.mark.parametrize("case",data1)
    def test_zyy(self,case):
        all=self.all
        case=eval(Template(str(case)).render(all))
        allure_init(case)
        req_data = get_req_data(case)
        #请求
        logging.info(req_data)
        response= requests.request(**req_data)
        # json提取
        res_json=response.json()
        logging.info(f"返回的json是{res_json}",)

        if case["jsonExData"]:
            with allure.step("json提取"):
                for k,v in eval(case["jsonExData"]).items():
                    value=jsonpath.jsonpath(res_json, v)[0]
                    all[k]=value
        if case["sqlExData"]:
            with allure.step("sql提取"):
                for k,v in eval(case["sqlExData"]).items():
                    value=jsonpath.jsonpath(res_json, v)[0]
                    all[k]=value
        #http断言
        if case["expected"]:
            http_assert(res_json,case)
        # jdbc断言
        if case["sql_expected"]:
            jdbc_assert(case)




