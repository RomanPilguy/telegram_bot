# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:27:51 2018

@author: POMAH
"""

import telebot
import config
from telebot import types
import urllib3
from bs4 import BeautifulSoup, SoupStrainer

http  = urllib3.PoolManager()
response = http.request('GET','https://timetable.spbu.ru/AMCP/StudentGroupEvents/Primary/14928/2018-05-28')
span = SoupStrainer('div',{'class' :'panel panel-default'})
soup = BeautifulSoup(response.data,parseOnlyThese = span)

class Day:
    def __init__(self,panel):
        self.content = panel
        self.teacher_list = []
        self.subject_list = []
        self.adress_list = []
        self.time_list = []
        
        
list_day = []

for i in soup.findAll('div',{'class' :'panel panel-default'}):
    day = Day(i)
    for a in day.content.findAll(title = "Teachers"):
        if len(a)>1:
            day.teacher_list.append(a.contents[1].contents[1].string)
    for a in day.content.findAll(title = "Subject"):
        day.subject_list.append(a.string)
    for a in day.content.findAll("div","address-modal-btn"):
        day.adress_list.append(a.contents[1].string)
    for a in day.content.findAll("span","moreinfo"):
        day.time_list.append(a.string)
    list_day.append(day)


print(list_day[0].time_list)
      


bot = telebot.TeleBot(config.token)



@bot.message_handler(commands = ['start'])
def start(message):
    
    bot.send_message(message.chat.id,list_day[0].time_list[1])
 
    


    
       
           
                       
                
                
if __name__ == '__main__':
    bot.polling(none_stop=True)
    
        