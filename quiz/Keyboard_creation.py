from typing import List, Any
from telebot import types
import random
import json


def paintings_buttons(correct_painting: str, stuff: List) -> Any:
    """
    this function creates a keyboard consisting of one correct name of the painting and three other invalid options
    :param correct_painting: The correct name of the painting
    :param stuff:
    :return:
    """
    keyboard = types.InlineKeyboardMarkup()
    stuff.append(correct_painting)
    random.shuffle(stuff)
    for item in stuff:
        if item == correct_painting:
            button = types.InlineKeyboardButton(text=item, callback_data='correct_painting')
            keyboard.add(button)
        else:
            button = types.InlineKeyboardButton(text=item, callback_data='invalid_painting')
            keyboard.add(button)
    return keyboard


def painters_buttons(valid_painter: str) -> Any:
    """
    this function creates a keyboard consisting of one correct name of the painter and three other invalid options
    :param valid_painter: The correct name of the Painting's artist
    :return:
    """
    keyboard = types.InlineKeyboardMarkup()
    with open('Painters_names_storage.json') as file:
        stuff = json.load(file)
        buttons = list()
        buttons.append(valid_painter)
        stuff.remove(valid_painter)
        for _ in range(3):
            item = random.choice(stuff)
            buttons.append(item)
            stuff.remove(item)
        random.shuffle(buttons)
        for entity in buttons:
            if entity == valid_painter:
                button = types.InlineKeyboardButton(text=entity, callback_data='correct_painter')
                keyboard.add(button)
            else:
                button = types.InlineKeyboardButton(text=entity, callback_data='invalid_painter')
                keyboard.add(button)
    return keyboard
