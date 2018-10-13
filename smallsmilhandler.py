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

            rl['width'] = ""
            rl['height'] = ""
            rl['background-color'] = ""

            self.tags.append(['root-layout', rl])

        elif name == 'region':

            rg['id'] = ""
            rg['top'] = ""
            rg['bottom'] = ""
            rg['left'] = ""
            rg['right'] = ""

            self.tags.append(['region', rg])

        elif name == 'img':

            im['src'] = ""
            im['region'] = ""
            im['begin'] = ""
            im['dur'] = ""

            self.tags.append(['img', im])

        elif name == 'audio':

            au['src'] = ""
            au['begin'] = ""
            au['dur'] = ""

            self.tags.append(['audio', au])

        elif name == 'textstream':

            ts['src'] = ""
            ts['region'] = ""

            selfs.tags.append(['textstream', ts])

    def get_tags(self):





if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
