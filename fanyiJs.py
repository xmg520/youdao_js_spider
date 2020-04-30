#!/usr/bin/env python
#-*-coding:utf-8-*- 
__author__ = 'Mzx'
"""
项目实现，通过JS解密实现对有道翻译的反爬虫操作

关键js：
 var r = function(e) {
        var t = n.md5(navigator.appVersion)
          , r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10);
        return {
            ts: r,
            bv: t,
            salt: i,
            sign: n.md5("fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj")
        }
    };

知识点：
chrome开发者工具调试操作
hashlib加密操作
"""

# 所需模块
import json
import math
import time
import hashlib
import random
import requests


# 翻译文本,这里用 “”“” 支持长文本翻译
fanyi_name = """ 帅哥 """.strip()

# 可变参数编译
ts = int(time.time() * 1000)
# MD5使用hashlib 固定加密写法 hashlib.md5(("加密内容").encode('utf-8')).hexdigest()
bv = hashlib.md5(("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36").encode("utf-8")).hexdigest()
salt = str(ts) + str(int(random.random()*10))
sign_origin = "fanyideskweb" + fanyi_name + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
sign = hashlib.md5((sign_origin).encode("utf-8")).hexdigest()


# 请求数据
data = {
    'i': fanyi_name,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': ts,
    'bv': bv,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}

# 接口地址
post_url = "http://fanyi.youdao.com/translate_o"

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Referer': 'http://fanyi.youdao.com/',
    "Cookie":"NTES_SESS=aicZo3tvJTD_jFRCW4QvC8bbDCW3W3aQM9Jes2H3KK8Y490e4zw3CZBxznQzS9RbDFA7vo3QZnaBGtI2vicJGmtaMdzEYzWPy3fSVsTXv24Sy6DoC94zuxGUTXphXINq0329Jo78wmfxVtEcVOubxoWE8JGWrgdPJTp8XMEgK5rofjBxstkOUcLcXP6Qpi44AhIZkrclPQ564bjt3M5yz3S8g; ANTICSRF=9cd36a130117688b76eec98667b81e42; S_INFO=1533824632|0|3&80##|julywhj; P_INFO=julywhj@163.com|1533824632|0|other|11&12|bej&1533811267&other#bej&null#10#0#0|182068&0||julywhj@163.com; OUTFOX_SEARCH_USER_ID=-622851639@10.168.8.76; JSESSIONID=aaaeegEGe2AL2hCez7Nuw; OUTFOX_SEARCH_USER_ID_NCOO=288396918.7876193; ___rl__test__cookies=1533977025972"
}

# 服务器返回信息
response = requests.post(url=post_url,headers=headers,data=data).text

# 打印服务器返回信息
print("服务器返回内容：" + response)

# 打印获取翻译数据,通过json loads 把str类型转为json类型，再提取数据
print("翻译内容："+fanyi_name)
print("翻译结果：" + json.loads(response)['translateResult'][0][0]['tgt'])