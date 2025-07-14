from telegram import Update
from telegram.ext import CallbackContext


def start_command(update: Update, context: CallbackContext):
    user = update.effective_user
    text = f"Assalomu alaykum, *{user.full_name}*!\n\nEchoBotga xush kelibsiz, bu bot nima yuborsangiz shuni qaytaradi."
    update.message.reply_markdown(text)


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Menga hohlagan narsa yuboring va men sizni shuni qaytaraman.")


def echo_text(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(text)


def echo_photo(update: Update, context: CallbackContext):
    photo = update.message.photo[0]
    update.message.reply_photo(photo)


def echo_video(update: Update, context: CallbackContext):
    video = update.message.video
    update.message.reply_video(video)


def echo_audio(update: Update, context: CallbackContext):
    audio = update.message.audio
    update.message.reply_audio(audio)


def echo_contact(update: Update, context: CallbackContext):
    contact = update.message.contact
    update.message.reply_contact(contact)


def echo_location(update: Update, context: CallbackContext):
    location = update.message.location
    update.message.reply_location(location)


def echo_dice(update: Update, context: CallbackContext):
    dice = update.message.dice
    update.message.reply_dice(dice)


def echo_sticker(update: Update, context: CallbackContext):
    sticker = update.message.sticker
    update.message.reply_sticker(sticker)


def echo_document(update: Update, context: CallbackContext):
    document = update.message.document
    update.message.reply_document(document)


def echo_animation(update: Update, context: CallbackContext):
    animation = update.message.animation
    update.message.reply_animation(animation)


def echo_voice(update: Update, context: CallbackContext):
    voice = update.message.voice
    update.message.reply_voice(voice)


def echo_animation(update: Update, context: CallbackContext):
    animation = update.message.animation
    update.message.reply_animation(animation)


def echo_video_note(update: Update, context: CallbackContext):
    video_note = update.message.video_note
    update.message.reply_video_note(video_note)
