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
            rl['width'] = attrs.get('width', "")
            rl['height'] = attrs.get('height', "")
            rl['background-color'] = attrs.get('background-color', "")

            self.tags.append(['root-layout', rl])

        elif name == 'region':

            rg = {}
            rg['id'] = attrs.get('id', "")
            rg['top'] = attrs.get('top', "")
            rg['bottom'] = attrs.get('bottom', "")
            rg['left'] = attrs.get('left', "")
            rg['right'] = attrs.get('right', "")

            self.tags.append(['region', rg])

        elif name == 'img':

            im = {}
            im['src'] = attrs.get('src', "")
            im['region'] = attrs.get('region', "")
            im['begin'] = attrs.get('begin', "")
            im['dur'] = attrs.get('dur', "")

            self.tags.append(['img', im])

        elif name == 'audio':

            au = {}
            au['src'] = attrs.get('src', "")
            au['begin'] = attrs.get('begin', "")
            au['dur'] = attrs.get('dur', "")

            self.tags.append(['audio', au])

        elif name == 'textstream':

            ts = {}
            ts['src'] = attrs.get('src', "")
            ts['region'] = attrs.get('region', "")

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
    print(cHandler.get_tags())
