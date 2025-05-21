import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7808438689:AAG3KiOvkDn7N1BBbIzjV30RmjKTqvvnc54")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27099161"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4ebbba630c8da1e27875ba399ae78a7f")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5340147496"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://modkha7110:modkha7110@cluster0.4jiwjny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
