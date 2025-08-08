# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "28904208"))
API_HASH = getenv("API_HASH", "d4cb0faa009a05048a193176fbb6c2f8")
BOT_TOKEN = getenv("BOT_TOKEN", "6920122670:AAEkJdEVd-dgZM0r-O_CES5u7ycQQf6ANDU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6777352931").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Tolemma:Tolemma@cluster0.s7dsa.mongodb.net/?retryWrites=true&w=majority")
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://Tolemma:Tolemma@cluster0.s7dsa.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002243875168")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002243875168"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "10000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "10000"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
