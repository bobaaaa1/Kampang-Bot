
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


@register(outgoing=True, pattern="^.marsha$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(" Hai Ka saya marsha🥺")
        await e.edit("orang tasikmalaya🥺")
        await e.edit("gak ganteng gak kaya🥺")
        await e.edit("tapi sangat setia🥺")
        await e.edit("Cita-cita pengen hidup poya poya🥺")
        await e.edit("punya istri lima🥺")
        await e.edit("cantik semua🥺")
        await e.edit("paham agama🥺")
        await e.edit(" Kalau kaka mau PC aja ya🥺")
CMD_HELP.update({"siapa": "`.siapa`\
    \nPenjelasan: .siapa. Biar bisa lihat siapa marsha"})
