from pyrogram import Client

api_id = 1006088
api_hash = "35f4b10cab604a1cb4088f8d83471129"

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "Greetings from Pyrogram!")
