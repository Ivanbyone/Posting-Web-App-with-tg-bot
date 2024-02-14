import asyncio

from config import dp, bot
from router import messages


async def start() -> None:
    dp.include_router(
        messages.router
    )
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except Exception as e:
        print(e)
        