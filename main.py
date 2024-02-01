from pyrogram import Client, idle

api_id = 26966078
api_hash = "a8c50ddacb21496549697fe8dbc86d3e"
bot_token = "6983357194:AAEGAQSVkx7Nld_ji1yWf5ZQuTASCIQ3bBI"

app = Client(
    name = "MOHANPRO",
    api_id = api_id,
    api_hash = api_hash,
    bot_token = bot_token,
)


app.start()
print("Bot fucking")
idle()
