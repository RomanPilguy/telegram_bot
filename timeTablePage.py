# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 05:24:48 2018

@author: POMAH
"""
from day import Day

class timeTablePage:
    
    def __init__(self,soup):
    
        self.list_day = []
        for i in soup.findAll('div',{'class' :'panel panel-default'}):
            day = Day(i)
            for a in day.content.findAll(title = "Teachers"):
                if len(a)>1:
                    day.teacher_list.append(a.contents[1].contents[1].string)
    
            for a in day.content.findAll("div","address-modal-btn"):
                day.adress_list.append(a.contents[1].string.strip())
            for a in day.content.findAll(title = "Time"):
                day.time_list.append(a.string.strip())
            for a in day.content.findAll(title = "Subject"):
                day.subject_list.append(a.string.strip())
            for a in day.content.findAll("h4","panel-title"):
                day.day.append(a.string.strip())
            self.list_day.append(day)