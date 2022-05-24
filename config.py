from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5150408662:AAGWTmatjbZfxjSN62lvM54O1StuEFpqjr0")
API_ID = int(getenv("API_ID", "9916333"))
API_HASH = getenv("API_HASH", "452c2f2e15041759acdbe1e02ffd18b8")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sathish:sathish2004!@cluster0.8exqk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5161578942 2141745029").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5161578942 2141745029").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001726630964"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Zeus")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/NotReallyShikhar/YukkiMusicBot"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))

STRING_SESSION1 = "AQAUeStifR3wpkHVehWG1L5e1vUJLspQAnjW8O_JIlGKgxqCafGKZwxZCftoMve7itZuuouYS0qIxRjHvz8AAhZz_1AIUMObxuQqTVEvYGj_IoLj89drc3R98q2MyLk9SbXRrWp8Jl7lfPsxRddczCxw9nS6vqkp_Inj8aetoThfAtLNlVZYzmZyOjsNZBfQhuLhuZE2_GWvD8hIaE1IzJzJSkvDpHHo_4-TV70c9a7G0EGX_i5Jg0Bwx8gvKGB3ts3hxBsg9VoNKbwSFSNe8i6LjbUIQ3kYIljwvcTiKKBH79D54Tg46EY0AgMLvnZ1zmxqCEx5d9OUs1_UIokZaY2qAAAAATa1LgsA"
if str(STRING_SESSION1).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
