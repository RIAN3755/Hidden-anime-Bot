import os
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(os.environ.get("APP_ID", "28029791")),
    api_hash= os.environ.get("API_HASH", "947353175502e3efde36aa961e1d7b57),
    bot_token= os.environ.get("TOKEN", "6162265130:5760852084:AAFLOLQ2SebCXYrlzokGN9Shn4yLvmFSXnQ")
)
