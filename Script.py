class script(object):
    START_TXT = """𝐇𝐄𝐋𝐋𝐎 {}🌝❤️‍🔥 
\n𝐈 𝐂𝐀𝐍 𝐏𝐑𝐎𝐕𝐈𝐃𝐄 𝐌𝐎𝐕𝐈𝐄𝐒 & 𝐒𝐄𝐑𝐈𝐄𝐒 𝐀𝐒 𝐏𝐄𝐑 𝐘𝐎𝐔𝐑 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐈𝐍 𝐆𝐑𝐎𝐔𝐏 🙃❤️‍🔥   \n𝐉𝐔𝐒𝐓 𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 & 𝐄𝐍𝐉𝐎𝐘 🥳🙈"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✿  𝙼𝚈 𝙽𝙰𝙼𝙴: {}
\n✿  𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/ABHINAND3510>Admin 🥱</a>
\n✿  𝙻𝙸𝙱𝚁𝙰𝚁𝚈 & 𝙻𝙰𝙽𝙶: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 | 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
\n✿  𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 & 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙼𝙾𝙽𝙶𝙾𝙳𝙱 | 𝚅𝙿𝚂
\n✿  𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Source - https://t.me/thefilmyspot
<b>DEVS:</b>
- <a href=https://t.me/thefilmyspotin>🌝🤍</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message
<b>NOTE:</b>
1. should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
-Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/thefilmyspotbot)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message Hehe😆)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my database ."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Bot🌝🏷️
<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my Admins😼
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a msg to all connected groups</code>"""
    STATUS_TXT = """<b>Tᴏᴛᴀʟ Fɪʟᴇs Fʀᴏᴍ Bᴏᴛʜ DBs: <code>{}</code>

Bᴏᴛ Usᴇʀs ᴀɴᴅ Cʜᴀᴛs Cᴏᴜɴᴛ
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>

Pʀɪᴍᴀʀʏ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛɪsᴛɪᴄs 
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>

Sᴇᴄᴏɴᴅᴀʀʏ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛɪsᴛɪᴄs
★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{} MB</code>
</b>

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser 🌝🤍
ID - <code>{}</code>
Name - {}
"""
    ALRT_TXT = """Hey {} 🙂,
This Is Not Your Requested Things 😤
Please Request Yourself With Movie Name & Send In This Group 🙂🙏🏼
"""

    OLD_ALRT_TXT = """Hey {} 🙂,
This Is Your Old/Expired Request , 
Please Request Again 🙏🏼.
"""

    CUDNT_FND = """ Not Found Anything Related To 
{}
Please Check The Spelling On Google ....
Choose Any Suggested Title Listed Below ! 👇🏼
"""


    I_CUDNT = """Not Found Anything Related To 
{}
Please Check The Title Is Digitally Released Or Check Spelling ....
"""


    I_CUD_NT = """Not Found Anything Related To
{}
Please Check The Title Is Digitally Released Or Check Spelling ....
"""

    MVE_NT_FND = """ This Movie/Series Is Not Available On Our Database...
Please Check The Title Is Digitally Released Or Check Spelling....
"""

    TOP_ALRT_MSG = """𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐦𝐨𝐯𝐢𝐞 𝐢𝐧 𝐭𝐡𝐞𝐟𝐢𝐥𝐦𝐲𝐬𝐩𝐨𝐭 𝐝𝐚𝐭𝐚𝐛𝐚𝐬𝐞 📀🗂️
"""


    MELCOW_ENG = """<b>HELLO {}🌝❤️

WELCOME TO {} 🤑🥂 

THANKS FOR JOINING &
 KEEP SUPPORTING US 🤍🙌🏻</b>"""

    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : A҉B҉H҉I҉N҉A҉N҉D҉
• ᴜꜱᴇʀɴᴀᴍᴇ : @Abhinand3510
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/abhinand3510'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a></b>"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠
 • Request Admin For a File Not Available, Join @thefilmyspotsupport Group & Request With ▶️ #request <Movie Name>◀️ 
 • Also Check Next Page Below To Find The File You Looking For ! """

    MINFO = """
⚪ REQUESTING FORMAT ⚪

→ Search Name On Google 
→ Then Copy & Paste The Correct Name On Group

Movie : Kgf Chapter 2 2022 Tamil
Series : Breaking Bad s01e14
🚯 Never Use These Any Symbols !"""

    RESTART_TXT = """

<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>

⏰Tɪᴍᴇ : <code>{}</code>

🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    CAPTION = """
<b>📂</b> <code>{file_name}</code>

<b>
╭─────── • ◆ • ───────╮

➠ <a href="https://t.me/+aT55PxDdIbsyZjll">Join 𝐭𝐡𝐞𝐟𝐢𝐥𝐦𝐲𝐬𝐩𝐨𝐭 💎 
For All Movies & Series Files ✅ </a>

╰─────── • ◆ • ───────╯

========= • ✠ • =========

📌 Note : We Only Share contents that are Already on Telegram . 
So If You Have Any Issues With These Files, 
Then We aren't Responsible for That ❗

========= • ✠ • =========</b>"""

    IMDB_TEMPLATE_TXT = """
✿ <b>🏷 Title</b>: <a href={url}>{title}</a>  

✿ 📆 Year: <a href={url}/release_date>{year}</a>  | ⏳ {runtime} Min

✿ 🎭 Genres: {genres}

✿ 🌟 Rating: <a href={url}/ratings>{rating} / 10</a> 

✿ 🎙️ Languages : <code>{languages}</code>

✿ ▶️ : <a href={url}/box_office>{kind}</a> | Seasons 👀: {seasons}

✿ 👥 Cast : <code>{cast}</code>

✿ 📖 Storyline : {plot}

<a href={poster}>Click here for Posters</a>

🗣️ : {message.from_user.mention} 🌝"""
    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋
<i><b>𝚃𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚎𝚕𝚙𝚜 𝚢𝚘𝚞 𝚝𝚘 𝚜𝚑𝚘𝚛𝚝 𝚊 𝚞𝚛𝚕 </i></b>
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /short: <b>𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌</b>
➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/example...</code>"""


