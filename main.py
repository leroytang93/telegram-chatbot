import config as key
import responses as responses
import logging
from telegram import Update
from telegram.ext import *


print("Loading...")
print("How may i help you? Please input these 4 options stated: \n"
      "Input 1 if you require keyboard cleansing e.g. due to spills/dust\n"
      "Input 2 if you require your keyboard to be troubleshooted due to faulty hardware\n")

logging.basicConfig(
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses.responses(text)
    
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(key.API_KEY, use_context=True)
    dp = updater.dispatcher

    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

main()   