
from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern=r"^\.prg (.*)")
async def honkasays(event):
    await event.edit("`Sedang Memprosess!!!`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("`Beri Aku Bebeberapa Teks, Contoh .prog test`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("`Boss! Saya tidak bisa menggunakan hal-hal sebaris di sini...`")
    except ChatSendStickersForbiddenError:
        await event.edit("Maaf bos, saya tidak bisa mengirim stiker ke sini !!")


CMD_HELP.update({"prog": "`.prg`\
    \nPenjelasan: .prg <kata kata>. Biar bisa lihat kodok bentuk badut"})


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "marsa":

        await event.edit(input_str)

        animation_chars = [

            "𝐏𝐞𝐫𝐤𝐞𝐧𝐚𝐥𝐤𝐚𝐧 𝐬𝐚𝐲𝐚 𝐌𝐚𝐫𝐬𝐡𝐚...",
            "𝐒𝐞𝐤𝐢𝐥𝐚𝐬 𝐢𝐧𝐟𝐨 𝐭𝐞𝐧𝐭𝐚𝐧𝐠 𝐦𝐚𝐫𝐬𝐡𝐚...",
            "(1) 𝐨𝐫𝐚𝐧𝐠 𝐭𝐚𝐬𝐢𝐤𝐦𝐚𝐥𝐚𝐲𝐚: ☑️",
            "(1)𝐨𝐫𝐚𝐧𝐠 𝐭𝐚𝐬𝐢𝐤𝐦𝐚𝐥𝐚𝐲𝐚: ✅",
            "(2) 𝐠𝐚𝐤 𝐠𝐨𝐨𝐝 𝐥𝐨𝐨𝐤𝐢𝐧𝐠: ",
            "(2) 𝐠𝐚𝐤 𝐠𝐨𝐨𝐝 𝐥𝐨𝐨𝐤𝐢𝐧𝐠: ✅",
            "(3) 𝐠𝐚𝐤 𝐤𝐚𝐲𝐚: ",
            "(3) 𝐠𝐚𝐤 𝐤𝐚𝐲𝐚 :",
            "(4) 𝐨𝐫𝐚𝐧𝐠 𝐧𝐲 𝐛𝐚𝐢𝐤: ☑️",
            "(4) 𝐨𝐫𝐚𝐧𝐠 𝐧𝐲 𝐛𝐚𝐢𝐤: ✅",
            "(5) 𝐠𝐚𝐤 SANGEAN: ☑️",
            "(5) 𝐠𝐚𝐤 SANGEAN: ✅",
            "(6) 𝐡𝐮𝐦𝐨𝐫𝐢𝐬: ",
            "(6) 𝐡𝐮𝐦𝐨𝐫𝐢𝐬: ✅",
            "(7) 𝐬𝐞𝐭𝐢𝐚 : ☑️",
            "(7) 𝐬𝐞𝐭𝐢𝐚 : ✅",
            "(8) 𝐤𝐚𝐥𝐚𝐮 𝐦𝐚𝐮 𝐤𝐞𝐧𝐚𝐥 𝐏𝐂 𝐚𝐣𝐚 : ☑️",
            "(8) 𝐤𝐚𝐥𝐚𝐮 𝐦𝐚𝐮 𝐤𝐞𝐧𝐚𝐥 𝐏𝐂 𝐚𝐣𝐚 : ✅",
CMD_HELP.update({"marsa: ".marsa
    \nPenjelasan: .marsa . Biar bisa lihat biodata singkat marsha"})
