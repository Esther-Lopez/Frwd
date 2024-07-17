from os import environ 

class Config:
    API_ID = environ.get("API_ID", "18996089")
    API_HASH = environ.get("API_HASH", "9320db7656ad27d7839290383be00c91")
    BOT_TOKEN = environ.get("BOT_TOKEN", "1205133532:AAFfioU9XDHKkUN6bCBelhrY083KEPnqYuU") 
    BOT_SESSION = environ.get("BOT_SESSION", "botzxx") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://tewem57544:LkAPl5h9kpy4sYUS@cluster0.2g2emyt.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forwardbot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '313753983').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
