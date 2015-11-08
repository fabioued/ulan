#!/usr/bin/env python

__author__  = 'vickydasta'
__date__    = '06/08/2015'
__apps__    = 'namepy c0re'
__version__ = '1.3'
'''
about: name generator library (namepy)
version: version 1.3
url: github.com/vickydasta/namepy
'''
import random
import logging
import urllib2
from random import shuffle as randomize
import string


class vars():
    @staticmethod
    # set x and y index
    hy = random.choice([ 0, 1, 2, 3, 4, 5, 6, 7 ])
    hx = random.choice([ 0, 1, 2, 3, 4 ])
    # present_word = ['acuh','amin','antah','']
    url = 'http://www.morewords.com/word/%s' # current known words

class algorithm():
    @staticmethod

    def gvoc():
        'return vocal alp h'
        return 'aiueo'
        #make it simpler dude

    def gconslist():
        return [[x for x in list(string.lowercase) if x not in algorithm().gvoc()]
    def gconso(conslist):

        '''
        where the magic happen
        '''
        get_consonant = conslist
        y_index = [0, 1, 2, 3, 4, 5, 6, 7]
        try:
            randomize(y_index)
            randomize(conslist)
            r = random.choice(y_index)
            s = random.choice(y_index)
            t = random.choice(y_index)
            u = random.choice(y_index)
            v = random.choice(y_index)
            w = random.choice(y_index)
            x = random.choice(hy)
            y = random.choice(hy)
            return c[r] + c[s] + c[t] + c[u] + c[v] + c[w] + c[x] + c[u]

        except Exception as errors:
            logging.errors(errors)

    def name_meaning_present(lang='ind',name):
    	url = urllib2.urlopen(+name)
    	read_data = url.read()
    	if re.findall("No words found in this wordlist when searching for",read_data) != []:
    		return True
    	return False

    def generateNames(list1, list2, num=5):
        if len(list1) != 8 and len(list2) != 5:
            pass
        else:
            l=list(list1)
            randomize(l)
            for a in l:
               	for b in list1:
                       l = random.choice([ 0, 1, 2, 3, 4, 5, 6, 7 ])
                       j = random.choice([ 0, 1, 2, 3, 4])
                       final=list2[j]+list1[l]+list1[j]+list2[l]+list1[j]
                       if checkdb('db.txt',final) == 'not':
                           return final
                       else:
                           pass

    def generateName(list1,list2,num=5):
    	global final
    	final = ''
    	#randomize list
    	for a in list1:
    		for b in list2:
    			if num == 5:
    				INDEX1=random.choice([0,1,2,3,4,5,6,7])
    				INDEX2=random.choice([0,1,2,3,4,])
    				final=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]
    			elif num == 6:
    				INDEX1=random.choice([0,1,2,3,4,5,6,7])
    				INDEX2=random.choice([0,1,2,3,4])
    				final=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]+list2[INDEX2]
    	return final


    def DetectRegion(name):
    	pass


    def gencheck(list1,list2):
    	pass
    	'''generate random name with random alphabet
    	'''
    	#select random alphabet
    	pass
    	for a in list1:
    		for b in list2:
    			INDEX1 = random.choice([ 0, 1, 2, 3, 4, 5, 6, 7 ])
    			INDEX2 = random.choice([ 0, 1, 2, 3, 4 ])
    			final = a + b + list1[INDEX2] + list2[INDEX2]+list1[INDEX1]
    			detect_region = region_detector(final)
    			if detect_region == '':
    				res = 'unmatch with current database'
    			else:
    				pass

    			if final != None:
    				res = 'match found'
    				print 'Current Name : {}'.format(final)
    				print 'status : '+ res
    				print '{} comes from --> '.format(final),region_detector(final)
    			else:
    				pass
