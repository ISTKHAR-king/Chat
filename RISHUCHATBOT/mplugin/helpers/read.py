from config import OWNER_USERNAME, SUPPORT_GRP
from RISHUCHATBOT import RISHUCHATBOT
from pyrogram import Client, filters



START = """**
❍ ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ꜱᴜᴘᴇʀғᴀꜱᴛ ᴄʜᴀᴛʙᴏᴛ 

❍ ꜱᴜᴘᴘᴏʀᴛꜱ ᴛᴇxᴛ, ꜱᴛɪᴄᴋᴇʀ, ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ...
❍ ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ
❍ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ  
❍ ʏᴏᴜ ᴄᴀɴ ᴄʟᴏɴᴇ/ᴍᴀᴋᴇ ᴄʜᴀᴛʙᴏᴛ  
❍ ᴍᴀᴋᴇ ʏᴏᴜʀ ɪᴅ-ᴄʜᴀᴛʙᴏᴛ 


╔═══ ⋆ʟᴏᴠᴇ ᴡɪᴛʜ⋆ ══╗
♡ [⋆⎯꯭‌𝅃꯭᳚❤️‍🔥꯭⃕ ⃪꯭〬𐏓꯭𝐈꯭꯭ѕ꯭꯭፝֠֩‌тк꯭꯭н፝֠֩‌α꯭꯭я꯭꯭𝄄𝄀꯭𝄄꯭🔥꯭᪳𝆺꯭𝅥⎯‌꯭⟶⋆](https://t.me/ll_ISTKHAR_BABY_lll) ♡
╚═════ ⋆★⋆ ═════╝

➲ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴩꜱ ᴛᴏ ᴜꜱᴇ ꜰᴇᴀᴛᴜʀᴇꜱ.
**"""

HELP_READ = f"""**
Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/ur_support07).

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /**
"""

TOOLS_DATA_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴛᴏᴏʟꜱ:

➻ /start ᴛᴏ ᴡᴀᴋᴇ ᴜᴘ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ʀᴇᴄᴇɪᴠᴇ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇssᴀɢᴇ!
──────────────
➻ /help ғᴏʀ ɢᴇᴛᴛɪɴɢ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs.
──────────────
➻ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ (ᴘɪɴɢ) ᴏғ ᴛʜᴇ ʙᴏᴛ!
──────────────
➻ /id ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴜsᴇʀ ɪᴅ, ᴄʜᴀᴛ ɪᴅ, ᴀɴᴅ ᴍᴇssᴀɢᴇ ɪᴅ ᴀʟʟ ɪɴ ᴏɴᴇ ᴍᴇssᴀɢᴇ.
──────────────
➻ /broadcast ᴛᴏ ғᴏʀᴡᴀʀᴅ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄʜᴀᴛs ʙᴀsᴇᴅ ᴏɴ sᴘᴇᴄɪғɪᴇᴅ ғʟᴀɢs!\nᴇxᴀᴍᴘʟᴇ: `/broadcast -user -pin ʜᴇʟʟᴏ ғʀɪᴇɴᴅs`
──────────────
➻ /shayri ɢᴇᴛ ʀᴀɴᴅᴏᴍ sʜᴀʏʀɪ ғᴏʀ ʏᴏᴜʀ ʟᴏᴠᴇ
──────────────
➻ ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ ғᴏʀ ᴇᴀᴄʜ ᴄʜᴀᴛ /lang
➻ ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ/ᴅɪꜱᴀʙʟᴇᴅ ʙʏ /chatbot
➻ ʏᴏᴜ ᴄᴀɴ ᴄʟᴏɴᴇ/ᴍᴀᴋᴇ ᴄʜᴀᴛʙᴏᴛ ʙʏ /clone
➻ ᴍᴀᴋᴇ ʏᴏᴜʀ ɪᴅ-ᴄʜᴀᴛʙᴏᴛ ʙʏ /idclone
──────────────
➲ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴩꜱ ᴛᴏ ᴜꜱᴇ ꜰᴇᴀᴛᴜʀᴇꜱ.**
"""

CHATBOT_READ = f"""**
๏ ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴄʜᴀᴛʙᴏᴛ:

