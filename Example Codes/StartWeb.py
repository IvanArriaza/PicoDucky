#This code was written with the purpose of understanding how this hid oriented librarys work. I use an Spanish keyboard layout, which you can easily get. 

import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from keyboard_layout_win_es import KeyboardLayout


kb=Keyboard(usb_hid.devices)
ly=KeyboardLayout(kb)

#Open CMD
kb.send(Keycode.WINDOWS)
kb.send(Keycode.C,Keycode.M,Keycode.D)
time.sleep(0.5)
kb.press(Keycode.ENTER)
kb.release_all()

#CMD command
time.sleep(0.5)
ly.write("start https://netflix.com")
kb.press(Keycode.ENTER)
kb.release_all()

#Exit CMD
time.sleep(1)
kb.send(Keycode.ALT,Keycode.TAB)
ly.write("exit")
kb.press(Keycode.ENTER)
kb.release_all()

#As You can see, It simply opens the netflix main webpage upon plugin the device in.
