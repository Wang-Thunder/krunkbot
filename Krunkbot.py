from tkinter.messagebox import YES
import pyautogui as pag
import random

pag.PAUSE = 1

title = "Autotoon's Krunkinator 5000"



delay = pag.prompt(title=title,text='Enter number of seconds between keypresses. Please use AT LEAST 2 seconds.')
keypress = pag.prompt(title=title, text='Select a keypress. The Krunkinator will press this key')


pag.confirm(title=title, text="Put your beer in hotkey slot [" + keypress + "] The Krunkinator will press this key every [" + delay + "] seconds." "\n" "To stop the Krunkinator, press CTRL + C" "\n" "Are you prepared to get krunk every [" + delay + "] seconds?", buttons=['Yes', 'No'])

while YES:
    pag.press(keypress, interval=delay)