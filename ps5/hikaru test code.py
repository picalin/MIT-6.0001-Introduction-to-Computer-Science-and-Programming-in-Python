# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 23:18:43 2021

@author: HIKARU
"""
class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        
    def is_in_phrase(self, text):
        text = text.lower()

a = PhraseTrigger("The purple cow is soft and cuddly")
print(a.__init__("aa"))