#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler


if __name__ == "__main__":

    try:
        file = sys.argv[1]
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file))
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")
