import asyncio
from pyrogram import Client
import json
import time

api_id = 19890531
api_hash = '7ec8158285a1d583eaea1d881c70ca2e'


async def main():
    async with Client('my-acc', api_id, api_hash) as app:
        async for dialog in app.get_dialogs():
            data = json.loads(str(dialog))
            print(data['chat']['id'], data['chat']['username'])
            time.sleep(1)

asyncio.run(main())
