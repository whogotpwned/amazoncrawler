#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import logging
from os.path import abspath, dirname, join

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from telegram.ext import Updater, CommandHandler

from amazoncrawler import replace_ampersands_in_file, parse_config_file, \
    retrieve_stock_of_all_items_in_config
from tools.plotter import Plotter

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

EXIT_SUCCESS, EXIT_FAILURE = 0, 1

CONF = parse_config_file()
PROJECT_ROOT = abspath(dirname(__file__))
DRIVER_BIN = join(PROJECT_ROOT, "bin/chromedriver")


def _list_all_files_of_type(targetdir, ftype_wildchard):
    """
    Lists all files of a certain type in a certain directory
    :param targetdir: target dir to search files in.
    :param ftype_wildchard: type of files to search for in targetdir.
    :return:
    """
    import glob
    import os
    os.chdir(targetdir)
    return [file for file in glob.glob(ftype_wildchard)]


def start(bot, update):
    """
    Sends a message when the command /start is issued.
    :return:
    """
    assert int(update.message.chat_id) in list(eval(CONF["data"]["bot-options"]["chat-id"]))
    bot.send_message(chat_id=update.message.chat_id, text='Bot started!')

    return EXIT_SUCCESS


def help(bot, update):
    """
    Sends a message when the command /help is issued.
    :return:
    """
    assert int(update.message.chat_id) in list(eval(CONF["data"]["bot-options"]["chat-id"]))
    bot.send_message(chat_id=update.message.chat_id, text='Help!')

    return EXIT_SUCCESS


def retrieve_stock(bot, update):
    """
    Retrieves the current stock of all items in config.
    :return:
    """
    assert int(update.message.chat_id) in list(eval(CONF["data"]["bot-options"]["chat-id"]))

    bot.send_message(chat_id=update.message.chat_id, text="Wait. Stocks are being retrieved...")

    options = Options()
    selenium_options = CONF["data"]["selenium-options"]
    if ast.literal_eval(selenium_options["headless-mode"]):
        options.add_argument("--headless")

    browser = Chrome(executable_path=DRIVER_BIN, options=options)
    retrieve_stock_of_all_items_in_config(browser)

    bot.send_message(chat_id=update.message.chat_id, text="Generating plots...")
    p = Plotter()
    p.plot_and_save_all_plot_files(target_dir=".")

    for f in _list_all_files_of_type(".", "*.png"):
        bot.send_document(chat_id=update.message.chat_id, document=open(f, "rb"))

    bot.send_message(chat_id=update.message.chat_id, text="Done!")

    return EXIT_SUCCESS


def error(bot, update):
    """
    Logs Errors caused by Updates.
    :return:
    """
    assert int(update.message.chat_id) in list(eval(CONF["data"]["bot-options"]["chat-id"]))
    logger.warning('Update "%s" caused error "%s"', bot, update.error)

    return EXIT_SUCCESS


def add_command_handlers_to_dispatcher(target_dispatcher):
    """
    Adds all handlers to the dispatcher.
    :type target_dispatcher: target dispatcher to add handler to.
    :return:
    """
    target_dispatcher.add_handler(CommandHandler("start", start))
    target_dispatcher.add_handler(CommandHandler("help", help))
    target_dispatcher.add_handler(CommandHandler("retrieve_stock", retrieve_stock))
    target_dispatcher.add_error_handler(error)

    return EXIT_SUCCESS


if __name__ == '__main__':
    replace_ampersands_in_file("config.xml")

    updater = Updater(CONF["data"]["bot-options"]["private-token"])

    add_command_handlers_to_dispatcher(updater.dispatcher)

    updater.start_polling()
    updater.idle()
