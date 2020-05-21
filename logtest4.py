#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger(__name__)
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# logger.setLevel(level=logging.INFO)  # 日志总级别，handler是在此级别基础上再获取日志，一般这里设置成DEBUG,默认值是WARING

# 日志输出到控制台
stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
format_stream = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(format_stream)
logger.addHandler(stream_handler)

# 同时日志输入到文件
file_handler = logging.FileHandler(filename='logtest4.log', mode='a', encoding=None)  # mode:w表示设置为重写模式，默认为a追加模式
file_handler.setLevel(level=logging.DEBUG)
format_file = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s- %(filename)s- %(lineno)d- %(message)s')
file_handler.setFormatter(format_file)
file_handler.mode
logger.addHandler(file_handler)



# Log
logger.info('This is a log info')
logger.warning(u'警告1')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.critical('critical exists')
logger.info('Finish')




'''
reload(sys)
sys.setdefaultencoding('utf8')
# Test_api006-009，服务器返回的都是json格式的数据
@ddt.ddt
class Test_api006(object):

    # set_trace()
    # p1 = sys.getdefaultencoding()
    # print p1
    # reload(sys)
    # sys.setdefaultencoding('utf8')
    # p2 = sys.getdefaultencoding()
    # print p2
    logger.info(u'Test_api006接口开始测试...')
 
    set_trace()
    logger.info(u'Test_api006接口开始测试...')  
    问题：如果在logger.info中包含中文，前面有set_trace()，在win10的cmd中运行代码，会提示Failure：IOError([Erroe 0] Error)...ERROR
        导致代码运行失败
    解决方法：
    方法1：代码运行前执行下面2行，将运行环境设置为utr-8
    reload(sys)
    sys.setdefaultencoding('utf8')
    方法2：不要在logger.info中包含中文前加set_trace()
    方法3：logger.info中不要写中文
'''