#!/usr/in/python

# eja
# analisis pengejaan kata dalam Bahasa Indonesia
# algoritma pencarian pola dan pengembangan: vickydasta

__author__ = "vickydasta"
__about__  = "ejalah"

'''
daftar singkatan:
- pk = pola kata
'''

import re
import string

acceptable = [3, 4, 5, 6, 7, 9]
exception = ['pneumonoultramacroscopicsilicovolcanoconiosis'] # its length is 45
vokal = list('aiueo')
kons = ([w for w in string.lowercase if w not in vokal])

def klasifikasi(_str, mode='x'):
    if mode == 'x':
        return ([w for w in _str.lower()])
    return len(x)

def caripola(kata):
    return [(kata[:i], kata[i:]) for i in range(len(kata)+1)]

def pola(pk):
    global acceptable
    while len(pk) in acceptable:
        return caripola(pk)

def main():
    print pola(klasifikasi('nama'))

if __name__ == '__main__':
    main()

