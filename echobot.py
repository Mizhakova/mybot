import json
import requests
import time
import urllib
import random

from dbhelper import DBHelper

db = DBHelper()

TOKEN = "463754766:AAFzTMhAsiO5qEimKWzHM-w4oD-dLHqSeuQ"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
prevtext = ""

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def echo_all(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            first_name = update["message"]["chat"]["first_name"]
            last_name = update["message"]["chat"]["last_name"]
            kukuruza = "CAADAgAD-AkAAlxN3gI2bVZtImHGbgI"
            olen = "CAADAgADDggAAlwCZQNFSVgWdzyu6gI"
            vse = "CAADAgAD_wADN4QwAAF8nRYl-ztdpAI"
            besish = "CAADAgADkwEAAjeEMAABpUFEFN_jRTMC"
            prodolzhay = "CAADAgADogQAAjeEMAAB6QXMbZ2d69YC"
            daticho = "CAADAgAD5ggAAjeEMAABEMu0u8RaH_IC"
            zasmeyalsa = "CAADAgADpwQAAjeEMAABEJOQwybLyUwC"
            pomolchi = "CAADAgAD6AgAAjeEMAABIfUQFaWug98C"
            stickers = [kukuruza,olen,vse,besish,prodolzhay,daticho,zasmeyalsa,pomolchi]
            happystickers =["CAADAgAD7wIAAlwCZQN1mgoBtgKe1gI","CAADAgADQwADzUhuAqNVbfK4IYpXAg","CAADAgADeQADl4eRBKiw_kASyMKJAg","CAADAgADRgADihKqDpNhzzTM57IiAg"]
            happy = ["круто","лучше","крутая","крутой","клевая","клевый","клево","прикольно","прикольная","прикольный","здорово","like","лайк","\ud83d\udc4d","\ud83d\ude4f","\ud83d\udcaa"]
            yes = ["ага", "да","конечно","угу","конеш","ясен хер","давай","точно","покажи","покежь"]
            hello = ["привет","дратути", "прив", "здравствуй","здравствуйте","добрый день","добрый вечер","доброе утро","приветики","здарова","хай","hi","hello","хеллоу","халлоу","хелоу","халоу"]
            helloans = ["И тебе не хворать","дратути","приветики"]
            tell = ["расскажи","рассказывай"]
            tellans ="""Суд, дело об избиении Деда Мороза. На скамейке интеллигентного вида мужичок и обычный парень. Судья спрашивает интеллигента:
-Расскажите как дело было. 
-Ехал в автобусе, Дед Мороз наступил мне на ногу. Я думаю, если через 3 минуты не уберет ногу и не извинится, то ударю. Смотрю на часы - 1 минута - стоит. 2 минуты - стоит. 3 минуты - стоит. Вот и не выдержал. 
Судья обращается к парню:
-А вы зачем подключились и начали допинывать ногами?
-А вы себе представьте: еду я в автобусе, вижу стоит какой-то мужик и Дед Мороз. Мужик смотрит то на часы - то на Деда Мороза, то на часы - то на Деда Мороза. Потом как начнет его пиздить, я думал, что по всей стране началось."""
            find = ["найти","искать","находить"]
            findans = ["не теряй","спроси позже"]
            universalans = ["сам знаешь","ой всё","а самому подумать никак?","спроси у тополя"]
            no = ["нет", "неа"]
            kakans = ["нормально", "никак","лучше расскажи у тя как"]
            voicehelp = ["сири","siri","алиса","алису","алисе","алисы","алиска"]
            voicehelpans = ["да, в жопу эту бабу","а вот щас обидно было","ну и иди к ней"]
            start = ["В штанах у тебя ", "Жизнь твоя "]
            greeting = "Дратути, " + first_name + "! Показать че я умею?"
            meme = "http://memesmix.net/media/created/nzzwbb.jpg"
            memeno = "http://memesmix.net/media/created/rm7pi9.jpg"
            db.add_item(text, chat, first_name, last_name)
            if text == "/start":
                send_message(greeting, chat)
            elif any(ans in text.lower() for ans in hello):
                send_message(random.choice(helloans), chat)
            elif any(ans in text.lower() for ans in yes):
                send_message(meme,chat)
            elif text.lower() in no:
                send_message(memeno,chat)
            elif any(ans in text.lower() for ans in tell):
                send_message(random.choice(tellans),chat)
            elif any(ans in text.lower() for ans in find):
                send_message(random.choice(findans),chat)
            elif any(ans in text.lower() for ans in voicehelp):
                send_message(random.choice(voicehelpans),chat)
            elif any(ans in text.lower() for ans in happy):
                send_sticker(random.choice(happystickers),chat)
            elif "?" in text:
                if "как" in text:
                    send_message(random.choice(kakans), chat)
                else:
                    send_message(random.choice(universalans), chat)
            elif len(text.split())>2:
                send_sticker(random.choice(stickers), chat)
            else:
                send_message(random.choice(start)+text, chat)
        except Exception as e:
            sticker = update["message"]["sticker"]["file_id"]
            chat = update["message"]["chat"]["id"]
            send_sticker(sticker,chat)
            print(e)
            print(sticker)


def send_message(text, chat_id):
    db.add_item(text, chat_id, "bot", "bot")
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def send_sticker(sticker, chat_id):
    sticker = urllib.parse.quote_plus(sticker)
    url = URL + "sendSticker?sticker={}&chat_id={}".format(sticker, chat_id)
    get_url(url)


def main():
    db.setup()
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()