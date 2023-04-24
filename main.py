import aiogram
import asyncio
from tokensdata import TOKEN

# Create a new Telegram bot with your bot token
bot = aiogram.Bot(token=TOKEN)
dp = aiogram.dispatcher.Dispatcher(bot)

@dp.message_handler(commands=["cite"])
async def cite(message: aiogram.types.Message):
    # Ask the user for the necessary information
    await message.reply("Please enter the author's name in the format 'Lastname, Firstname':")
    author = (await bot.reply("message")).text
    await message.reply("Please enter the publication year (e.g. '2021'):")
    year = (await bot.reply("message")).text
    await message.reply("Please enter the article title:")
    title = (await bot.reply("message")).text
    await message.reply("Please enter the article URL:")
    url = (await bot.reply("message")).text
    await message.reply("Please enter the date accessed (e.g. 'March 13, 2023'):")
    date_accessed = (await bot.reply("message")).text

    # Format the citation using Westminster Harvard style
    citation = f"{author}. ({year}). {title}. [online] Available at: {url} [Accessed {date_accessed}]."

    # Reply to the user with the formatted citation
    await message.reply(citation)

if __name__ == "__main__":
    # Start the bot
    print("Starting bot...")
    loop = asyncio.get_event_loop()
    loop.create_task(dp.start_polling())
    loop.run_forever()
