import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8060637136:AAEPWVz-Oh0qeLwaS5_JwcNsygGh3CsCaZQ")
API_ID = int(os.environ.get("API_ID", "24103884"))
API_HASH = os.environ.get("API_HASH", "257516f22417652d03896cb2e007d6df")


OWNER_ID = int(os.environ.get("OWNER_ID", "1672634667"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Wleakshere:Thunderstrikes27@wleakshere.api7w.mongodb.net/?retryWrites=true&w=majority&appName=Wleakshere")
DB_NAME = os.environ.get("DB_NAME", "madflixbotz")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002348593955"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1000")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[1672634667]
    for x in (os.environ.get("ADMINS", "1672634667").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "Baka! I'm just here to make you smile, not to be your property!"

START_MSG = os.environ.get("START_MESSAGE", " {mention}\n\nI  Well, hello there! Your presence just turned up the heat in here. Ready for some fun?</b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(1672634667)

LOG_FILE_NAME = "wwleakshere_bot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
