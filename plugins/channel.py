from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file

media_filter = filters.document | filters.video

EXCLUDED_KEYWORDS = ["predvd", "Predvdrip", "hdcamrip", "apk", "sample", "camrip", "hdcam"]

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
        if any(keyword in media.caption.lower() for keyword in EXCLUDED_KEYWORDS):
            return  # Skip if any excluded keyword is present in the caption
        if media.file_name and any(keyword in media.file_name.lower() for keyword in EXCLUDED_KEYWORDS):
            return  # Skip if any excluded keyword is present in the file name
        await save_file(media)
