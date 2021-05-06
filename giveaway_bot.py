# PROGRAMMED BY @mayvidxd 

from telethon import *
from telethon.sessions import StringSession
import os
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
owner = os.environ.get("USER_ID")
owner = int(owner)
errormessage = os.environ.get("MESSAGE")
channel = os.environ.get("CHANNEL")
string_session = os.environ.get("STRING_SESSION")
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
            dbb = open("database.txt","r")
            dbb1 = dbb.read()
            dbb.close()
            database = list(dbb1)
            for i in database:
                count5 = count5+1
            count6 = 0
            while count6<count5:
                user_id = int(database[count6])
                await client.send_message(user_id,mess)
                count6 = count6+1
    elif event.peer_id.user_id in user_in_channel:
        ui = str(event.peer_id.user_id)
        await client.forward_messages(owner, event.message)
        await client.send_message(owner,ui)
        database.append(ui)
        dbr = open("database.txt","r")
        datas = dbr.read()
        datas = str(datas)
        datas = datas[:-1]
        dbr.close()
        db = open("database.txt","w")
        datastored = str(database)
        datastored = datastored.replace("[",",")
        db1 = db.write(datas + datastored)
        db.close()
    
    else:
        ui = str(event.peer_id.user_id)
        await client.send_message(event.peer_id.user_id,errormessage)
        database.append(ui)
        dbr = open("database.txt","r")
        datas = dbr.read()
        datas = str(datas)
        datas = datas[:-1]
        dbr.close()
        db = open("database.txt","w")
        datastored = str(database)
        datastored = datastored.replace("[",",")
        db1 = db.write(datas + datastored)
        db.close()
    

client.run_until_disconnected()

