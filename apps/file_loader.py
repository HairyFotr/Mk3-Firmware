import ugfx
import os
import pyb

def callback_button(line):
	global stay_here
	stay_here = 0
	print("Quitting")

def main():
	wi = ugfx.width()
	hi = ugfx.height()

	win_header = ugfx.Container(0,0,wi,30)
	win_files = ugfx.Container(0,33,int(wi/2),hi-33)
	win_preview = ugfx.Container(int(wi/2)+2,33,int(wi/2)-2,hi-33)


	ugfx.set_default_font("D*")
	title = ugfx.Label(3,3,wi-10,29,"Choose File",win_header)


	ugfx.set_default_font("c*")
	options = ugfx.List(3,3,win_files.width()-6,win_files.height()-6,win_files)

	btn_ok = ugfx.Button(10,win_preview.height()-25,20,20,"A",win_preview)
	l_ok = ugfx.Label(35,win_preview.height()-25,100,20,"Run",win_preview)

	btn_back = ugfx.Button(10,win_preview.height()-50,20,20,"B",win_preview)
	l_back = ugfx.Label(35,win_preview.height()-50,100,20,"Back",win_preview)

	btn_menu = ugfx.Button(10,win_preview.height()-75,20,20,"M",win_preview)
	l_back = ugfx.Label(35,win_preview.height()-75,100,20,"Pin",win_preview)


	win_header.show()
	win_files.show()
	win_preview.show()


	folders = os.listdir("/flash/apps")
	for folder in folders:
		try: #is there a better way of doing this in upy?
			appfiles = os.listdir("/flash/apps/" + folder)
			if ((folder+".py") in appfiles):
				options.add_item(folder)
		except:
			2+2
			#ignore and continue
	
	
	#files = os.listdir()

	#for f in files:
	#	if f.endswith(".py"):
	#		options.add_item(f)

	options.attach_input(ugfx.JOY_UP,0)
	options.attach_input(ugfx.JOY_DOWN,1)
	#btn_menu.attach_input(ugfx.BTN_MENU)
	#btn_ok.attach_input(ugfx.BTN_A)

	

	tgl_menu = pyb.Pin("BTN_MENU", pyb.Pin.IN)
	extint = pyb.ExtInt(tgl_menu, pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP, callback_button)

	stay_here = 1;

	while(stay_here):
		pyb.wfi()
	extint = pyb.ExtInt(tgl_menu, pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP, None)
	
	
	win_header.dispose()
	win_files.dispose()
	win_preview.dispose()
	title.dispose()
	options.dispose()
	btn_ok.dispose()
	l_ok.dispose()
	btn_back.dispose()
	l_back.dispose()
	btn_menu.dispose()
	l_back.dispose()
		
		