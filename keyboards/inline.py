from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def show_paginated_jokes_kb(jokes_list, start=0, finish=5, page=1):
    length = len(jokes_list)  # кол-во элементов списка
    total_pages = round(length / 5)  # общее кол-во страниц

    buttons = [
        InlineKeyboardButton(text=f'Joke-{i+1}', callback_data=f'joke_{i}_{start}_{finish}_{page}')
        for i in range(start, finish)
    ]
    kb = InlineKeyboardBuilder()
    kb.add(*buttons)
    kb.adjust(1)

    kb.row(
        InlineKeyboardButton(text='<', callback_data=f'prev_{start}_{finish}_{page}'),
        InlineKeyboardButton(text=f'{page}/{total_pages}', callback_data='current'),
        InlineKeyboardButton(text='>', callback_data=f'next_{start}_{finish}_{page}_{total_pages}')
    )

    return kb.as_markup()

def return_to_menu_kb(start, finish, page):
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(text='Назад', callback_data=f'menu_{start}_{finish}_{page}')
    )
    return kb.as_markup()