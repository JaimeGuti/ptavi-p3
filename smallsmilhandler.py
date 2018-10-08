#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    
    def init(self):
        self.width = ""
        self.height = ""
        self.background-color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""