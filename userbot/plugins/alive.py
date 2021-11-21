# Thanks to @D3_krish
# Porting in REBELUSERBOT by REBEL75

import asyncio
import random
from telethon import events, version
from userbot import ALIVE_NAME, REBELversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "THANOSBOT"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

REBEL = bot.uid

edit_time = 4
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/96c7031243c9bbaab31eb.jpg"
file2 = "https://telegra.ph/file/97012cc8b32a2744c50b3.jpg"
file3 = "https://telegra.ph/file/ba5bc78cdf6fbc65e1cce.jpg"
file4 = "https://telegra.ph/file/4c1b9c5b5856109533635.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥ＴＨΛＮ♢Ｓ  ＩＳ ΛＬＩＶΣ🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                🔰ᗰᗩՏTᗴᖇ🔰\n      **『😈[{DEFAULTUSER}](tg://user?id={REBEL})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `𝚅𝚎𝚛𝚜𝚒𝚘𝚗:` `{REBELversion}`\n"
pm_caption += f"┣•➳➠ `𝚂𝚞𝚍𝚘:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `𝙲𝚑𝚊𝚗𝚗𝚎𝚕:` [𝙹𝙾𝙸𝙽](https://t.me/thanos_userbot)\n"
pm_caption += f"┣•➳➠ `𝙲𝚛𝚎𝚊𝚝𝚘𝚛:` [RISHABH](https://t.me/MAFIARISHABH)\n"
pm_caption += f"┣•➳➠ `𝙲𝚛𝚎𝚊𝚝𝚘𝚛:` [LUCYBOT](https://t.me/LUCY_MANAGER2_bot)\n"
pm_caption += f"┣•➳➠ `Do Join:` [THANOS CHAT](https://t.me/thanosbot_chat)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥𝐑𝐄𝐏𝐎🔥](https://github.com/Itz-UNKOWN-xd/Lynx-Bot) 🔹 Do Join [📜THANOS CHAT📜](https://t.me/thanosbot_chat)"

# @command(outgoing=True, pattern="^.lynx$")
@bot.on(admin_cmd(outgoing=True, pattern="lynx$"))
@bot.on(sudo_cmd(pattern="lynx$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    

    """ For .lynx command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "rebel", None, "To check am i alive with your favorite alive pic"
).add()
