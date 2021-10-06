# -*- codeing = utf-8 -*-
# @Time : 2021/9/15 18:30
# @File : SDUNoticeClawer.py
# @Software : PyCharm

import nonebot
import requests
from nonebot_plugin_apscheduler import scheduler
from lxml import etree
import re
import datetime
import time


@scheduler.scheduled_job('cron', second='*/20')
async def notice_():
    group_id = "780021611"
    bot = nonebot.get_bot("1431721752")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    baseUrl = 'https://www.bkjx.sdu.edu.cn/'
    resp = requests.get(baseUrl, headers=headers)
    resp.encoding='utf-8'
    html = etree.HTML(resp.text)

    # 工作通知
    work_notice_url = baseUrl + html.xpath('/html/body/div[3]/div[4]/div[1]/div[1]/a/@href')[0]
    # 教学快讯
    teaching_notice_url = baseUrl + html.xpath('/html/body/div[3]/div[4]/div[2]/div[1]/a/@href')[0]

    work_resp = requests.get(work_notice_url, headers=headers)
    work_resp.encoding='utf-8'
    work_obj = re.compile(r'<div class="bjClass2"></div>.*?<a href="(?P<href>.*?)".*?'
                          r'title="(?P<title>.*?)".*?style="(?P<style>.*?)".*?\[(?P<time>.*?)\]', re.S)
    
    teaching_resp = requests.get(teaching_notice_url)
    teaching_resp.encoding = 'gbk2312'
    teaching_obj = re.compile(r'<div class="bjClass2"></div>.*?<a href="(?P<href>.*?)".*?'
                              r'title="(?P<title>.*?)".*?.*?\[(?P<time>.*?)\]', re.S)

    # 获取当前系统时间
    curr_time = datetime.datetime.now()
    date = str(curr_time.date())

    work_result = work_obj.finditer(work_resp.text)
    work_items = []
    work_item = []
    for it in work_result:
        if date == it.group("time"):
            work_item.append(it.group("title"))
            work_item.append(it.group("style"))
            work_item.append(it.group("time"))
            work_item.append(it.group("href"))
            work_items.append(work_item)
        work_item = []
    

    teaching_result = teaching_obj.finditer(teaching_resp.text)
    teaching_items = []
    teaching_item = []
    for it in teaching_result:
        if date == it.group("time"):
            teaching_item.append(it.group("title"))
            teaching_item.append(it.group("time"))
            teaching_item.append(it.group("href"))
            teaching_items.append(teaching_item)

    work_path = r'./clawerData' + '/work_notice' + date + '.txt'
    teaching_path = r'./clawerData' + '/teaching_notice' + date + '.txt'

    work_updates = compare(work_path, work_items)
    teaching_updates = compare(teaching_path, teaching_items)

    # 更新的内容
    # print(work_updates)
    # print(teaching_updates)

    work_msg = ''
    for i in range(len(work_updates)):
        work_msg += work_updates[i][0]  # title
        work_msg += '\n日期:' + work_updates[i][2]  # date
        work_msg += '\n\n'

    teaching_msg = ''
    for i in range(len(teaching_updates)):
        teaching_msg += teaching_updates[i][0]  # title
        teaching_msg += '\n日期:' + teaching_updates[i][1]  # date
        teaching_msg += '\n\n'

    if work_msg or teaching_msg:
        msg = '【本科生院通知更新】\n'
        if work_msg:
            msg += '工作通知:\n' + work_msg
        if teaching_msg:
            msg += '教学快讯:\n' + teaching_msg
        local_time = time.localtime(time.time())
        msg += "更新时间:" + str(local_time.tm_hour).rjust(2,'0') + ':' + str(local_time.tm_min).rjust(2,'0') + ':' + str(local_time.tm_sec).rjust(2,'0')

        return await bot.call_api(
            'send_group_msg',
            **{
                'message': msg,
                'group_id': group_id
            })

def compare(path, items):
    # 将爬到的title与文档中的title进行比对
    updates = []
    try:
        with open(path, mode="r", encoding='utf-8') as fo:
            file_content = fo.read()
            flag = 1
            for index in range(len(items)):
                for title_in_data in file_content.split('\n'):
                    if str(items[index][0]) == str(title_in_data):
                        # 文档中有此title
                        flag = 0
                        break
                if flag == 1:
                    updates.append(items[index])
                else:
                    flag = 1
    except FileNotFoundError:
        # 如果还未创建数据文件，则items内的内容全部为updates
        updates = items

    # 写文件
    try:
        with open(path, mode="a", encoding='utf-8') as fw:
            for i in range(len(updates)):
                fw.write(updates[i][0])
                fw.write('\n')
                i += 1
    except Exception as e:
        print(e)

    return updates
