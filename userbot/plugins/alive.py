# Thanks to @D3_krish
# Porting in REBELUSERBOT by REBEL75

import asyncio
import random
from telethon import events, version
from userbot import ALIVE_NAME, REBELversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# ๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค
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
pm_caption = "  __**๐ฅ๐ฅ๏ผด๏ผจฮ๏ผฎโข๏ผณ  ๏ผฉ๏ผณ ฮ๏ผฌ๏ผฉ๏ผถฮฃ๐ฅ๐ฅ**__\n\n"

pm_caption += f"**โโโโโโโโโโโโโโโโโโโโโโโโโโโ**\n\n"
pm_caption += (
    f"                ๐ฐแฐแฉีTแดแ๐ฐ\n      **ใ๐[{DEFAULTUSER}](tg://user?id={REBEL})๐ใ**\n\n"
)
pm_caption += f"โโโโโโโโโโโโโโโโโโโ\n"
pm_caption += f"โฃโขโณโ  `๐๐๐๐๐๐๐๐:` `{version.__version__}` \n"
pm_caption += f"โฃโขโณโ  `๐๐๐๐๐๐๐:` `{REBELversion}`\n"
pm_caption += f"โฃโขโณโ  `๐๐๐๐:` `{sudou}`\n"
pm_caption += f"โฃโขโณโ  `๐ฒ๐๐๐๐๐๐:` [๐น๐พ๐ธ๐ฝ](https://t.me/thanos_userbot)\n"
pm_caption += f"โฃโขโณโ  `๐ฒ๐๐๐๐๐๐:` [RISHABH](https://t.me/MAFIARISHABH)\n"
pm_caption += f"โฃโขโณโ  `๐ฒ๐๐๐๐๐๐:` [LUCYBOT](https://t.me/LUCY_MANAGER2_bot)\n"
pm_caption += f"โฃโขโณโ  `Do Join:` [THANOS CHAT](https://t.me/thanosbot_chat)\n"
pm_caption += f"โโโโโโโโโโโโโโโโโโโ\n"
pm_caption += " [๐ฅ๐๐๐๐๐ฅ](https://github.com/Itz-UNKOWN-xd/Lynx-Bot) ๐น Do Join [๐THANOS CHAT๐](https://t.me/thanosbot_chat)"

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
