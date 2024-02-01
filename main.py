from pyrogram import Client, idle
from pyrogram import filters

api_id = 26966078
api_hash = "a8c50ddacb21496549697fe8dbc86d3e"
bot_token = "6983357194:AAEGAQSVkx7Nld_ji1yWf5ZQuTASCIQ3bBI"

app = Client(
    name = "MOHAN_MUSIC_PRO",
    api_id = api_id,
    api_hash = api_hash,
    bot_token = bot_token,
)


@app.on_message(filters.command("start") & filters.private)
async def start_message(client, message):
    message.reply_text(f"Hello, {message.from_user.mention}")





app.start()
print("Bot fucking")
idle()
