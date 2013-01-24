#!/usr/bin/python
#for remove thumbnails of this directory : /home/your_login/.cache/thumbnails/normal
#I love python :)
# enjoy it, ;)
#
import subprocess,sys
Path_rm=subprocess.Popen("rm -r /home/revolt/.cache/thumbnails/",shell=True)
Path_rm.wait()
print "ok,"
sys.exit()
