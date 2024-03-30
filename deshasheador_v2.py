#!/usr/bin/env python3
import hashlib
import argparse
import os
from termcolor import colored

parser = argparse.ArgumentParser(description= 'Convertidor de hash en texto plano')
parser.add_argument( '--hash', type= str, required = True, help='Debes introducir un hash y un diccionario¡¡')
parser.add_argument( '--diccionario',type =str, required=True)
parser = parser.parse_args()
 
def main ():
    if parser.hash and parser.diccionario:
        diccionario = parser.diccionario
        diccionario = open(diccionario, 'r')
        for word in diccionario:
            word = word.strip()
            word_crack = hashlib.sha1(word.encode()).hexdigest()
            if parser.hash == word_crack:
                print (colored(f'La contraseña es: {word}','red'))
                break
            else:
                print (colored(f'La contraseña no es {word}', 'green'))


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print (colored('Saliendo...','yellow'))
        exit()