# (c) @AbirHasan2005 | @PredatorHackerzZ
# KELEGA FREE FIRE 🔥 😂

import os


class Config(object):
    API_ID = os.environ.get("14050586")
    API_HASH = os.environ.get("42a60d9c657b106370c79bb0a8ac560c")
    BOT_TOKEN = os.environ.get("7818358444:AAEg1M7Zs_3arp-ifmQnHIhzKuxeB4y1A80")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merger_Bot")
    UPDATES_CHANNEL = os.environ.get("@Animes_India_bot")
    LOG_CHANNEL = os.environ.get("-1002281888349")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 5))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("5446367898",1849814176))

    START_TEXT = """
𝐇𝐞𝐥𝐥𝐨! 𝐃𝐮𝐟𝐟𝐞𝐫, 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚 𝐕𝐢𝐝𝐞𝐨 𝐌𝐞𝐫𝐠𝐞𝐫 𝐁𝐨𝐭 𝐛𝐲 [@Animes_India_bot](https://t.me/Animes_India_bot)!
𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐜𝐚𝐧 𝐌𝐞𝐫𝐠𝐞 𝐌𝐮𝐥𝐭𝐢𝐩𝐥𝐞 𝐕𝐢𝐝𝐞𝐨𝐬 𝐢𝐧 𝐎𝐧𝐞 𝐕𝐢𝐝𝐞𝐨 𝐀𝐧𝐃 𝐕𝐢𝐝𝐞𝐨 𝐅𝐨𝐫𝐦𝐚𝐭𝐬 𝐬𝐡𝐨𝐮𝐥𝐝 𝐛𝐞 𝐬𝐚𝐦𝐞. 

𝐌𝐚𝐝𝐞 𝐛𝐲 @Animes_India_bot
"""
    CAPTION = "𝐕𝐢𝐝𝐞𝐨 𝐌𝐞𝐫𝐠𝐞𝐝 𝐛𝐲 @{}\n\n𝐌𝐚𝐝𝐞 𝐛𝐲\n\n@Dads_links"
    PROGRESS = """
🛠 𝐏𝐞𝐫𝐜𝐞𝐧𝐭𝐚𝐠𝐞 : {0}%
✅ 𝐃𝐨𝐧𝐞: {1}
📡 𝐓𝐨𝐭𝐚𝐥: {2}
🚀 𝐒𝐩𝐞𝐞𝐝: {3}/s
⏳ 𝐄𝐓𝐀: {4}
"""
