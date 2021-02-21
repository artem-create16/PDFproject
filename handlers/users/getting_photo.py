from aiogram.dispatcher.filters import Command

from loader import dp, bot
from io import BytesIO
from aiogram import types
from fpdf import FPDF
from aiogram.types import InputFile


@dp.message_handler(Command("start"))
async def start_command(message: types.Message):
    await message.answer('Hi man')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def return_document(message: types.Message):
    await message.photo[-1].download(destination=f"/home/rootkali/catPDF.jpg")
    pdf = FPDF()
    pdf.add_page()
    pdf.image("/home/rootkali/catPDF.jpg", x=10, y=10, w=190)
    pdf.output("/home/rootkali/Your_doc.pdf")
    await bot.send_document(chat_id=message.chat.id, document=InputFile("/home/rootkali/Your_doc.pdf"))
