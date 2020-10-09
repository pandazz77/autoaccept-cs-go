from PIL import Image, ImageGrab
from time import sleep
import pyautogui
import keyboard
from playsound import playsound
import webcolors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

requested_colour = (250,175,100)
actual_name, closest_name = get_colour_name(requested_colour)

while True:
	keyboard.wait('Ctrl + 1')
	playsound('start.mp3')
	while True:
		image = pyautogui.screenshot()
		(width, height) = image.size
		width, height = round(width/2),round((height/2)*1.12)
		color = image.getpixel((width, height))
		sleep(2)
		actual_name, closest_name = get_colour_name(color)
		if 'green' in closest_name:
			pyautogui.click(x=width, y=height)
		elif keyboard.is_pressed('Ctrl + 2'):
			playsound('end.mp3')
			break
