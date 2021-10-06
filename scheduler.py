# -*- coding = utf-8 -*-
# @Time : 2021/9/4 1:39
# @File : scheduler.py
# @software : PyCharm

import nonebot
import requests
import json
from nonebot_plugin_apscheduler import scheduler
import urllib


@scheduler.scheduled_job('cron', hour='7', minute='0')
async def good_morning_():
    group_id = "279626548"
    bot = nonebot.get_bot("1431721752")

    cityname = "即墨"

    morning = "[CQ:face,id=74]早上好，新的一天又开始了~\n" \
              "今日【" + cityname + "】天气:\n"
    msg = ""

    try:
        url = 'http://apis.juhe.cn/simpleWeather/query?city=%s&key=a8b3dd5052f0e3e2dff14175165500d6' % urllib.parse.quote(
            cityname)
        data = requests.get(url=url, timeout=5).json()
        # time_today = "时间：" + data['result']['future'][0]['date']
        temperater_today = "温度:" + data['result']['future'][0]['temperature']
        weather_today = "天气：" + data['result']['future'][0]['weather']
        direction_today = "风向：" + data['result']['future'][0]['direct']
        msg = temperater_today + '\n' + weather_today + '\n' + direction_today + '\n\n'

        #每日哲学一句
        url_yiyan = "https://v1.hitokoto.cn?c=k"
        data_yiyan = requests.get(url_yiyan, data=data).json()
        yiyan = data_yiyan["hitokoto"] + "  \n" + "——" + data_yiyan["from"]


        return await bot.call_api(
            'send_group_msg',
            **{
                'message': morning + msg + yiyan,
                'group_id': group_id
            })

    except Exception as e:
        return await bot.call_api(
            'send_group_msg',
            **{
                'message': morning + "无法获得天气信息:" + str(e),
                'group_id': group_id
            }
        )