from pyrogram import Client, filters
from AarohiX import app
from pyrogram.types import Message

# -----------------------------------------------------

@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()


# -------------------------------

async def delete_pdf_files(client, message):
    if message.document and message.document.mime_type == "application/pdf":
        warning_message = f"@{message.from_user.username} WARNING ⚠️ ,\n DETECTED COPYRIGHT FILE\n\n @admin Report Successfully \n\n Contact|| @PB65_Aujla || ."
        await message.reply_text(warning_message)
        await message.delete()
    else:  
        pass

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)
