from enum import Enum, unique
from typing import Any, Dict

from datetime import datetime, timedelta, timezone
 
print(datetime.now().strftime('%Y%m%d%H%M%S%f'))
print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

class TimeZoneChina:
    SHA_TZ = timezone(
        timedelta(hours=8),
        name='Asia/Shanghai',
    )
    @classmethod
    def now(cls):
        '''
        北京时间
        '''
        return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(cls.SHA_TZ)
    @classmethod
    def now_str(cls):
        return cls.now().strftime('%Y-%m-%dT%H:%M:%SZ')


print(TimeZoneChina.now().strftime('%Y%m%d%H%M%S%f'))

#@unique装饰器可以帮助我们检查保证没有重复值
@unique
class ExcelColumnEnum(Enum):
    CASE_NO = '用例编号'
    IS_EXECUTE = '是否执行'
    CASE_TITLE = '用例标题'
    CASE_DESC = '用例描述'
    REQ_HOST = '请求主机'

    REQ_METHOD = '请求方式'
    REQ_PATH = '请求路径'
    REQ_HEADER = '请求头'
    REQ_PARAM = '请求体'
    RESP_DATA = '响应数据'

    RESP_SHARE_PARAM = '响应共享参数'
    RESP_SUCCESS = '响应成功'
    RETRY_COUNT = '重试次数'
    RETRY_INTERVAL_SECOND = '重试时间'


class ExcelColumnDto():
    def __init__(self):
        for name,_ in ExcelColumnEnum.__members__.items():
            setattr(self, name.lower(), None)

    def new(self, kwargs: Dict[ExcelColumnEnum, Any]): 
        for k, v in kwargs.items():
            setattr(self, k.name.lower(), v)
        return self

if __name__ =='__main__':
    print([i.value for i in ExcelColumnEnum if i !=
           ExcelColumnEnum.RETRY_COUNT and i != ExcelColumnEnum.RETRY_INTERVAL_SECOND])

    a = {
        ExcelColumnEnum.CASE_NO: 123
    }
    b = ExcelColumnDto().new(a)
    print(b.case_no)
    print(b.__dict__)
