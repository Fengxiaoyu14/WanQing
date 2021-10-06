# -*- codeing = utf-8 -*-
# @Time : 2021/9/11 1:27
# @File : hitokoto.py
# @Software : PyCharm

from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, MessageEvent, Event
import requests
import json
import random

yiyan = on_command("一言", priority=5)
@yiyan.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()
    if args:
        types = {
            "动画": "a",
            "漫画": "b",
            "游戏": "c",
            "文学": "d",
            "原创": "e",
            "网络": "f",
            "其他": "g",
            "影视": "h",
            "诗词": "i",
            "网易云": "j",
            "哲学": "k",
            "抖机灵": "l"
        }
        choice = types[args]
    else:
        type = [
            "a", #动画
            "b", #漫画
            "c", #游戏
            "d", #文学
            "e", #原创
            "f", #来自网络
            "g", #其他
            "h", #影视
            "i", #诗词
            "j", #网易云
            "k", #哲学
            "l", #抖机灵
            #其他 作为 动画 类型处理
        ]
        choice = random.choice(type)

    msg = await get_yiyan(choice)
    await yiyan.finish(msg)


async def get_yiyan(type_: str):
    url = "https://v1.hitokoto.cn"
    full_url = url + f"?c={type_}"
    resp = requests.get(full_url)
    msg = json.loads(resp.text)["hitokoto"]
    return msg