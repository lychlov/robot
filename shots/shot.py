# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     shot
   Description :
   Author :       Lychlov
   date：          2018/12/6
-------------------------------------------------
   Change Activity:
                   2018/12/6:
-------------------------------------------------
"""
import json

from bot.commando_query import call_fx_api
from bot.alarm_query import old_alarm_query,parse_101,fuzzy_query
result='[{"property9":null,"disp_tag":"等待派单","device_room":"100013669039867:南阳市郊区水产市场机房","event_id":"010-103-00-801066","last_time":"2018-12-12 11:07:04","property11":"63695","record_id":8623280519,"disp_id":null,"object_type":"ENODEB","title":"TROUBLESHOOTING DATA RECEIVED","device_name":"郊区水产市场-NLH","disp_status":null,"device_county":"宛城区","key_value":"NOKIA-CMHA-ZZ,SubNetwork=Nokia-102165,ManagedElement=MRBTS-63695||NYJQSHUICHANSHICHANG-NLH","device_province":"河南省","device_site":"100013669039865:南阳市郊区水产市场","device_vendor":"诺基亚","project_status":"工程状态","object_id":"100013693309091","vendor_event_id":"71106","device_specialty":"LTE无线网","severity":"二级告警","object_alias":"NYJQSHUICHANSHICHANG-NLH","vendor_event_seve":"3","device_city":"南阳市","object_name":"郊区水产市场-NLH","descr":"对象类名:ManagedElement,告警时间:2018-12-12 11:07:04,系统识别名:NOKIA-CMHA-ZZ,SubNetwork=Nokia-102165,ManagementNode=OMC-102165,IRPAgent=NBI-1,可能原因:0,告警级别:4,厂商特有告警类型:71106||TROUBLESHOOTING DATA RECEIVED,对象实例标识符:NOKIA-CMHA-ZZ,SubNetwork=Nokia-102165,ManagedElement=MRBTS-63695||NYJQSHUICHANSHICHANG-NLH,通知号:71770,详细原因:71106||TROUBLESHOOTING DATA RECEIVED,告警号:71106附加信息:||Complete TSUPL_eNB_63695_10105.20181212110544.tar||||TROUBLESHOOTING DATA RECEIVED||||PLMN-PLMN/MRBTS-63695,,,,,,,,"}]'
json_re = json.loads(result)
# print(call_fx_api('chengzhikun', '301'))
print(fuzzy_query('206-袁店'))
