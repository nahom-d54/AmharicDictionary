import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN","")
    START = "Hello this is an Amharic dictionary bot\Made in 🇪🇹"
    THANKS = f"""Thanks to ..."""
    BASE = "https://dictionary.abyssinica.com/Services/AjaxService.svc/GetSearchResult"
    API_BASE_URL = os.environ.get("API_URL",BASE)
    Langs = os.environ.get("LANGS","Amhari,Geez").split(',')
    DEF_LANGS = ['Amharic','Geez']
    ABOUT = """
The Amharic and Geez Dictionary Telegram Bot is a chatbot that allows users to look up words in Amharic and Geez, two languages spoken in Ethiopia. The bot provides definitions, synonyms, and examples of usage for each word, making it a useful tool for language learners and anyone who wants to improve their vocabulary in these languages.
---- Thanks for ----
[Abissinica](https://dictionary.abyssinica.com/) for making this possible
and [Me](https://t.me/nahom_d54)
"""
    HELP = """
This is the simplest help guide
------------------------------
/start - to start the bot 
/help - for this help message
/about - for the about page

"""


