import logging
import json
import uuid
from urllib.parse import urlencode
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
                    
logging.debug('debug 信息')
# logging.info('info 信息')
# logging.warning('warning 信息')
# logging.error('error 信息')
# logging.critical('critial 信息')


a_dict ='{{"tid":112}}'
f ={}
print(a_dict.format(**f))

print(a_dict)

b_dict ={"tid":112}

print(json.dumps(b_dict))


print(json.dumps({'4': 5, '6': 7}, separators=(',', ':')))


# query = '{"noZip":true,"highSearch":[{"type":"Select","queryName":"ORDER_STATUS","value":"1"},{"type":"Input","queryName":"SOURCE_CODE","value":"202101120209532295"}]}'

# print(urlencode(query))


print(uuid.uuid1())
print(uuid.uuid4())
