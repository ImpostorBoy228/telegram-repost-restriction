from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import asyncio

BOT_TOKEN = "INSERT"
TARGET_CHAT = INSERT_ID

BANNED_FORWARD_IDS = [-1001418440636, -1001787778169] # channel ids

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.chat.id == TARGET_CHAT, F.forward_from_chat)
async def delete_forward(message: Message):
    forward_chat = message.forward_from_chat
    if forward_chat and forward_chat.id in BANNED_FORWARD_IDS:
        try:
            await message.delete()
            print(f"Deleted forward {message.message_id}")
        except Exception as e:
            print(f"Failed to delete {message.message_id}: {e}")

async def main():
    print("Live filter started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
