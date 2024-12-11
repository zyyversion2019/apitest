# author zyy
# time 2024/12/10 15:03
import logging

import pytest

from utils.request_utils import send_jdbc_del


@pytest.fixture(scope="session",autouse=True)
def destroy_f():
    logging.info("初始化完成")
    yield
    logging.info("销毁测试数据")
    sql="delete from sp_manager where mg_name='zyy'"
    send_jdbc_del(sql)
