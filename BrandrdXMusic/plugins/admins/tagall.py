from BrandrdXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **hey baby nee enga irukaraga🤗🥱** ",
           " **Nee thoogidu irukaragara pola online varama😊** ",
           " **seri, vc vaga pesulam😃** ",
           " **Nee sapidacha..??🥲** ",
           " **Unga v2 yalarum eppudi irukaraga🥺** ",
           " **Naan unai romba miss panuran, athu enaku thareyam🤭** ",
           " **oii Enna panra..??🤨** ",
           " **yen enkita pesamdiya..??🙂** ",
           " **unga name enna enkita sluga..??🥲** ",
           " **Eniku nan Cooking panaporan..??😋** ",
           " **Unnai paartha pinbu naan naanaaga illaiyae😍** ",
           " **Enna pa online varamdikara Romba busy ah😅😅** ",
           " **Eniku day romba mookiya podhuu..??🤔** ",
           " **Nee online thana irukaa vaa tea kudikalam🙄🙄** ",
           " **unaki enna song pudikum enkita slu plzz😕** ",
           " **vc on panuga song kepoma ..??🙃** ",
           " **vannakam Enna panuraga 😛** ",
           " **hello baby soluu..!🌝🫰** ",
           " **vagaa namba gamd play panuvom 🤗** ",
           " **Tea pudikuma 🫰😇** ",
           " **nega Vaga nambs dubai povom 🤭** ",
           " **Enai patha unaku pavama llaya🥺🥺** ",
           " **oii online iruthudu oru message lla enaku😶** ",
           " **Eniku unaku office leave ah..??🤔** ",
           " **oii Good Morning 😜** ",
           " **Pubg pudikuma unaku🙂** ",
           " **enaku romba thookam varuthu😪** ",
           " **nice to meet you ☺** ",
           " **hello🙊** ",
           " **study complet ah??😺** ",
           " **Enna nu slu thambi🥲** ",
           " **niga romba cute ah irukarga...??😅** ",
           " **eniku nan ghost pudika poran..?😅** ",
           " **Good bye😆😆😆** ",
           " **unaku rose milk pudikuma😉** ",
           " **I love you 🙈🙈🙈** ",
           " **Do you love me..?👀** ",
           " **Nan eppudi slurarthu unaa pudichu iruku.??🙉** ",
           " **poidu song kelu thambi..?😹** ",
           " **En alu online vandhuchuuh😻** ",
           " **Instgram Id kadikuma..??🙃** ",
           " **Whatsapp la chat panulama..?😕** ",
           " **Eniku day eppudi pochu unaku..?🙃** ",
           " **Nan unai romba miss panaa..?🙃** ",
           " **unaku black colour pudikuma😊** ",
           " **enkita yarum pesamdikaraga🙁** ",
           " **bye thoogaam varuthu poran😠** ",
           " **unga v2 yalarum eppudi irukaraga..?❤** ",
           " **sluga..?👱** ",
           " **pei dreams varudom unaku 🤧❣️** ",
           " **enna thambi appudi pskuraa😏😏** ",
           " **Nan vaai zh mudiduu irukaporan🤐** ",
           " **chii poo😒** ",
           " **yaru nee comedy piece 😂🤣** "
           " **Hii👀** ",
           " **apple penne nee yaroo 🙈** ",
           " **Unga name enna ☹️** ",
           " **Naliku pakulam 🥺🥺** ",
           " **vannkam da 😂** ",
           " **ungaliku enna song pudikum 🙂** ",
           " **unaku dog pudikuma..?🤔** ",
           " **chat pana yarum llaya..🥺** ",
           " **un manasu enaku mattum thaan🥺🥺** ",
           " **Daii Thookulaya 🤭😅** ",
           " **Group ki vaga😕** ",
           " **Nee commited ah..?👀** ",
           " **peoples comes and leave 😼** ",
           " **Everyone is Selfish🥲** ",
           " **Nan oru ghost👻** ",
           " **nee romba attitude kaduraa🤨** ",
           " **Summa vaedikka mattum paapom...🧐** ",
           " **Evanku oru kedu varamadikuthuu👀** ",
           " **Bro nan ungala enamo ninachea, neega eppudi panniteengale🥲** ",
           " **Bangam thalaiva😂** ",
           " **Nan unga Dubai lla iruken da😅** ",
           " **heloo🧐** ",
           " **Noov mass na neenga🤯** ",
           " **Kangal rendum neerile🥺** ",
           " **Kaadhal ambu vitu enna senjitaley😍** ",
           " **Un reply kaaga kaathirunthu kaathirunthu kaalangal ponathadi🙂** ",
           " **Yen ennai pirindhai uyire𝐢😭** ",
           " **Ennaiya mattum vittu kadalaya podurimgala ellarum🥺** ",
           " **Style style uh than ithu super style uh than😜** ",
           " **Ipo eppudi ambu vittu crt pandrenu mattum paruu🥰** ",
           ]

