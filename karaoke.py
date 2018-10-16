#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import json
import urllib.request


class KaraokeLocal():

    def __init__(self, file):
        parser = make_parser()
        self.cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(self.cHandler)
        parser.parse(open(file))
        # print(cHandler.get_tags())

    def __str__(self):
        for elemento in self.cHandler.get_tags():
            etiqueta = elemento[0]
            # print(etiqueta)
            atributos = ""
            for atributo in elemento[1]:
                if elemento[1][atributo] != "":
                    atributos = atributos + '\\t' + atributo + '="'
                    atributos += elemento[1][atributo] + '"'
                    self.list = etiqueta + atributos
            print(etiqueta + atributos + '\\n')

    def to_json(self, file, json_file):
        json_file = open(json_file, 'w')
        json.dump(self.list, json_file)

    def do_local(self):
        for elemento in self.cHandler.get_tags():
            for atributo in elemento[1]:
                if elemento[1][atributo][:7] == 'http://':
                    urllib.request.urlretrieve(elemento[1][atributo])
                    # Ejercicio 6: indica la localización local del recurso
                    elemento[1][atributo] = elemento[1][atributo].split('/')

if __name__ == "__main__":

    try:
        file = sys.argv[1]
        json_file = file[:-4] + "json"
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")

    karaoke = KaraokeLocal(file)
    karaoke.__init__(file)
    karaoke.__str__()
    karaoke.to_json(file, json_file)
    karaoke.do_local()
    karaoke.to_json(file, 'local.json')
