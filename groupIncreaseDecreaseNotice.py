# -*- coding = utf-8 -*-
# @Time : 2021/9/2 0:34
# @File : groupIncreaseDecreaseNotice.py
# @software : PyCharm

from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Message, GroupIncreaseNoticeEvent, GroupDecreaseNoticeEvent


notice = on_notice()

#进群事件
@notice.handle()
async def greeting(bot: Bot, event: GroupIncreaseNoticeEvent, state: T_State):
    if event.group_id == 780021611 or 733385409 or 279626548:
        userId = event.get_user_id()
        at_ = "[CQ:at,qq={}]".format(userId)
        msg = at_ + '欢迎新进群的小伙伴~\n请按照【年级 学院 名字 乐器】的格式来修改群备注哦\n\n社团QQ:3368419258' \
                    '\n编配组群:781482377\nB站:山青DS器乐社\nhttps://space.bilibili.com/1036307210\n\n' \
                    '\n回复 "社团简介" 获得更多信息\n\n' \
                    '【关于琴房】\n' \
                    '琴房在会文南楼A区一楼东侧\n' \
                    '琴房四:\n' \
                    '本学期面向器乐社开放时间\n' \
                    '周五-周日19:00-22:00\n' \
                    '内有电钢、古筝、架子鼓、钢片琴等乐器供体验，如果想要借用私人乐器前请告知管理员~\n' \
                    '琴房一:\n' \
                    '7*24开放\n' \
                    '内有凳子和少量谱架，进入练习无需申请，请勿搬动架子鼓'
        await notice.send(Message(msg))
