
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot,Event
from nonebot.adapters.onebot.v11.message import Message

text = '命令菜单          功能        \n\
        help 或 帮助      显示命令菜单 \n\
        jjrp 或 今日人品  表面意思     \
'


helps = on_keyword(['help','帮助'],priority=49)
@helps.handle()

async def helps_handle(bot: Bot, event: Event):
    await helps.finish(Message(text))
