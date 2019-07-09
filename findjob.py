# -*- coding: UTF-8 -*-
__author__ = 'Joynice'

import datetime
import os
from core.QCWY import QCWY
from core.boss import Boss
from core.zhilian import ZhiLian
from multiprocessing import Process

if __name__ == '__main__':
    downloadpath = os.path.join(os.getcwd(), 'save-data')
    if os.path.exists(downloadpath):
        city = input('请输入城市名：')
        keyword = input('请输入搜索关键词：')
        if keyword != None and city!=None:
            print('''
            请选择获取的网站如下：
            1. 前程无忧
            2. Boss直聘 
            3. 智联招聘
            4. 全部
            输入选项前方数字，进行选择！！！
            ''')
            web = input('请输入选项(数字)：')
            if web == '1':
                QCWY(city=city, keyword=keyword).run()
            elif web == '2':
                Boss(city=city, keyword=keyword).run()
            elif web == '3':
                ZhiLian(city=city, keyword=keyword).run()
            elif web == '4':
                qcwy = Process(target=QCWY(city=city, keyword=keyword).run)
                zhilian = Process(target=ZhiLian(city=city, keyword=keyword).run)
                boss = Process(target=Boss(city=city, keyword=keyword).run)
                qcwy.start()
                # zhilian.start()
                # boss.start()
