### Author: EMF Badge team
### Description: Change WiFi settings
### Category: Settings
### License: MIT
### Appname : Wifi

import buttons
from dialogs import *
from database import *
import ugfx

ugfx.init()
width = ugfx.width()
height = ugfx.height()
buttons.init()

cursor_loc = 0

sty = ugfx.Style()

def _move_arrow(x, backcolour, win):
	global cursor_loc
	arrow = [[0,0],[20,7],[0,14],[4,7]]
	win.fill_polygon(4, cursor_loc*25+18, arrow , backcolour)
	cursor_loc += x
	if cursor_loc < 0:
		cursor_loc = 0
	if cursor_loc > 2:
		cursor_loc = 2
	win.fill_polygon(4, cursor_loc*25+18, arrow ,ugfx.RED)


# Create visual elements
win_header = ugfx.Container(0,0,width,33)
win_main = ugfx.Container(0,35,width,height-35)

components = [win_header, win_main]
ugfx.set_default_font(ugfx.FONT_TITLE)
components.append(ugfx.Label(3,3,width-10,29,"Wifi Settings",parent=win_header))
ugfx.set_default_font(ugfx.FONT_MEDIUM_BOLD)
components.append(ugfx.Label(40,10,85,25,"Name:",parent=win_main))
components.append(ugfx.Label(40,35,85,25,"Password:",parent=win_main))
ugfx.set_default_font(ugfx.FONT_MEDIUM)
lname = ugfx.Label(125,10,100,25,"BadgeNet",parent=win_main)
lpwd = ugfx.Label(125,35,100,25,"letmein",parent=win_main)
components.append(lname)
components.append(lpwd)
ckdefault = ugfx.Checkbox(40,65,250,25,"EMF camp default",parent=win_main)
components.append(ckdefault)

win_main.show()
win_header.show()

ap = ""
pwd = ""
try:
	de = wifi.connection_details()
	ap = de["ssid"]
	pwd = de["pw"]
except:
	pass

try:

	_move_arrow(0, sty.background(), win_main)

	while True:

		if buttons.is_triggered("BTN_B"):
			break

		if buttons.is_triggered("BTN_A"):
			if cursor_loc == 0:
				new_ap = prompt_text("Enter the access point name", init_text = ap, width = 310, height = 220)
				if new_ap:
					ap = new_ap
					lname.text(ap)
			if cursor_loc == 1:
				new_pwd = prompt_text("Enter the password", init_text = pwd, width = 310, height = 220)
				if new_pwd:
					pwd = new_pwd
					lpwd.text(pwd)
			_move_arrow(0, sty.background(), win_main)

		if buttons.is_triggered("JOY_UP"):
			_move_arrow(-1,sty.background(),win_main)
			ckdefault.detach_input(ugfx.BTN_A)

		if buttons.is_triggered("JOY_DOWN"):
			_move_arrow(1,sty.background(),win_main)
			if cursor_loc == 2:
				ckdefault.attach_input(ugfx.BTN_A,0)


finally:
	for component in components:
		component.destroy()
