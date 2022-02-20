from telegram.ext import Updater
import requests

def incoming_message_action(update, context):
  image_url=requests.get('https://api.single-developers.software/logo?name='+(update.message.text).replace(' ','%20'))
  context.bot.sendPhoto(chat_id=update.message.chat.id, photo=image_url,
                          reply_to_message_id=update.message.reply_to_message.message_id)

updater.dispatcher.add_handler( MessageHandler(Filters.text, incoming_message_action))
updater.start_polling()
updater.idle()
