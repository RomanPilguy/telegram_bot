# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 03:58:53 2018

@author: POMAH
"""

import telebot
import config
from telebot import types

from timeTablePage import timeTablePage
from  Soup import Soup



        
        
url_list=['https://timetable.spbu.ru/AMCP/StudentGroupEvents/Primary/14928/2018-05-14',
        'https://timetable.spbu.ru/AMCP/StudentGroupEvents/Primary/14928/2018-05-21',
        'https://timetable.spbu.ru/AMCP/StudentGroupEvents/Primary/14928/2018-05-28',
        'https://timetable.spbu.ru/AMCP/StudentGroupEvents/Primary/14928/2018-06-04',
        'https://timetable.spbu.ru/AMCP/StudentGroupEvents/Primary/14928/2018-06-11'
        ]



page_list = []
for i in url_list:
    page_list.append(timeTablePage(Soup(i).soup))


bot = telebot.TeleBot(config.token)

return_markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)

return_markup.add(types.KeyboardButton("Return"))
g=0

    
    

    
@bot.message_handler(commands = ['start'])
def menu(message):
        
        days_markup = types.ReplyKeyboardMarkup()
        days_markup.add(types.KeyboardButton("Week --->"))
        days_markup.add(types.KeyboardButton("<--- Week"))
        for i in page_list[g].list_day:
            days_markup.add(types.KeyboardButton(i.day[0]))
    
        bot.register_next_step_handler(bot.send_message(message.chat.id,"Сhoose a day",reply_markup = days_markup),show_timetable)
    

def show_timetable(message):
        if message.text =="Week --->":
            global g
            g=g+1
            
            if(g == len(page_list)):
                g=0;
            
          
            bot.register_next_step_handler(bot.send_message(message.chat.id,"_"),menu)
        elif message.text =="<--- Week":
            
            
            g = g-1
            if(g == -1 ):
                g = len(page_list)-1
            bot.register_next_step_handler(bot.send_message(message.chat.id,"_"),menu)
      
        else:
          for i in page_list[g].list_day:
            if message.text == i.day[0]:
                if len(i.time_list )>0:
                    for a in range(len(i.time_list)):
                        bot.send_message(message.chat.id,i.time_list[a] + ' ' +  i.subject_list[a]+ ', ' + i.teacher_list[a] + ', ' + i.adress_list[a])
                else:
                    bot.send_message(message.chat.id,"No Events")
                    
          bot.register_next_step_handler(bot.send_message(message.chat.id,"_",reply_markup  = return_markup),menu) 
         
     
                
if __name__ == '__main__':
    bot.polling(none_stop=True)
    