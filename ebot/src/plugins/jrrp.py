import random
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot,Event
from nonebot.adapters.onebot.v11.message import Message

def luck_simple(num):
    if num < 18:
        return '大吉'
    elif num < 53:
        return '吉'
    elif num < 58:
        return '半吉'
    elif num < 62:
        return '小吉'
    elif num < 65:
        return '末小吉'
    elif num < 71:
        return '末吉'
    else:
        return '凶'

jrrp = on_keyword(['jrrp','今日人品'],priority=50)
@jrrp.handle()
async def jrrp_handle(bot: Bot,event: Event):
    rnd = random.Random()
    rnd.seed(int(event.get_user_id()))
    luckn = rnd.randint(1,100)
    print(event.get_user_id())
    await jrrp.finish(Message(f'[CQ:at,qq={event.get_user_id()}]您今日的幸运指数是{luckn}/100（越低越好），为"{luck_simple(luckn)}"'))