VC_TAG = [ "**𝐎𝚈𝙴 𝐕𝙲 𝐀𝙰𝙾 𝐍𝙰 𝐏𝙻𝚂🥲**",
         "**𝐉𝙾𝙸𝙽 𝐕𝙲 𝐅𝙰𝚂𝚃 𝐈𝚃𝚂 𝐈𝙼𝙰𝙿𝙾𝚁𝚃𝙰𝙽𝚃😬**",
         "**𝐂𝙾𝙼𝙴 𝚅𝙲 𝙱𝙰𝙱𝚈 𝙵𝙰𝚂𝚃🏓**",
         "**𝐁𝙰𝙱𝚈 𝐓𝚄𝙼 𝐁𝙷𝙸 𝐓𝙷𝙾𝚁𝙰 𝐕𝙲 𝐀𝙰𝙽𝙰🥰**",
         "**𝐎𝚈𝙴 𝐂𝙷𝙰𝙼𝚃𝚄 𝐕𝙲 𝐀𝙰 𝐄𝙺 𝐄𝙰𝙼 𝐇𝙰𝙸🤨**",
         "**𝐒𝚄𝙽𝙾 𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁 𝐋𝙾🤣**",
         "**𝐕𝙲 𝐀𝙰 𝐉𝙰𝙸𝚈𝙴 𝐄𝙺 𝐁𝙰𝚁😁**",
         "**𝐕𝙲 𝐓𝙰𝙿𝙺𝙾 𝐆𝙰𝙼𝙴 𝐂𝙷𝙰𝙻𝚄 𝐇𝙰𝙸⚽**",
         "**𝐕𝙲 𝐀𝙰𝙾 𝐁𝙰𝚁𝙽𝙰 𝐁𝙰𝙽 𝐇𝙾 𝐉𝙰𝙾𝙶𝙴🥺**",
         "**𝐒𝙾𝚁𝚁𝚈 𝐕𝙰𝙱𝚈 𝐏𝙻𝚂 𝐕𝙲 𝐀𝙰 𝐉𝙰𝙾 𝐍𝙰😥**",
         "**𝐕𝙲 𝐀𝙰𝙽𝙰 𝐄𝙺 𝐂𝙷𝙸𝙹 𝐃𝙸𝙺𝙷𝙰𝚃𝙸 𝐇𝚄🙄**",
         "**𝐕𝙲 𝐌𝙴 𝐂𝙷𝙴𝙲𝙺 𝐊𝚁𝙺𝙴 𝐁𝙰𝚃𝙰𝙾 𝐓𝙾 𝐒𝙾𝙽𝙶 𝐏𝙻𝙰𝚈 𝐇𝙾 𝐑𝙷𝙰 𝐇?🤔**",
         "**𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁𝙽𝙴 𝐌𝙴 𝐊𝚈𝙰 𝐉𝙰𝚃𝙰 𝐇 𝐓𝙷𝙾𝚁𝙰 𝐃𝙴𝚁 𝐊𝙰𝚁 𝐋𝙾 𝐍𝙰🙂**",
        ]


@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("🌷 𝐁𝐑𝐀𝐍𝐃𝐄𝐃 𝐓𝐀𝐆 𝐀𝐋𝐋 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐒𝐓𝐎𝐏𝐏𝐄𝐃 🎉")
