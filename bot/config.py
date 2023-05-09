import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","")
    THANKS = f"""Thanks to ..."""
    BASE = "https://dictionary.abyssinica.com/Services/AjaxService.svc/GetSearchResult"
    API_BASE_URL = os.environ.get("API_URL",BASE)
    Langs = os.environ.get("LANGS","Amhari,Geez").split(',')
    DEF_LANGS = ['Amharic','Geez']


