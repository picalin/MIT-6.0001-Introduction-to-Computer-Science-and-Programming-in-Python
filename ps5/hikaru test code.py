# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:18:43 2021

@author: HIKARU
"""
# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        return self.guid
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_link(self):
        return self.link
    
    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        story is one of the instance of NewsStory
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError
        
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def is_in_phrase(self, text):
        text = text.lower()
        #1: remove punctuation in text
        for char1 in string.punctuation:
            text = text.replace(char1, ' ')
        word_list = text.split(' ')
        #2: remove space factor in word_list
        while '' in word_list:
            word_list.remove('')
        #3: change word_list into string
        list_phrase = self.phrase.split()
        if len(word_list) < len(list_phrase):
            return False
        for i in range(len(word_list)-len(list_phrase) + 1):
            if word_list[i] == list_phrase[0]:
                new_word_list = word_list[i:len(list_phrase + i)]
                if new_word_list == list_phrase:
                    return True
        return False

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return self.is_in_phrase(story.get_title())
  
                    



cuddly    = NewsStory('', 'The purple cow is soft and cuddly.', '', '', datetime.now())
exclaim   = NewsStory('', 'Purple!!! Cow!!!', '', '', datetime.now())
symbols   = NewsStory('', 'purple@#$%cow', '', '', datetime.now())
spaces    = NewsStory('', 'Did you see a purple     cow?', '', '', datetime.now())
caps      = NewsStory('', 'The farmer owns a really PURPLE cow.', '', '', datetime.now())
exact     = NewsStory('', 'purple cow', '', '', datetime.now())

plural    = NewsStory('', 'Purple cows are cool!', '', '', datetime.now())
separate  = NewsStory('', 'The purple blob over there is a cow.', '', '', datetime.now())
brown     = NewsStory('', 'How now brown cow.', '' ,'', datetime.now())
badorder  = NewsStory('', 'Cow!!! Purple!!!', '', '', datetime.now())
nospaces  = NewsStory('', 'purplecowpurplecowpurplecow', '', '', datetime.now())
nothing   = NewsStory('', 'I like poison dart frogs.', '', '', datetime.now())

s1 = TitleTrigger('PURPLE COW')

