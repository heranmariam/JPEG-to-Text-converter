import keyboard
import time
import random
from PIL import Image
import pytesseract

# creates a pytesseract objects
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# file path
fpath='C:\\Users\heran\OneDrive\Desktop\\500 ST Images Workload\\'
# file name
fname="filename.JPEG"

# open image by PIL_image
# feed the image to pytesseract
this=pytesseract.image_to_string(Image.open(fpath+fname))

# repalce misspelled chrachters 
this=this.replace("\n\n","\n") # \n\n with \n
this=this.replace("|","I")     # | with I

time.sleep(3)

# Add randomness between words
# this makes the Typing more humanly
keyboard.write(this,delay=random.uniform(0.03,0.07))

# uncomment the following section to save the file automatically
# press control + S to save
# keyboard.press_and_release('ctrl+s')
# enter the file name
# keyboard.write(fname)4
# press enter to save the file
# keyboard.press_and_release("enter")
