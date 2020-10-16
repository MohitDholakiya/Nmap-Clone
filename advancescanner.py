#!/usr/bin/python
from termcolor import colored
from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost,tgtPort))
		print ('[+] %d /tcp Open' %tgtPort)
	except:
		print ('[+] %d /tcp Closed' %tgtPort)
	finally:
		sock.close()
def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print ('Unknown Host %s ' %tgtHost)
	try:
		tgtName = gethostbyaddr(tgtIP)
		print ('[+} Scan Results for:' + tgtName[0])
	except:
		print ('[+] Scan Results for:' + tgtIP)
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()
def main():
	parser = optparse.OptionParser('Usage of program: ' + '-H <targe host> -p <target ports>')
	parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
	parser.add_option('-p', dest = 'tgtport', type = 'string', help = 'specify target ports seperated by comma')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtport).split(',')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print (parser.usage)
		exit(0)
	portScan(tgtHost,tgtPorts)
if __name__ ==  '__main__':
	main()
