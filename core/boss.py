# -*- coding: UTF-8 -*-
__author__ = 'Joynice'

import requests
from utils.utils import get_header
import os
from lxml import etree
import queue

class Boss(object):
    '''
    Boss直聘
    '''

    def __init__(self, keyword, city, path='.\\'):
        self.keyword = keyword
        self.city = city
        self.path = path
        self.base_url = 'https://www.zhipin.com/job_detail/'
        self.jobqueue = queue.Queue()
        self.csv_header = ['职位名称', '公司名称', '工作地点', '薪资', '工作经验', '学历要求', '所属领域', '公司状态',
                           '公司规模', '发布人', '发布时间']

    def _get_city_code(self):
        url = 'https://www.zhipin.com/wapi/zpCommon/data/city.json'
        req = requests.get(url=url, headers=get_header()).json()
        if req['message'] == 'Success':
            city_code_dict = req.get('zpData').get('hotCityList')
            for i in city_code_dict:
                if i['name'] == self.city:
                    return i['code']
            return '100010000'  # 全国

    def Spider(self):
        params = {
            'query': self.keyword,
            'city': self._get_city_code()
        }
        req = requests.get(url=self.base_url, params=params, headers=get_header())
        html = etree.HTML(req.text)
        for i in range(1, 31):
            title = html.xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[1]/h3/a/div[1]'.format(i))
            name = html.xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[2]/div/h3/a/text()'.format(i))
            data1 = html.xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[1]/p/text()'.format(i))
            area = data1[0]
            salery = html.xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[1]/h3/a/span/text()'.format(i))
            exp = data1[1]
            study = data1[2]
            belong = html.xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[2]/div/p/text()[1]'.format(i))
            status = html.xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[2]/div/p/text()[2]'.format(i))
            size = html.xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[2]/div/p/text()[3]'.format(i))
            who = html.xpath('//*[@id="main"]/div/div[3]/ul/li[{}]/div/div[3]/h3/text()[1]'.format(i))
            job = html.xpath('//*[@id="main"]/div/div[3]/ul/li[1]/div/div[3]/h3/text()[2]'.format(i))
            time = html.xpath('//*[@id="main"]/div/div[3]/ul/li[1]/div/div[3]/p/text()')





if __name__ == '__main__':
    a = Boss(keyword='java', city='郑州').Spider()
