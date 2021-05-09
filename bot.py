# PROGRAMMED BY @mayvidxd 

from telethon import *
import asyncio
from telethon.sessions import StringSession
import os
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
owner = int(os.environ.get("USER_ID"))
errormessage = os.environ.get("MESSAGE")
channel = os.environ.get("CHANNEL")
string_session = os.environ.get("STRING_SESSION")
errormessage = errormessage + "\nBOT DEVLOPED BY ★𝓐𝓟★"
client = TelegramClient(StringSession(string_session), api_id, api_hash)
client.start()
user_in_channel = list()
database = list()
@client.on(events.NewMessage)
async def my_event_handler(event):
    async for user in client.iter_participants(channel):
        user_in_channel.append(user.id)
    if event.peer_id.user_id == owner:
        if event.raw_text[0:5] == "/send":
            mess = event.raw_text[6:]
            mess2 = mess.find(" ")
            mess3 = int(mess[0:mess2])
            mess4 = mess[mess2 +1 :]
            await client.send_message(mess3,mess4)
        elif event.raw_text[0:10] == "/broadcast":
            mess = event.raw_text[11:]
            count5 = 0
            for i in database:
                count5 = count5+1
            count6 = 0
            while count6<count5:
                user_id = int(database[count6])
                await client.send_message(user_id,mess)
                count6 = count6+1
        elif event.raw_text == "./senddata":
            datanh = str(database)
            await client.send_message(owner,datanh)
    elif event.peer_id.user_id in user_in_channel:
        ui = str(event.peer_id.user_id)
        await client.forward_messages(owner, event.message)
        await client.send_message(owner,ui)
        if ui in database:
            pass
        else:
            database.append(ui)
    else:
        ui = str(event.peer_id.user_id)
        await client.send_message(event.peer_id.user_id,errormessage)
        if ui in database:
            pass
        else:
            database.append(ui)



client.run_until_disconnected()
