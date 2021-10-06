# -*- coding = utf-8 -*-
# @Time : 2021/9/2 15:20
# @File : command.py
# @software : PyCharm

from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, MessageEvent, Message
import requests
import json

"""社团简介"""
introduction = on_command("社团简介", priority=5)


@introduction.handle()
async def introduction_(bot: Bot, event: MessageEvent, state: dict):
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
                "\n社团指导老师：艺术学院袁伟副教授\n" \
                "本学期开设课程：”懂一点音乐，会一点钢琴“(艺术) 2学分\n" \
                "上课地点：周六下午2-4点，振声苑W201\n" \
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
        await bot.send(message=msg, event=event)
    else:
        pass


"""网易云评论"""
comment = on_command("网易云", priority=5)
@comment.handle()
async def comment_1(bot: Bot, event: MessageEvent, state: dict):
    await comment.send("正在获取评论中")
    url = "https://v1.hitokoto.cn?c=j"
    resp = requests.get(url)
    x = json.loads(resp.text)
    msg = x["hitokoto"]
    await bot.send(message=msg, event=event)


map_ = on_command("地图", priority=5)
@map_.handle()
async def help_(bot: Bot, event: MessageEvent, state: dict):
    msg = f'[CQ:image,file=file:///home/bot/QQbot/src/data/map.jpg]'
    await map_.send(Message(msg))


weather = on_command("降雨图", priority=5)
@weather.handle()
async def weather_(bot: Bot, event: MessageEvent, state: dict):
    await weather.send("获取全国降水量预报图中")
    url = "https://api.iyk0.com/jyu?type=img"
    resp = requests.get(url)
    with open("weather.jpg", mode='wb') as f:
        f.write(resp.content)
    msg = f'[CQ:image,file=file:///home/bot/QQbot/src/data/weather.jpg]'
    await weather.send(Message(msg))
    
    
piano_room = on_command("琴房", priority=4)
@piano_room.handle()
async def piano_room_(bot: Bot, event: MessageEvent, state: dict):
    msg =   '【关于琴房】\n' \
            '琴房在会文南楼A区一楼东侧\n' \
            '琴房四:\n' \
            '本学期面向器乐社开放时间\n' \
            '周五-周日19:00-22:00\n' \
            '内有电钢、古筝、架子鼓、钢片琴等乐器供体验，如果想要借用私人乐器前请告知管理员~\n' \
            '琴房一:\n' \
            '7*24开放\n' \
            '内有凳子和少量谱架，进入练习无需申请，请勿搬动架子鼓'
    await piano_room.finish(msg)
    