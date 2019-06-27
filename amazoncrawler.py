#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from os.path import abspath, dirname, join
from time import sleep

import xmltodict
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from assets.uris import HOME_PAGE, CART_PAGE

EXIT_SUCCESS, EXIT_FAILURE = 0, 1

PROJECT_ROOT = abspath(dirname(__file__))
DRIVER_BIN = join(PROJECT_ROOT, "bin/chromedriver")
BROWSER = Chrome(executable_path=DRIVER_BIN)


def add_to_cart(driver):
    """
    Adds current product to cart.
    :param driver: driver to be used.
    :return:
    """
    try:
        add_to_chart_button = driver.find_element_by_id("add-to-cart-button")
        add_to_chart_button.submit()
    except Exception as e:
        print("Could not add product to cart: {}".format(e))
        return EXIT_FAILURE

    return EXIT_SUCCESS


def go_to_home(driver):
    """
    Redirects to cart page.
    :param driver: driver to be used.
    :return:
    """
    try:
        driver.get(HOME_PAGE)
    except Exception as e:
        print("Could not redirect to home page: {}".format(e))
        return EXIT_FAILURE

    return EXIT_SUCCESS


def go_to_cart(driver):
    """
    Redirects to cart page.
    :param driver: driver to be used.
    :return:
    """
    try:
        driver.get(CART_PAGE)
    except Exception as e:
        print("Could not redirect to cart page: {}".format(e))
        return EXIT_FAILURE

    return EXIT_SUCCESS


def retrieve_stock(driver):
    """
    Utilizes the 999 trick to retrieve the current stock of certain item.
    :param driver: driver to be used.
    :return:
    """
    select = Select(driver.find_element_by_name("quantity"))
    select.select_by_value("10")

    quant_box = driver.find_element_by_name("quantityBox")

    quant_box.send_keys(Keys.BACK_SPACE)
    for i in range(3):
        quant_box.send_keys(Keys.NUMPAD9)
    quant_box.send_keys(Keys.ENTER)

    # wait for correct stock to be set
    sleep(5)

    quant_box = driver.find_element_by_name("quantityBox")
    return quant_box.get_attribute("value")


def get_current_stock_of_item(driver, item):
    """
    Complete workflow of retrieving the current stock of a certain item.
    :param driver: driver to be used.
    :param item: item to retrieve the current stock for.
    :return:
    """
    go_to_home(driver)
    driver.get(item)
    add_to_cart(driver)
    go_to_cart(driver)

    return retrieve_stock(driver)


def remove_last_item_from_cart(driver):
    """
    Removes the last added item from cart.
    :param driver: driver to be used.
    :return:
    """
    try:
        driver.get(CART_PAGE)
        driver.find_element_by_xpath("//input[@type='submit' and @value='Löschen']").click()
    except Exception as e:
        print("Remove button could not be clicked: {}".format(e))
        return EXIT_FAILURE

    return EXIT_SUCCESS


def replace_ampersands_in_file(path_to_target_file):
    """
    Replaces all ampersands in a certain file with its correct encoding.
    :param path_to_target_file: file to replace encodings in.
    :return:
    """
    try:
        with open(path_to_target_file, 'r') as file:
            file_data = file.read()

        file_data = file_data.replace('&', ' ')

        with open(path_to_target_file, 'w') as file:
            file.write(file_data)

    except Exception as e:
        print("Ampersands could not be replaced: {}".format(e))
        return EXIT_FAILURE

    return EXIT_SUCCESS


def create_log_file_if_not_exists(target_log_name):
    """
    Creates log file if not exists.
    :type target_log_name: name of target log file.
    :return:
    """
    import os
    try:
        if not os.path.exists(target_log_name):
            with open(target_log_name, "w") as file_handler:
                file_handler.write("item;stock" + "\n")

    except Exception as e:
        print("File could not be created: {}".format(e))
        return EXIT_FAILURE

    return EXIT_SUCCESS


def parse_config_file():
    """
    Parses the local xml config file.
    :return:
    """
    global conf
    with open("config.xml") as fd:
        conf = xmltodict.parse(fd.read())

    return conf


def retrieve_stock_of_all_items_in_config():
    """
    Utilizes the 999 trick to retrieve the current stock of all items specified in config.xml.
    :return:
    """
    for obj in conf["data"]["item"]:
        try:
            item_list = list(obj.items())

            name, link = item_list[0][1], item_list[1][1]

            stock = get_current_stock_of_item(BROWSER, link)
            remove_last_item_from_cart(BROWSER)
            go_to_home(BROWSER)

            create_log_file_if_not_exists(name + ".csv")

            with open(name + ".csv", "a") as file_handler:
                file_handler.write("{};{}\n".format(datetime.now(), stock))
        except Exception as e:
            print("Stock could not be retrieved for {}: {}".format(obj, e))
            return EXIT_FAILURE

    return EXIT_SUCCESS


def main():
    replace_ampersands_in_file("config.xml")
    parse_config_file()
    retrieve_stock_of_all_items_in_config()


if __name__ == '__main__':
    main()
