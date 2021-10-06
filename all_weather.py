from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event  # 这两个没用的别删
from nonebot.adapters.cqhttp.message import MessageSegment
import requests, json
from nonebot.permission import *
from nonebot.rule import to_me
import requests

weather = on_keyword({'全国降雨预报图','降雨图'})
@weather.handle()
async def weather_(bot: Bot, event: Event, state: T_State):
    await weather.send(Message("获取全国降水量预报图中"))
    id = str(event.get_user_id())
    url = "https://api.iyk0.com/jyu?type=img"
    resp = requests.get(url)
    with open("/home/bot/QQbot/src/data/weather.jpg", mode='wb') as f:
        f.write(resp.content)
    msg = f'[CQ:image,file=file:///home/bot/QQbot/src/data/weather.jpg]'
    await weather.send(Message(msg))