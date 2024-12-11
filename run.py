# author zyy
# time 2024/12/10 15:03
import logging
import os

import pytest

if __name__=="__main__":
    pytest.main(["-vs", "./testcases/test_runner.py", "--alluredir", "./report/json_report", "--clean-alluredir"])
    os.system("allure generate ./report/json_report -o ./report/html_report --clean")