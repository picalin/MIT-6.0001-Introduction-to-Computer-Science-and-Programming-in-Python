# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:18:43 2021

@author: HIKARU
"""
import string
class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
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
            
        #3: make phrase list
        phrase_list = self.phrase.split(' ')
        #4: 連番でフレーズリストがtextにあればTrue
        check = []
        for char2 in phrase_list:
            for i, char3 in enumerate(word_list):
                if char2 == char3:
                    check.append(i)
        
        if len(check) < len(phrase_list):
            return False
        for i in range(len(check)-1):
            if check[i + 1] - check[i] != 1:
                return False
        return True
                    

           
a = PhraseTrigger("purple cow")
print(a.phrase)

# print(a.is_in_phrase("The purple cow is soft!! and cuddly!!"))
print(a.is_in_phrase("soft!! purple    Cuddly@!  cow"))


