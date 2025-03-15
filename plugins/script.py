from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """👋 សួរស្តី {} 

ខ្ងុំជា Tᴇʟᴇɢʀᴀᴍ URL Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ.

**Sᴇɴᴅ ᴍᴇ ᴀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ᴀɴᴅ ɪ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀs ᴀ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ**

Usᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ

"""
    

    HELP_TEXT = """
**Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ** 🤔
   
𖣔 Fɪʀsᴛ ɢᴏ ᴛᴏ ᴛʜᴇ /settings ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴇ ʙᴏᴛ ʙᴇʜᴀᴠɪᴏʀ ᴀs ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.

𖣔 Sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ sᴀᴠᴇ ɪᴛ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ.

𖣔 **Sᴇɴᴅ ᴜʀʟ | Nᴇᴡ ɴᴀᴍᴇ.ᴍᴋᴠ**

𖣔 Sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴏᴘᴛɪᴏɴ.

𖣔 Usᴇ `/caption` ᴛᴏ sᴇᴛ ᴄᴀᴘᴛɪᴏɴ ᴀs Rᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ

"""
    
    ABOUT_TEXT ="""
╭───────────⍟
├📛 **Mʏ Nᴀᴍᴇ** : URL Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ
├📢 **Fʀᴀᴍᴇᴡᴏʀᴋ** : <a href=https://docs.pyrogram.org/>Pʏʀᴏꜰᴏʀᴋ 2.3.58</a>
├💮 **Lᴀɴɢᴜᴀɢᴇ** : <a href=https://www.python.org>Pʏᴛʜᴏɴ 3.13.2</a>
├💾 **Dᴀᴛᴀʙᴀsᴇ** : <a href=https://cloud.mongodb.com>MᴏɴɢᴏDB</a>
├🚨 **Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ** : <a href=https://t.me/AnimationTV_Group>Sᴜᴘᴘᴏʀᴛ</a>
├🥏 **Cʜᴀɴɴᴇʟ** : <a href=https://t.me/AnimationTV_Clouds>Cʜᴀɴɴᴇʟ</a>
├👨‍💻 **Cʀᴇᴀᴛᴇʀ** :  @phu_kdet
╰───────────────⍟
"""


    PROGRESS = """
┣📦 Pʀᴏɢʀᴇꜱꜱ : {0}%
┣ ✅ Dᴏɴᴇ : {1}
┣ 📁 Tᴏᴛᴀʟ : {2}
┣ 🚀 Sᴘᴇᴇᴅ : {3}/s
┣ 🕒 Tɪᴍᴇ : {4}
┗━━━━━━━━━━━━━━━━━━━━
"""

    PROGRES = """
{}
{}
"""


    INFO_TEXT = """
╭──────────────〄
├📛 **Fɪʀsᴛ Nᴀᴍᴇ :** <b>{}</b>
├📛 **Sᴇᴄᴏɴᴅ Nᴀᴍᴇ :** <b>{}</b>
├👤 **Usᴇʀɴᴀᴍᴇ :** <b>@{}</b>
├🆔 **Tᴇʟᴇɢʀᴀᴍ ⵊᴅ :** <code>{}</code>
├🖇️ **Pʀᴏꜰɪʟᴇ Lɪɴᴋ :** <b>{}</b>
├📡 **Dᴄ :** <b>{}</b>
├💮 **Lᴀɴɢᴜᴀɢᴇ:** <b>{}</b>
├💫 **Sᴛᴀᴛᴜs :** <b>{}</b>
╰──────────────────〄
"""


    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🛠️ ការកំណត់', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('😐 មានចម្ងល់?', callback_data='help'),
        InlineKeyboardButton('🎯 អំពីយើងខ្ងុំ', callback_data='about')
        ],[
        InlineKeyboardButton('⛔ បិទ', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🛠️ ការកំណត់', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('🔙 ត្រឡប់', callback_data='home'),
        InlineKeyboardButton('🎯 អំពីយើងខ្ងុំ', callback_data='about')
        ],[
        InlineKeyboardButton('⛔ បិទ', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🛠️ ការកំណត់', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('🔙 ត្រឡប់', callback_data='home'),
        InlineKeyboardButton('😐 មានចម្ងល់?', callback_data='help')
        ],[
        InlineKeyboardButton('⛔ បិទ', callback_data='close')
        ]]
    )
    PLANS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎯 អំពីយើងខ្ងុំ', callback_data='about')
        ],[
        InlineKeyboardButton('🔙 ត្រឡប់', callback_data='home'),
        InlineKeyboardButton('😐 មានចម្ងល់?', callback_data='help')
        ],[
        InlineKeyboardButton('⛔ បិទ', callback_data='close')
        ]]
   )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔ បិទ', callback_data='close')
        ]]
    )
    INCORRECT_REQUEST = """មានបញ្ហា"""
    DOWNLOAD_FAILED = "🔴 មានបញ្ហា 🔴"
    TEXT = "ផ្ញើររូបភាពរបស់លោកអ្នកដើម្បីឲ្យខ្ងុំធ្វើជា ᴛʜᴜᴍʙɴᴀɪʟ ជូន!😁"
    IFLONG_FILE_NAME = " Only 64 characters can be named . "
    RENAME_403_ERR = "សុំទោស! លោកអ្នកមិនអាចផ្លាស់ប្តូរឈ្មោះឯកសារនេះបានទេ!😐"
    ABS_TEXT = " សូម​កុំ​អាត្មានិយម.😐"
    FORMAT_SELECTION = "<b>Sᴇʟᴇᴄᴛ Yᴏᴜʀ Fᴏʀᴍᴀᴛ 👇</b>\n"
    SET_CUSTOM_USERNAME_PASSWORD = """<b>🎯 លោកអ្នកសូមជ្រើសរើសក្នុង Bᴜᴛᴛᴏɴ Vɪᴅᴇᴏ/MP3</b>\n\n<b>🚨ចំណាំ: ប្រសិនបើលោកអ្នកទាញយកវីដេអូពី YᴏᴜTᴜʙᴇ.លោកអ្នកមិនគួរ,ជ្រើសរើសយក Bᴜᴛᴛᴏɴ,ដែលមានអក្សរ,𝗪𝗘𝗕𝗠,ទេ!វាមិនមែនជាវីដេអូឡើយ!❤️</b>\n\n<b>"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "📥 កំពុងធ្វើការដោនឡូត...\n\nFile Name: {}"
    UPLOAD_START = "📤 កំពុងធ្វើការអាប់ឡូត... 📤"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2000MB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "**អគុណសម្រាប់ការប្រើប្រាស់,Botរបស់ខ្ងុំ** 🥰"
    SAVED_CUSTOM_THUMB_NAIL = "**រូបភាព THUMBNAIL ត្រូវរក្សាទុក** ✅"
    DEL_ETED_CUSTOM_THUMB_NAIL = "**DELETED THUMBNAIL** ✅"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "មិនមានរូបភាព ᴛʜᴜᴍʙɴᴀɪʟ ទេ!😐"
    NO_VOID_FORMAT_FOUND = "មានបញ្ហា... <code>{}</code>"
    FILE_NOT_FOUND = "Error, File not Found!!"
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "លោកអ្នកអាចទាក់ទងមកខ្ញុំ។ដើម្បីទទួលបាន,ព័ត៌មានផ្សេងៗទៀត។ @phu_kdet "
    ADD_CAPTION_HELP = """Select an uploaded file/video or forward me <b>Any Telegram File</b> and just write the text you want to be on the file <b>as a reply to the file</b> and the text you wrote will be attached as the caption! 🤩
    
Example: <a href='https://te.legra.ph/file/ecf5297246c5fb574d1a0.jpg'>See This!</a> 👇"""
