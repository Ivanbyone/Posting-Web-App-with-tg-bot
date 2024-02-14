from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from config import bot
from markups.markups import start_button

router = Router()


@router.message(CommandStart())
async def start_message(message: Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Hi, <b>{message.from_user.full_name}</b>!\n\nClick button to find Post",
                           parse_mode="html",
                           reply_markup=await start_button())
    

@router.message(F.text == "Find post")
async def find_post(message: Message, state: FSMContext) -> None:
    await state.set_state(id)
    await bot.send_message(chat_id=message.from_user.id,
                           text="Write post id to find it")
    