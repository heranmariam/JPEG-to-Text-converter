import keyboard
import time
import random
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
fpath='C:\\Users\heran\OneDrive\Desktop\\500 ST Images Workload\\'
fname="4095.JPEG"
this=pytesseract.image_to_string(Image.open(fpath+fname))
this=this.replace("\n\n","\n")
this=this.replace("|","I")
time.sleep(3)
keyboard.write(this,delay=random.uniform(0.03,0.07))
# keyboard.press_and_release('ctrl+s')
# keyboard.write(fname)
# keyboard.press_and_release("enter")
