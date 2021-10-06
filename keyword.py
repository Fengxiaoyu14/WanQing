# -*- coding = utf-8 -*-
# @Time : 2021/9/2 16:54
# @File : keyword.py
# @software : PyCharm

from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Bot, Event, GroupMessageEvent
from nonebot.adapters.cqhttp.message import MessageSegment
from nonebot.permission import *
from nonebot.rule import to_me


"""社团简介"""
introduction = on_keyword({"社团简介","introduction"})
@introduction.handle()
async def introduction_(bot: Bot, event: GroupMessageEvent, state: T_State):
    #这里的group_id表示只在这些群生效
    if event.group_id == 780021611 or 733385409 or 279626548:
        msg =   "[CQ:face,id=74]山东大学（青岛）Dream-seeker器乐社，简称山青DS器乐社。山东大学DS器乐团最初于2014年在软件园校区成立，青岛校区器乐社于2016年注册成立。现以山东大学（青岛）一多书院作为指导单位，由山东大学艺术学院袁伟副教授担任指导老师，是山东大学青岛校区五星级社团。现有正式成员近二百人，从演奏各类乐器，到熟悉乐理及编曲，成员各有所长。\n" \
                "社团内现有大小各类乐器及演奏人员，包括：\n" \
                "键盘乐器：钢琴、手风琴、midi键盘\n" \
                "打击乐器：架子鼓、钢片琴、中国大鼓、沙锤、音树、锣等\n" \
                "弓弦乐器：小提琴、大提琴、二胡\n" \
                "拨弦乐器：原声吉他、电吉他、琵琶、中阮、古筝\n" \
                "吹管乐器：萨克斯、单簧管、长笛、竖笛、葫芦丝、小号，唢呐，竹笛，箫等\n" \
                "除此之外，还有编配组打工人员数名\n" \
                "假期线上音乐会及编配组课程是山青DS的品牌活动。\n" \
                "在星光达人秀、各学院晚会等学校举办的各种文艺活动中都会有器乐社原创编曲的作品演出。\n" \
                "\n" \
                "社团QQ:3368419258\n" \
                "编配组群:781482377\n" \
                "B站:山青DS器乐社 https://space.bilibili.com/1036307210\n" \
                "人民号: https://wap.peopleapp.com/rmh/396185\n" \
                "齐鲁壹点号: https://m.ql1d.com/new/ydIndex/13126\n" \
                "\n" \
                "友情链接:\n" \
                "山大DreamSeeker器乐团(济南)\n" \
                "B站: https://space.bilibili.com/1434239202\n" \
                "QQ群: 942699803\n"
        await introduction.send(Message(msg))
    else:
        pass
    
    
    
import requests    
import json
comment = on_keyword({'网易云评论', '网易云', '网抑云'})
@comment.handle()
async def comment_1(bot: Bot, event: Event, state: T_State):
    await comment.send("正在获取评论中")
    
    url = "https://api.iyk0.com/wyy"
    resp = requests.get(url)
    x = json.loads(resp.text)
    song = x['data']['song']
    # url_1 = x['data']['url']
    content = x['data']['content']
    msg = str('歌曲名：' + song + '\n'  + '评论：' + content)
    await comment.send(msg)
    
    
map = on_keyword({'地图', '校区地图'})
@map.handle()
async def map_(bot: Bot, event: Event, state: T_State):
    msg = f'[CQ:image,file=file:///home/bot/QQbot/src/data/map.jpg]'
    await map.send(Message(msg))
    
    
# wj = on_keyword('[CQ:face,id=178][CQ:face,id=67]')
# @wj.handle()
# async def wj_(bot: Bot, event: Event, state: T_State):
#     msg = '[CQ:face,id=178][CQ:face,id=67]'
#     await wj.send(Message(msg))