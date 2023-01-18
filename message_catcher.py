from pyrogram import Client
from pyrogram.handlers import MessageHandler
import json
import logging


main_chat = -1001805969759
receive_chat = -1001461994670

logging.basicConfig(level=logging.INFO)
app = Client("my-acc")



def dump(client, message):
    data = json.loads(str(message))
    if data['chat']['id'] == main_chat:
        if 'media' not in data.keys():
            if 'reply_to_top_message_id' in data.keys():
                topic_id = data['reply_to_top_message_id']
            else:
                topic_id = data['reply_to_message_id']
            text = ''
            if 'username' in data['from_user'].keys():
                text += '@' + data['from_user']['username'] + '\n'
            if 'first_name' in data['from_user'].keys():
                text += data['from_user']['first_name'] + '\n'
            app.send_message(
                chat_id=receive_chat,
                text=text + data['text']
            )
        elif 'sticker' in data.keys():
            app.send_sticker(chat_id=receive_chat,
                             sticker=data['sticker']['file_id'])
        elif 'photo' in data.keys():
            # print(message)
            text = 'Фото '
            if 'username' in data['from_user'].keys():
                text += '@' + data['from_user']['username'] + '\n'
            if 'first_name' in data['from_user'].keys():
                text += data['from_user']['first_name'] + '\n'
            if 'caption' in data.keys():
                app.send_photo(chat_id=receive_chat,
                               photo=data['photo']['file_id'],
                               caption=text + data['caption'])
            else:
                app.send_photo(chat_id=receive_chat,
                               photo=data['photo']['file_id'],
                               caption=text)
        elif 'document' in data.keys():
            text = 'Документ '
            if 'username' in data['from_user'].keys():
                text += '@' + data['from_user']['username'] + '\n'
            if 'first_name' in data['from_user'].keys():
                text += data['from_user']['first_name'] + '\n'
            if 'caption' in data.keys():
                app.send_document(chat_id=receive_chat,
                                  document=data['document']['file_id'],
                                  caption=text + data['caption'])
            else:
                app.send_document(chat_id=receive_chat,
                                  document=data['document']['file_id'],
                                  caption=text)
        elif 'video' in data.keys():
            text = 'Видео '
            if 'username' in data['from_user'].keys():
                text += '@' + data['from_user']['username'] + '\n'
            if 'first_name' in data['from_user'].keys():
                text += data['from_user']['first_name'] + '\n'
            if 'caption' in data.keys():
                app.send_video(chat_id=receive_chat,
                               video=data['video']['file_id'],
                               caption=text + data['caption'])
            else:
                app.send_video(chat_id=receive_chat,
                               video=data['video']['file_id'],
                               caption=text)


app.add_handler(MessageHandler(dump))

app.run()
