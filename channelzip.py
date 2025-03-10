#    Copyright (C) Midhun KM 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import shutil
import os
import uuid
from userbot import catub

plugin_category = "utils"

@catub.cat_cmd(pattern="channelzip(?: |$)(.*)")
async def starky(event):
    if event.fwd_from:
        return
    un = event.pattern_match.group(1)
    rndm = uuid.uuid4().hex
    dir = f"./{rndm}/"
    media_count = 0
    text_count = 0
    os.makedirs(dir)
    if un:
        channel = un
    else:
        channel = event.chat_id
    await event.edit(f"**Fetching All Files From This Channel**")
    try:
        channel_msgs = await borg.get_messages(channel, limit=3000)
    except:
        await event.edit("**Unable To fetch Messages !** \n`Please, Check Channel Details And IF THere Are Any Media :/`")
        return
    total = int(channel_msgs.total)
    await event.edit(f"**Downloading {total} Media/Messages**")
    for d in channel_msgs:
        if d.media:
            media_count += 1
            await borg.download_media(d.media, dir)
        if d.text:
            text_count += 1
            f = open(f"{dir}{channel}.txt", "a")
            f.write(f"{d.raw_text} \n\n")
    await event.edit(f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts Appended :** `{text_count}` \n**Now Zipping Files.**")
    shutil.make_archive(f"{channel}", "zip", dir)
    tf = await event.edit(f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts Appended :** `{text_count}` \n**Uploading Zip**")
    await borg.send_file(event.chat_id, f"{channel}.zip", caption=f"**Total Media :** `{total}` \n**Downloaded Media :** `{media_count}` \n**Total Texts Appended :** `{text_count}`")
    await tf.delete()
    os.remove(f"{channel}.zip")
    shutil.rmtree(dir)
            



 