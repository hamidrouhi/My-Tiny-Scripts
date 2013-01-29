#!/usr/bin/python
#this app help you for check open port on your entred range IP
#author Revolt313(Hamid Rouhi)
# hrouhi[dot]kh[at]gmail[dot]com :}
import string,os,socket
ip3=[];ports=[80,21,23];log=open("log.txt",'a')

def data_in():
  try:
		global ip2,end
		ip1=(raw_input("ip 1 : "))
		end=(raw_input("ip 2 : "))
		ip2=ip1.split(".")
		range_ip_proc_()
	except KeyboardInterrupt:pass
def ip_port_proc_():
	try:
		log2=open('log2.txt','w')
		log=open("log.txt",'r')
		for line in log:
			print 60*'-','\n'
			print str(line)
			for i in ports:
				try:
					s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
					s.connect((line,int(i)))
					log2.write(str(line)+'\t\t\t'+str(i)+'\t\t On')
					print '\t\t\t'+str(i)+'\t\t On'
				except socket.error:
					log2.write(str(line)+'\t\t\t'+str(i)+'\t\t Off')
					print '\t\t\t'+str(i)+'\t\t Off'
					s.close()
	except KeyboardInterrupt:pass

def range_ip_proc_():
	try:
		global ips
		for i in range(len(ip2)):
			t = int(ip2[i])
			ip3.append(t)
		for i in range(10000000):
			ips=('%d.%d.%d.%d')%(ip3[0],ip3[1],ip3[2],ip3[3])
			log.write(ips+"\n")
			if ips==end:
				log.close()
				break
			ip3[3]+=1
			if ip3[3]==256:
				if ip3[2] < 256:	
					ip3[3]=0
					ip3[2]+=1
			if ip3[2]==256:
				if ip3[1] < 256:
					ip3[2]=0
					ip3[1]+=1
			if ip3[1]==256:
				if ip3[0]< 255:
					ip3[1]=0
					ip3[0]+=1
		ip_port_proc_()
	except KeyboardInterrupt:pass
if __name__=='__main__':data_in()			
