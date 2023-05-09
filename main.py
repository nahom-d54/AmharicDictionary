from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from bot.config import Config
from bot.bot import start,help_user,about,mezgebe_kalat




class createApp:
    def __init__(self):
        self.application = Application.builder().token(Config.BOT_TOKEN).build()
    def app(self):
        return self.application
    ## the below decorator is not oprational
    def command_handler(self,command=None,filter : list = None):
        def add_handler(func):
            def wrapper():
                if command:
                    self.application.add_handler(CommandHandler(command, func))
                elif filter:
                    for key in filter:
                        self.application.add_handler(MessageHandler(key, func))
                return wrapper
        return add_handler


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.

    # on different commands - answer in Telegram
    application = createApp().app()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_user))
    application.add_handler(CommandHandler("about", about))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mezgebe_kalat))

    # Run the bot until the user presses Ctrl-C
    print('App started running')
    application.run_polling()


if __name__ == "__main__":
    main()