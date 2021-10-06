# -*- codeing = utf-8 -*-
# @Time : 2021/9/10 0:34
# @File : weather.py
# @Software : PyCharm

import urllib.request
from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
import urllib, requests
from urllib import parse


weather = on_command("天气", priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询神马城市的天气ovo")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.finish(city_weather)


async def get_weather(city: str):
    cityname = city
    url = 'http://apis.juhe.cn/simpleWeather/query?city=%s&key=a8b3dd5052f0e3e2dff14175165500d6' % urllib.parse.quote(
        cityname)
    data = requests.get(url=url, timeout=5).json()
    try:
        if data["reason"] == "查询成功!" or "查询成功":
            time_today = "时间：" + data['result']['future'][0]['date']
            temperater_today = "温度:" + data['result']['future'][0]['temperature']
            weather_today = "天气：" + data['result']['future'][0]['weather']
            direction_today = "风向：" + data['result']['future'][0]['direct']

            time_tomorrow = "时间：" + data['result']['future'][1]['date']
            temperater_tomorrow = "温度:" + data['result']['future'][1]['temperature']
            weather_tomorrow = "天气：" + data['result']['future'][1]['weather']
            direction_tomorrow = "风向：" + data['result']['future'][1]['direct']
            return str(cityname + '\n' + time_today + '\n' + temperater_today + '\n' + weather_today + '\n' + direction_today
                       + '\n\n\n' + time_tomorrow + '\n' + temperater_tomorrow + '\n' + weather_tomorrow + '\n' + direction_tomorrow)
        elif data["reason"] == "暂不支持该城市":
            return str("不知道你说的是哪里鸭QAQ")
        else:
            print(data)
            return str("暂时无法查询")
    except:
        return str("不支持查询该城市或其他错误")