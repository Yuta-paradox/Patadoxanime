import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7176408406:AAHK6MRvOUTHGJrNdsHtLhSLBAtHb3Xo9kM")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26977508"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "396589629e6705c592bc7fe891dc6e37")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002041068526"))

# Port
PORT = os.environ.get("PORT", "8040")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Ujwal:JZCVCfWTThhegRxt@ujwal.82hvrit.mongodb.net/?retryWrites=true&w=majority&appName=Ujwal")
DB_NAME = os.environ.get("DATABASE_NAME", "Summer")

# Force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1673982355"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1002196790523"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))

# Mainly add graph else telegraph link
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/9f10cfb5ea93d4766357e.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/541d20525d6938d2fd77e.jpg")

# Add your text according to your preference
HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for @Animes_Paradox\n\n❏ Bot Cammands\n├/start : start the bot\n├/about : Our Information\n└/help : Help related Bot\n\n💥 Simply click on link and start the bot join both channels and try again thats it.....!\n\n🧑‍💻Developed by <a href=https://t.me/spy_Radios>Yuta Paradox</a></b>"
ABOUT_TXT = "<b>⟦⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ My God: <a href=https://t.me/spy_Radios>Yuta</a>\n◈ Animes channel : <a href=https://t.me/Animes_Paradox>Anime Paradox</a>\n◈ Ongoing Anime : <a href=https://t.me/Ongoing_Paradox>Ongoing Paradox</a>\n◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>\n◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>\n◈ Develop By  : <a href=https://t.me/Spy_Radios>Yuta</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"

# start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - @Animes_Paradox</b>")
try:
    ADMINS=[6193451722]
    for x in (os.environ.get("ADMINS", "6193451722").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Owner list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Animes_Paradox"


OWNER_ID = int(os.environ.get("OWNER_ID", "5090651635"))
ADMINS.append(OWNER_ID)
ADMINS.append(5090651635)

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

LOG_FILE_NAME = "filesharingbot.txt"
LOG_FILE_NAME = "filesharingbot.txt"

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

# Hi There My Name is Sahil and if you like this repo make sure to give it a thumbs up and don't Remove my credit....
