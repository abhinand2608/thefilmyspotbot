from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file

media_filter = filters.document | filters.video


@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    """Media Handler"""
    for file_type in ("document", "video"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type
    media.caption = message.caption

    # Check if the file size is greater than or equal to 40MB (40000000 bytes)
    if media.file_size and media.file_size >= 40000000:
        await save_file(media)
