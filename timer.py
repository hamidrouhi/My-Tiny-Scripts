#!/usr/bin/python
# timer up counter
#author revolt313(Hamid Rouhi)
# -*- coding: UTF-8 -*-

import os
import time
s=00;d=00;h=00

def timer()
  while 1:
		os.system('clear')
		print h,':',d,':',s
		
		s=s+1
		if s==60:
			d=d+1
			s=0
			if d==60:
				d=0
				h+1
				if h==24:
					break
				
		time.sleep(1)

	
	
	
