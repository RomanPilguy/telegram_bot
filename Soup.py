# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 06:28:15 2018

@author: POMAH
"""
import urllib3
from bs4 import BeautifulSoup, SoupStrainer
class Soup :
    def __init__(self,url):
        http  = urllib3.PoolManager()
        self.response = http.request('GET',url)
        self.span = SoupStrainer('div',{'class' :'panel panel-default'})
        self.soup = BeautifulSoup(self.response.data,parseOnlyThese = self.span)