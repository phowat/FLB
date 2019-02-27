from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ChatAction, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
import logging
import arparse
from sys import exit


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('token', nargs=1, action='store', type=int)
    args = parser.parse_args()
