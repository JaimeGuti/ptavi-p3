#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import json
from urllib.request import urlretrieve


if __name__ == "__main__":

    try:
        file = sys.argv[1]
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")


    parser = make_parser()
    cHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(file))
    # print(cHandler.get_tags())

    # Imprimir listado de etiquetas y atributos-valor
    for elemento in cHandler.get_tags():
        etiqueta = elemento[0]
        # print(etiqueta)
        atributos = ""
        for atributo in elemento[1]:
            if elemento[1][atributo] != "":
                atributos = atributos + '\\t'+ atributo + '="'
                atributos += elemento[1][atributo] + '"'
        print(etiqueta + atributos + '\\n')

    # Funcionalidad para ficheros json
    json_file = file[:-4] + ".json"
    json_file = open(json_file, 'w')
    json.dump(atributos, json_file)

    # Ejercicio 5: descargar en local
    for elemento in cHandler.get_tags():
        for atributo in elemento[1]:
            if elemento[1][atributo][:7] == 'http://':
                print("OOOOOOOOKKKKK")
