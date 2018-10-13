#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.attrs = []
        self.tags = []

    def startElement(self, name, attrs):

        if name == 'root-layout':

            rl = {}
            rl['width'] = ""
            rl['height'] = ""
            rl['background-color'] = ""

            self.tags.append(['root-layout', rl])

        elif name == 'region':

            rg = {}
            rg['id'] = ""
            rg['top'] = ""
            rg['bottom'] = ""
            rg['left'] = ""
            rg['right'] = ""

            self.tags.append(['region', rg])

        elif name == 'img':

            im = {}
            im['src'] = ""
            im['region'] = ""
            im['begin'] = ""
            im['dur'] = ""

            self.tags.append(['img', im])

        elif name == 'audio':

            au = {}
            au['src'] = ""
            au['begin'] = ""
            au['dur'] = ""

            self.tags.append(['audio', au])

        elif name == 'textstream':

            ts = {}
            ts['src'] = ""
            ts['region'] = ""

            self.tags.append(['textstream', ts])

    def get_tags(self):

        return self.tags



if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
