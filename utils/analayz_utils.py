# author zyy
# time 2024/12/10 17:25
import logging

import allure
from jinja2 import Template

from config.base_config import BASE_URL

@allure.step("解析用例")
def get_req_data(case):
    method = case["method"]
    url = BASE_URL + case["url"]
    params = eval(case["params"]) if isinstance(case["params"], str) else None
    data = eval(case["data"]) if isinstance(case["data"], str) else None
    files = eval(case["files"]) if isinstance(case["files"], str) else None
    headers = eval(case["headers"]) if isinstance(case["headers"], str) else None
    req_data = {
        "method": method,
        "url": url,
        "params": params,
        "data": data,
        "files": files,
        "headers": headers
    }
    return req_data

