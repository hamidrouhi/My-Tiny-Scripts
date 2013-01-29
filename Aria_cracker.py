#!/usr/bin/python
#filename : Aria_cracker.py
#fileversion : 1.0.0
#Author : err2000
#

import md5
import time

#This current path
path = '/home/revolt/dic.txt'
while 1==1 :
    try :
        dictionary = open(path, 'r')
    except IOError :
        print 'problem while reading %s' % path
        time.sleep(3)
        break
    #Get your md5_hash
    pass_hashed = raw_input("Type your hash (q for quit) >>> ")
    if pass_hashed == "q" :
        print "done!"
        time.sleep(3)
        break
    for line in dictionary :
        # Remove the newline_character(\n) at the end of the word
        line = line.replace("\n","")
        password = line
        # Generator md5 hash from dictionarys word
        word_hash = md5.new()
        word_hash.update(password)
        word_hash = word_hash.hexdigest()
        if pass_hashed == word_hash :
            print '%s : %s : OK' % (password,word_hash)
            break
    else :
        print "not found!"



