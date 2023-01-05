from nonebot.plugin import on_message
from nonebot.adapters.onebot.v11 import Bot,Event
from nonebot.adapters.onebot.v11 import Message
import requests
from nonebot.rule import to_me

def AI(ms):
    js = requests.get("http://api.qingyunke.com/api.php",{'key': 'free', 'appid': 0, 'msg': ms})
    js.encoding = 'utf8'
    js = js.json()
    return js['content']

bot_message = on_message(rule=to_me(),priority=51)
@bot_message.handle()

async def message_handle(bot:Bot, event:Event):
    msg = event.get_plaintext()
    await bot_message.finish(Message(AI(msg)))