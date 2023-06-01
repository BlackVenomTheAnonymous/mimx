import re, os, time, ipaddress, random, base64, json, urllib.parse, requests
from pyrogram import Client, filters
from telethon.sync import TelegramClient
import random
import string

Bot = Client(
    "SESSION-BOT",
    api_id= 6743126,
    api_hash="97308f0523add6f219fac238eab1e4dd",
    bot_token="6247955593:AAHnjOg2OOPiJFUaeGWkqTuenuq5QHTgKmI"
)
class TempDB:
    CMD = [".", "!", "/"]
@Bot.on_message(filters.command("cp", TempDB.CMD))
async def cp_(c, m):
    try:
        link = m.command[1]
    except BaseException:
        await m.reply("ɪɴᴠᴀʟɪᴅ ғᴏʀᴍᴀᴛ.⚠️\nᴜsᴀɢᴇ ⇾ /cp ᴄʜᴇᴄᴋᴏᴜᴛʟɪɴᴋ ")
    start = time.time()
    cslive= link.split('pay/')[1].split('#')[0]
    pk = urllib.parse.unquote((str(link.split('#')[1])))
    decoded = base64.b64decode(pk)
    dec = ""
    for c in decoded:
        dec += chr(5 ^ c)
    dd = json.loads(dec)
    pklive = dd['apiKey']
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://checkout.stripe.com',
        'referer': 'https://checkout.stripe.com/',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX2163) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'key': pklive, 
        'eid': 'NA',
        'browser_locale': 'en-IQ',
        'redirect_type': 'stripe_js',
    }
    try:
        response = requests.post('https://api.stripe.com/v1/payment_pages/'+cslive+'/init', headers=headers,data=data,).json()
        
        cslive = response['session_id']
        currency = response['currency']
        amount = response['line_item_group']['line_items'][0]['total']
        #images = response['line_item_group']['line_items'][0]['images']
        try:
           emaill = response['customer_email']
        except:
            emaill = "N/A"
        site = response['cancel_url']
        try:
            site = site.split('https://')[1].split('/')[0]
        except BaseException:
            site = "N/A"
    except BaseException:
        A = NA
    k = await m.reply("ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ!")
    caption = f"""
𝗣𝗔𝗥𝗦𝗘𝗗 ✅
━━━━ ɢʀᴀʙʙᴇᴅ ᴅᴇᴛᴀɪʟs ━━

ヤ 𝘊𝘴 ⇾ {cslive}

ヤ 𝘗𝘒 ⇾ {pklive} 

ヤ 𝘌𝘮𝘢𝘪𝘭 ⇾ {emaill} ↯

ヤ 𝘚𝘪𝘵𝘦 ⇾ {site} ↯

ヤ 𝘈𝘮𝘰𝘶𝘯𝘵 ⇾ {amount} ↯

ヤ 𝘊𝘶𝘳𝘳𝘦𝘯𝘤𝘺 ⇾ {currency} ↯

━━━━ ᴏᴛʜᴇʀ ᴅᴇᴛᴀɪʟs ━━
ヤ『𝘛𝘈𝘒𝘌𝘕↯ ⇾  {str(round((time.time() - start), 1))}'s`
ヤ『𝘎𝘳𝘢𝘣𝘣𝘦𝘥 𝘉𝘺 ↯ ⇾  {m.from_user.mention}
ヤ『Dev↯ ⇾ @stripe_checkouters ↯"""
    
    await k.delete()
    try:
        k = await m.reply_text(caption=caption)
    except BaseException:
        k = await m.reply(caption)

print("Bot Started")  
Bot.run()
