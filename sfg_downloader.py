#!/usr/bin/env python
"""
Thiss program is written to help people who live in iran .
usage : 
for example you want to download  :
http://sourceforge.net/projects/pydev/files/pydev/Pydev%201.6.5/Pydev%201.6.5.zip/download
you must use :
python main.py -u http://sourceforge.net/projects/pydev/files/pydev/Pydev%201.6.5/Pydev%201.6.5.zip/download
"""

import sys
dl_u = ['kent.dl.sourceforge.net', 'cdnetworks-kr-2.dl.sourceforge.net',
'cdnetworks-kr-2.dl.sourceforge.net', 'cdnetworks-us-1.dl.sourceforge.net',
'cdnetworks-us-2.dl.sourceforge.net', 'dfn.dl.sourceforge.net',
'freefr.dl.sourceforge.net', 'garr.dl.sourceforge.net',
'heanet.dl.sourceforge.net', 'hivelocity.dl.sourceforge.net',
'ignum.dl.sourceforge.net', 'iweb.dl.sourceforge.net',
'jaist.dl.sourceforge.net', 'jaist.dl.sourceforge.net',
'biznetnetworks.dl.sourceforge.net', 'mesh.dl.sourceforge.net',
'nchc.dl.sourceforge.net', 'ncu.dl.sourceforge.net',
'ovh.dl.sourceforge.net', 'puzzle.dl.sourceforge.net',
'softlayer.dl.sourceforge.net', 'sunet.dl.sourceforge.net',
'surfnet.dl.sourceforge.net', 'switch.dl.sourceforge.net',
'transact.dl.sourceforge.net', 'ufpr.dl.sourceforge.net', 'waix.dl.sourceforge.net']
if __name__ == '__main__':
    if len(sys.argv) > 2:
        for arg in sys.argv:
            if arg == '-h':
                print("Usage main.py -u downloadlink")
            if arg == '-u':
                urlt = sys.argv[int(sys.argv[1:].index(arg)) + 2]  
                utags = [s for s in urlt.split('/')]
                for our in dl_u:
                    url_print = utags[0] + "//" + our + "/" + "project/" + utags[4] + "/" + utags[6] + "/" + utags[7] + "/" + utags[8]
                    print(url_print)
    else :
        print("Usage main.py -u downloadlink")
     
    
