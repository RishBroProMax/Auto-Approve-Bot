from os import path, getenv

SUDO = "5171347305"

class Config:
    API_ID = int(getenv("API_ID", "14055090"))
    API_HASH = getenv("API_HASH", "a46f7b439d0afa45b7a69fc450f754e9")
    BOT_TOKEN = getenv("BOT_TOKEN", "5616982320:AAFk0OhEkbFuUMrSSs6dfLdBYhxUI0c9Pt4")
    FSUB = getenv("FSUB", "EmoBotDevolopers")
    CHID = int(getenv("CHID", "-1001551504918"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://rishbro:rishbro@cluster0.eiqoy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
cfg = Config()
