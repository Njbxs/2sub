#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Gamau Ribet ? : <a href='tg://user?id={OWNER_ID}'>Klik Link ?</a>\n\n○ Join Grup Vip Berbayar Nonton Tanpa Link\n\n○ Channel Testi Member Yang Sudah Join Grup Vip @TestiVipnero\n\n○ Channel  @VIDEOBOKEPCANDU\n\n○ Channel  @VIDEOJAVTELEGRAM\n\n○Group @CastleVirtual",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
