from os import path, getenv

SUDO = "5171347305"

class Config:
    API_ID = int(getenv("API_ID", "140090"))
    API_HASH = getenv("API_HASH", "a46f7b439d0f754e9")
    BOT_TOKEN = getenv("BOT_TOKEN", "5616982320:dBYhxUI0c9Pt4")
    FSUB = getenv("FSUB", "EmoBotDevolopers")
    CHID = int(getenv("CHID", "-1000112234"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rishbs=true&w=majority")
    
cfg = Config()
