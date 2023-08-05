# * @author        Nicky Lalrochhara <nickylalrochhara917@gmail.com>
# * @date          2023-06-21 22:12:27
# * @projectName   Sangtei
# * Copyright ©NickyLrca All rights reserved
import time
from logging import ERROR, INFO, StreamHandler, basicConfig, getLogger, handlers

from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from async_pymongo import AsyncClient
from pymongo import MongoClient
from pyrogram import Client

from Sangtei.core import Sangtei_patch
from Sangtei.vars import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    DATABASE_NAME,
    DATABASE_URI,
    TZ,
    USER_SESSION,
)

basicConfig(
    level=INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s.%(funcName)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        handlers.RotatingFileHandler("SangteiLogs.txt", mode="w+", maxBytes=1000000),
        StreamHandler(),
    ],
)
getLogger("pyrogram").setLevel(ERROR)
getLogger("openai").setLevel(ERROR)
getLogger("httpx").setLevel(ERROR)
getLogger("iytdl").setLevel(ERROR)

MOD_LOAD = []
MOD_NOLOAD = ["subscene_dl"]
HELPABLE = {}
cleanmode = {}
botStartTime = time.time()
Sangtei_version = "v2.10.13 - Stable"

# Pyrogram Bot Client
app = Client(
    "SangteiBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    mongodb=dict(connection=AsyncClient(DATABASE_URI), remove_peers=False),
)

# Pyrogram UserBot Client
user = Client(
    "SangteiBot",
    session_string=USER_SESSION,
    mongodb=dict(connection=AsyncClient(DATABASE_URI), remove_peers=False),
)

jobstores = {
    "default": MongoDBJobStore(
        client=MongoClient(DATABASE_URI), database=DATABASE_NAME, collection="nightmode"
    )
}
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone=TZ)

app.start()
BOT_ID = app.me.id
BOT_NAME = app.me.first_name
BOT_USERNAME = app.me.username
if USER_SESSION:
    user.start()
    UBOT_ID = user.me.id
    UBOT_NAME = user.me.first_name
    UBOT_USERNAME = user.me.username
else:
    UBOT_ID = None
    UBOT_NAME = None
    UBOT_USERNAME = None
