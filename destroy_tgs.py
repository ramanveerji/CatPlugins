# Made by @e3ris.
# The "-f" flag portion is ported From Friday Userbot, credits to their Devs.

import os
import asyncio

from random import randint, choice
from userbot import catub
from ..core.managers import edit_delete, edit_or_reply
os.system("pip install lottie")

plugin_category = "fun"


@catub.cat_cmd(
	pattern="destroy ?(.*)",
	command=("destroy", plugin_category),
	info={
		"header": "Makes sticker go weeee",
		"description": "TGS Killer :- It changes the dimensions of Animated Sticker",
		"flags": {
			"-f": "based on fRiDaY mode",
		},
		"usage": [
			"{tr}destroy <reply to animated sticker>",
			"{tr}destory -f <reply to sticker>",
		],
	},
)
async def destroy(event):
	"Messify TGS Stickers 🔥"
	args = event.pattern_match.group(1)
	if not event.is_reply:
		return await edit_delete(event, "`Reply to a Sticker`")
	reply = await event.get_reply_message()
	if not (reply.media and reply.file.ext == ".tgs"):
		return await edit_delete(event, "`Reply to a Animated Sticker master`")
	eris = await edit_or_reply(event, "`›››››`")

	dl = await reply.download_media("cat_tgs.tgs")
	await eris.edit("__Downloaded! ››__")
	await asyncio.sleep(1)
	os.system("lottie_convert.py cat_tgs.tgs json1.json")
	with open("json1.json") as f1:
		stick = f1.read()
		f1.close()

	await eris.edit("__processing sticker ›››__")
	await asyncio.sleep(1)

	if args == "-f":
		stick = (
			stick.replace("[1]", "[2]")
			.replace("[2]", "[3]")
			.replace("[3]", "[4]")
			.replace("[4]", "[5]")
			.replace("[5]", "[6]")
		)
	else:
		for i in range(1, randint(6, 12)):
			stick = choice([stick.replace(f'[{i}]', f'[{(i+i)*3}]'), stick.replace(f'.{i}', f'.{i}{i}')])

	with open("json1.json", "w") as f2:
		f2.write(stick)
		f2.close()

	os.system("lottie_convert.py json1.json cat_tgs.tgs")
	await reply.reply(file="cat_tgs.tgs")
	try:
		os.remove("cat_tgs.tgs")
		os.remove("json1.json")
		await eris.delete()
	except Exception:
		pass