#Author:Jin
#-*-coding:utf-8-*-
import urllib.request
from lxml import etree
import json
import time

def loadweb(sku,url):
    ua_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
    request = urllib.request.Request(url, headers=ua_headers)
    response = urllib.request.urlopen(request).read().decode('utf-8')
    content=etree.HTML(response)
    s_info=content.xpath('//div[@id="merchant-info"]/a[1]/text()')
    num_info=content.xpath('//div[@class="a-box-inner a-padding-base"]/span/a/text()')
    sum={'ASIN':sku,'购物车名称':s_info,'卖家数':num_info,'时间':time.ctime()}
    with open('sum_info.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(sum, ensure_ascii=False) + '\n')


while True:
    sku_list=['B07BRSRS82','B07BRM3J7X']
    for sku in sku_list:
        url='http://www.amazon.de/dp/'+sku+'?ie=UTF8&th=1&psc=1'
        loadweb(sku,url)
        time.sleep(2)
    time.sleep(3500)