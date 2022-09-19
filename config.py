import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9402346"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "12e6555c5c29b29b6877f88cd2b247cc")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001720937509"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1554867043"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", ""))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝗛𝗮𝗹𝗹𝗼 𝙎𝙖𝙮𝙖𝙣𝙜 {first}\n\n<b>𝙆𝙖𝙢𝙪 𝙃𝙖𝙧𝙪𝙨 𝙅𝙤𝙞𝙣 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝘿𝙪𝙡𝙪 𝙮𝙖𝙖 \n\n𝗠𝗮𝗹𝗲𝘀 𝗞𝗹𝗶𝗸 𝗕𝗼𝘁 𝗧𝗲𝗿𝘂𝘀 ? 𝗝𝗼𝗶𝗻 𝗚𝗿𝘂𝗽 𝗩𝗶𝗽 𝗔𝗷𝗮\n\n𝗣𝗿𝗼𝗺𝗼 𝗣𝗮𝗸𝗲𝘁  2 𝙂𝙍𝙐𝙋 100𝙆\n\n𝗣𝗿𝗼𝗺𝗼 𝗣𝗮𝗸𝗲𝘁  4 𝙂𝙍𝙐𝙋 190𝙆\n\n𝗣𝗿𝗼𝗺𝗼 𝗣𝗮𝗸𝗲𝘁  5 𝙂𝙍𝙐𝙋 250𝙆\n\n𝗣𝗿𝗼𝗺𝗼 𝗣𝗮𝗸𝗲𝘁  7 𝙂𝙍𝙐𝙋 450𝙆\n\n𝙇𝙄𝙎𝙏 𝙂𝙍𝙐𝙋 𝙑𝙄𝙋 @LISTGRUPVIPNERO\n\n𝗝𝗼𝗶𝗻 𝗩𝗶𝗽 𝗖𝗵𝗮𝘁 𝗔𝗱𝗺𝗶𝗻 @AULIAXS\n\n𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙏𝙚𝙨𝙩𝙞 𝙅𝙤𝙞𝙣 𝙑𝙞𝙥 @VIPNERO\n\n𝗣𝗿𝗲𝘃𝗶𝗲𝘄 𝙈𝙚𝙙𝙞𝙖 𝗩𝗶𝗽 𝙉𝙚𝙧𝙤 @PREVIEWMEDIAVIPNERO</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5458946193 1944309678 5585231960 1921712436 5474627943 5079984851 5484100662").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝗛𝗮𝗹𝗹𝗼 𝙎𝙖𝙮𝙖𝙣𝙜 {first}\n\n<b>𝙆𝙖𝙢𝙪 𝙃𝙖𝙧𝙪𝙨 𝙅𝙤𝙞𝙣 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝘿𝙪𝙡𝙪 𝙮𝙖𝙖 \n\n𝗠𝗮𝗹𝗲𝘀 𝗞𝗹𝗶𝗸 𝗕𝗼𝘁 𝗧𝗲𝗿𝘂𝘀 ? 𝗝𝗼𝗶𝗻 𝗚𝗿𝘂𝗽 𝗩𝗶𝗽 𝗔𝗷𝗮\n\n𝗣𝗿𝗼𝗺𝗼 𝗣𝗮𝗸𝗲𝘁  2 𝙂𝙍𝙐𝙋 100𝙆\n\n𝗣𝗿𝗼𝗺𝗼 𝗣𝗮𝗸𝗲𝘁  4 𝙂𝙍𝙐𝙋 190𝙆\n\n𝗣𝗿𝗼𝗺𝗼 𝗣𝗮𝗸𝗲𝘁  5 𝙂𝙍𝙐𝙋 250𝙆\n\n𝗣𝗿𝗼𝗺𝗼 𝗣𝗮𝗸𝗲𝘁  7 𝙂𝙍𝙐𝙋 450𝙆\n\n𝙇𝙄𝙎𝙏 𝙂𝙍𝙐𝙋 𝙑𝙄𝙋 @LISTGRUPVIPNERO\n\n𝗝𝗼𝗶𝗻 𝗩𝗶𝗽 𝗖𝗵𝗮𝘁 𝗔𝗱𝗺𝗶𝗻 @AULIAXS\n\n𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙏𝙚𝙨𝙩𝙞 𝙅𝙤𝙞𝙣 𝙑𝙞𝙥 @VIPNERO\n\n𝗣𝗿𝗲𝘃𝗶𝗲𝘄 𝙈𝙚𝙙𝙞𝙖 𝗩𝗶𝗽 𝙉𝙚𝙧𝙤 @PREVIEWMEDIAVIPNERO</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)

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
