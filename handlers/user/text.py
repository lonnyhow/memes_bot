from aiogram import Router, types, F
from aiogram.filters.command import CommandStart
from keyboards.inline import show_paginated_jokes_kb, return_to_menu_kb
from utils.main import read_json

router = Router()
lst = read_json('jokes.json')


@router.message(CommandStart())
async def handle_user_start(message: types.Message):


    await message.answer("Привет", reply_markup=show_paginated_jokes_kb(
        lst
    ))


@router.callback_query(F.data.startswith('prev_'))
async def show_prev_jokes(callback: types.CallbackQuery):
    _, start, finish, page = callback.data.split('_')

    if int(page) == 1:
        return await callback.answer("Назад дороги нет", show_alert=True)

    return await callback.message.edit_reply_markup(
        reply_markup=show_paginated_jokes_kb(
            jokes_list=lst,
            start=int(start) - 5,
            finish=int(finish) - 5,
            page=int(page) - 1
        )
    )


@router.callback_query(F.data.startswith('next_'))
async def show_next_jokes(callback: types.CallbackQuery):
    _, start, finish, page, total_pages = callback.data.split('_')

    if int(page) == int(total_pages):
        return await callback.answer("Вперед дороги нет", show_alert=True)

    return await callback.message.edit_reply_markup(
        reply_markup=show_paginated_jokes_kb(
            jokes_list=lst,
            start=int(finish),
            finish=int(finish) + 5,
            page=int(page) + 1
        )
    )

@router.callback_query(F.data.startswith('joke_'))
async def show_joke(callback: types.CallbackQuery):
    _, joke_index, start, finish, page = callback.data.split('_')

    joke = lst[int(joke_index)]

    await callback.message.edit_text(text=joke, reply_markup=return_to_menu_kb(
        start=int(start),
        finish=int(finish),
        page=int(page)
    ))

@router.callback_query(F.data.startswith('menu_'))
async def show_menu(callback: types.CallbackQuery):
    _, start, finish, page = callback.data.split('_')

    await callback.message.edit_text(
        text="Привет",
        reply_markup=show_paginated_jokes_kb(
            jokes_list=lst,
            start=int(start),
            finish=int(finish),
            page=int(page)
        )
    )