➻ /chatbot - ᴏᴘᴇɴs ᴏᴘᴛɪᴏns ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.
──────────────
➻ /lang, /setlang - ᴏᴘᴇɴs ᴀ ᴍᴇɴᴜ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴄʜᴀᴛ ʟᴀɴɢᴜᴀɢᴇ.  
──────────────
➻ /resetlang, /nolang - ʀᴇsᴇᴛs ᴛʜᴇ ʙᴏᴛ's ʟᴀɴɢᴜᴀɢᴇ ᴛᴏ ᴍɪxᴇᴅ ʟᴀɴɢᴜᴀɢᴇ.
──────────────
➻ /chatlang - ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ᴜꜱɪɴɢ ᴄʜᴀᴛ ʟᴀɴɢ ꜰᴏʀ ᴄʜᴀᴛ.
──────────────
➻ /status - ᴄʜᴇᴄᴋ ᴄʜᴀᴛʙᴏᴛ ᴀᴄᴛɪᴠᴇ ᴏʀ ɴᴏᴛ.
──────────────
➻ /stats - ɢᴇᴛ ʙᴏᴛ ꜱᴛᴀᴛꜱ
──────────────
➻ /clone [ ʙᴏᴛ ᴛᴏᴋᴇɴ ] - ᴛᴏ ᴄʟᴏɴᴇ ʏᴏᴜʀ ʙᴏᴛ.
──────────────
➻ /idclone [ ᴩʏʀᴏɢʀᴀᴍ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ] - ᴛᴏ ᴍᴀᴋᴇ ɪᴅ-ᴄʜᴀᴛʙᴏᴛ.
──────────────
➲ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴩꜱ ᴛᴏ ᴜꜱᴇ ꜰᴇᴀᴛᴜʀᴇꜱ.
**"""

SOURCE_READ = f"**ʜᴇʏ, ᴛʜᴇ [{RISHUCHATBOT.name}](https://t.me/{RISHUCHATBOT.username}) ɪs ɴᴇᴡ ᴘᴏᴡᴇʀғᴜʟʟ ᴄʜᴀᴛʙᴏᴛ ᴏғ ᴡʜᴏʟᴇ ᴛᴇʟᴇɢʀᴀᴍ.**\n\n**ᴘʟᴇᴀsᴇ ᴅᴏɴᴀᴛᴇ ᴛʜᴇ ᴅᴇᴠʟᴏᴘᴇʀ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴ ᴛʜᴇ ᴘʀᴏɪᴇᴄᴛs**\n\n**──────────────────**\n\n**ʜᴇʀᴇ ɪs ᴛʜᴇ ǫʀ [ᴅᴏɴᴀᴛᴇ ʜᴇʀᴇ](https://t.me/ll_ISTKHAR_BABY_lll/8)**\n\n**──────────────────**\n\n**ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴀᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/{SUPPORT_GRP})..\n\n<b>||ʟᴏᴠᴇ ᴡɪᴛʜ ➪ [ ⋆⎯꯭‌𝅃꯭᳚❤️‍🔥꯭⃕ ⃪꯭〬𐏓꯭𝐈꯭꯭ѕ꯭꯭፝֠֩‌тк꯭꯭н፝֠֩‌α꯭꯭я꯭꯭𝄄𝄀꯭𝄄꯭🔥꯭᪳𝆺꯭𝅥⎯‌꯭⟶⋆](https://t.me/THUNDERDEVS) **||</b>"

ADMIN_READ = f"sᴏᴏɴ"

ABOUT_READ = f"""
**➻ [{RISHUCHATBOT.name}](https://t.me/{RISHUCHATBOT.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**

**➻ [{RISHUCHATBOT.name}](https://t.me/{RISHUCHATBOT.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**

**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**

**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**

**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{RISHUCHATBOT.name}](https://t.me/{RISHUCHATBOT.username})**
"""
