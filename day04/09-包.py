"""
import
from ... import ...

# 方式一
import 包名.模块名
包名.模块名.工具名

# 方式二
from 包名 import 模块名
模块名.工具名

# 方式三       --- 最最常用的
from 包名.模块名 import 工具名
工具名

"""

from hm_message.send_message import send

send()

# as 起别名
import hm_message.receive_message as rm
rm.receive()

# 可以导入多个
from hm_message import receive_message,send_message
