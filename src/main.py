import src.config as config
import src.handlers as handlers
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def main():
    updater = Updater(config.TOKEN)
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(CommandHandler(['start', 'boshlash'], handlers.start_command))
    dispatcher.add_handler(CommandHandler(['help', 'yordam'], handlers.help_command))

    # message handlers
    dispatcher.add_handler(MessageHandler(Filters.text, handlers.echo_text))
    dispatcher.add_handler(MessageHandler(Filters.photo, handlers.echo_photo))
    dispatcher.add_handler(MessageHandler(Filters.video, handlers.echo_video))
    dispatcher.add_handler(MessageHandler(Filters.audio, handlers.echo_audio))
    dispatcher.add_handler(MessageHandler(Filters.contact, handlers.echo_contact))
    dispatcher.add_handler(MessageHandler(Filters.location, handlers.echo_location))
    dispatcher.add_handler(MessageHandler(Filters.dice, handlers.echo_dice))
    dispatcher.add_handler(MessageHandler(Filters.sticker, handlers.echo_sticker))
    dispatcher.add_handler(MessageHandler(Filters.document, handlers.echo_document))
    dispatcher.add_handler(MessageHandler(Filters.video_note, handlers.echo_video_note))

    updater.start_polling()
    updater.idle()
