from mcpi.minecraft import Minecraft
import pyautogui as pag
import time
from sense_hat import SenseHat
sh = SenseHat()

#unpresses all the keys
def unpress():
    for key in ['s', 'w', 'a', 'd']:
        pag.keyUp(key)

#presses the correct key
def move(direction):
    unpress()
    pag.keyDown(direction)

#the arrow
def displayArrow(c,rot):
    arrow = [
        e,e,e,c,c,e,e,e,
        e,e,c,c,c,c,e,e,
        e,c,c,c,c,c,c,e,
        c,c,e,c,c,e,c,c,
        c,e,e,c,c,e,e,c,
        e,e,e,c,c,e,e,e,
        e,e,e,c,c,e,e,e,
        e,e,e,c,c,e,e,e]
    sh.set_rotation(rot)
    sh.set_pixels(arrow)

#define the colors
r = [255,0,0]
e = [0,0,0]
g = [0,255,0]
b = [0,0,255]
stop = [ # the stop sign
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r]

mot = 'SSSS'
while True: #main loop
    x,y,z = sh.get_accelerometer_raw().values()
    x = round(x, 0)
    y = round(y, 0) 
    if x == -1 and abs(y) == 0 and mot != 'rrrr':
        displayArrow(b, 270)
        move('a') # right
        mot = 'rrrr'
    elif x == 1 and abs(y) == 0 and mot != 'llll':
        displayArrow(b, 90)
        move('d') #left
        mot = 'llll'
    elif y == -1 and mot != 'wwww':
        displayArrow(g, 0)
        move('w') #fwd
        mot = 'wwww'
    elif y == 1 and mot != 'bbbb':
        displayArrow(g, 180)
        move('s') #back
        mot = 'bbbb'
    elif abs(x) == 0 and abs(y) == 0:
        unpress() # stop
        sh.set_pixels(stop)
        mot = 'SSSS'