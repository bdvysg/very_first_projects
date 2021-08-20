from conifg import token, chat_id
import telebot
from keyboard import add_hotkey, wait
from requests import get
from pyperclip import paste
import os


def post_content(link: str):
    bot = telebot.TeleBot(token)
    if link.find('http') == 0:
        res = get(link, headers={'User-Agent':
	    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'})
        if res.headers['Content-Type'].startswith('image') == True:
            try:
                with open('file.' + res.headers['Content-Type'][6:], 'wb') as file:
                    file.write(res.content)
                print('return photo')
                bot.send_document(chat_id, open('file.' + res.headers['Content-Type'][6:], 'rb'))
                os.remove('file.' + res.headers['Content-Type'][6:])
            except Exception as ex:
                print(ex)
    
        elif res.headers['Content-Type'].startswith('application') == True:
            try:
                with open('file.' + res.headers['Content-Type'][11:], 'wb') as file:
                    file.write(res.content)
                print('return photo')
                bot.send_document(chat_id, open('file.' + res.headers['Content-Type'][11:], 'rb'))
                os.remove('file.' + res.headers['Content-Type'][11:])
            except Exception as ex:
                print(ex)

        else: 
            try:
                print('return link')
                bot.send_message(chat_id, link)
            except:
                pass
    else: 
        try:
            print('return text')
            bot.send_message(chat_id, link)
        except:
            pass

add_hotkey('Ctrl+`', lambda: post_content(paste()))
wait()

