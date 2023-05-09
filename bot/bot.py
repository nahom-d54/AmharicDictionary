from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from .dictionary import fetch

async def start(update,context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
    )
async def help_user(update,context):
    user = update.effective_user
    await update.message.text(
        "help"
    )
async def about(update,context):
    user = update.effective_user
    await update.message.text(
        "contrib and users and api mention and "
    )

async def test_func(update,context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def mezgebe_kalat(update,context):
    user = update.effective_user
    word = update.message.text
    response = await fetch(word)
    def construct_msg(res: list):
        msg = ""
        for r in res:
            word_type = r['WordType']
            word_lang = r['Language']
            text = f"""<b>🇪🇹 ቋንቋ {word_lang}</b>\n<b>አይነት {word_type}</b>\n-----------\n"""
            for t in r['defs']:
                text +="<code>" +t+ "</code>" + '\n'
            text += '-----------------\n'
            msg += text
        return msg
            

    msg = construct_msg(response) if construct_msg(response) else "ምንም ትርጉም አልተገኘም !!"
    await context.bot.send_message(chat_id=update.message.chat.id, 
                                   text=msg,
                                   parse_mode="HTML",
                                   disable_web_page_preview=True)
    