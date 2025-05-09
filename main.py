import telebot
import json
import random
token="8047793415:AAHtJF8nKenNLWwFTAm-FTGS_CaJTJV1qtk"
bot=telebot.TeleBot(token)
file=open("dannie.json","r",encoding="UTF-8")
slovar=json.load(file)
file.close()


@bot.message_handler(["start"])
def handle_start(message):
    bot.send_message(message.chat.id,"привет")

def tr(message):
    return True

@bot.message_handler(["append"])
def handle_append(message):
    spisoc=message.text.split(" ")
    print(spisoc)
    if len(spisoc)==3:
        slovorus=spisoc[1]
        slovoangl=spisoc[2]
        if str(message.chat.id) not in slovar:
            slovar[str(message.chat.id)]={slovorus:slovoangl}
        else:
            slova=slovar[str(message.chat.id)]
            slova[slovorus]=slovoangl
        file=open("dannie.json","w",encoding="UTF-8")
        json.dump(slovar,file,ensure_ascii=False,indent=4)
        file.close()
    else:
        bot.send_message(message.chat.id,"нужно написать русское и английское слово")
@bot.message_handler(["help"])
def handle_help(message):
    bot.send_message(message.chat.id,"/append-добавляет английские и русские слова"+"\n"+ "/help-покажет доступные команды бота"+"\n"+"/show_words-покажет все добавленные слова"+"\n"+"можете написать боту *привет* или *как дела?* и он ответит")
@bot.message_handler(["show_words"])
def handle_show_words(message):
    if str(message.chat.id) in slovar:
        slova=slovar[str(message.chat.id)]
        print(slova)
        for slovo in slova:
            bot.send_message(message.chat.id,slovo+"-"+slova[slovo])
    else:
        bot.send_message(message.chat.id,"вы не добавили еще не одного слова")
def vvod(message,anglsl,chislo,pravln,nepravln):
    if message.text==anglsl:
        bot.send_message(message.chat.id,"вы правильно ввели слово")
        pravln=pravln+1
    else:
        bot.send_message(message.chat.id,"вы неправильно ввели слово,правильное слово "+anglsl)
        nepravln=nepravln+1
    if chislo>0:
        d=funcia(message)
        sluchshislo=random.randint(0,len(d)-1)
        rusl=d[sluchshislo]
        netid=slovar[str(message.chat.id)]
        anglsl=netid[rusl]
        bot.send_message(message.chat.id,"введите перевод русского слова "+rusl)
        bot.register_next_step_handler_by_chat_id(message.chat.id,vvod,anglsl,chislo-1,pravln,nepravln)
    else:
        bot.send_message(message.chat.id,f"викторина закончилась, правильных-{pravln},неправильных-{nepravln}")
def funcia(message):
        spisoc=[]
        bezid=slovar[str(message.chat.id)]
        for slov in bezid:
            spisoc.append(slov)
        return spisoc
@bot.message_handler(["victorina"])
def handler_victorina(message):
    spisoc=message.text.split(" ")
    if len(spisoc)==2:
        chislo=int(spisoc[1])
        pravln=0
        nepravln=0
        d=funcia(message)
        sluchshislo=random.randint(0,len(d)-1)
        rusl=d[sluchshislo]
        netid=slovar[str(message.chat.id)]
        anglsl=netid[rusl]
        bot.send_message(message.chat.id,"введите перевод русского слова "+rusl)
        bot.register_next_step_handler_by_chat_id(message.chat.id,vvod,anglsl,chislo-1,pravln,nepravln)
    else:
        bot.send_message(message.chat.id,"вы неправильно ввели,правильно:victorina и число")
def namee(message):
    bot.send_message(message.chat.id,"Приятно познакомиться, "+message.text)
@bot.message_handler(["hello_name"])
def handler_helloname(message):
    bot.send_message(message.chat.id,"Как тебя зовут?")
    bot.register_next_step_handler_by_chat_id(message.chat.id,namee)
@bot.message_handler(func=tr)
def handle_all(message):
    if message.text=="привет":
        bot.send_message(message.chat.id,"здравствуйте")
    elif message.text=="как дела?":
        bot.send_message(message.chat.id,"хорошо")
    else:
        bot.send_message(message.chat.id,"не понимаю")
    

bot.polling()

