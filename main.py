import config
import handlers
from telegram.ext import Updater, CommandHandler


def main():
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', handlers.start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
