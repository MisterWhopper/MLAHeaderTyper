import keyboard as kb # see repo on GitHub
import datetime
from time import sleep

TRIGGER_WORD_HEADER = "%mlaheader%"
TRIGGER_WORD_CITATION = "%mlacitation%"
name = "MisterWhopper" # replace this name with whatever your name is

def MLA_HEADER():
    global name, TRIGGER_WORD_HEADER # make sure these are imported properly
    sleep(.25) # give us a little bit of breathing room
    for _ in range(len(TRIGGER_WORD_HEADER) + 1): 
        sleep(.015)
        kb.press("backspace") # erase the trigger word using backspace, including the leading space
    kb.write(name) # type out the name specified above
    kb.press("enter") # whitespace
    kb.write("<PROFESSOR NAME>") # type this exact string; the user can replace this themselves
    kb.press("enter") # whitespace
    kb.write("<CLASS TITLE>") # type this exact string; the user can replace this themselves
    kb.press("enter")
    date = datetime.datetime.now().strftime("%B %d, %Y") # get the current date
    date = date.split(" ") # some formatting
    date[1] = date[1].replace("0","") # some formatting
    date = ''.join(d + " " for d in date) # yet more formatting
    kb.write(date) # type the date
    kb.press("enter") # whitespace

def MLA_CITATION():
    sleep(.25) # give us some breathing room
    for _ in range(len(TRIGGER_WORD_CITATION) + 1):
        sleep(.025)
        kb.press("backspace") # erase the trigger word using backspace, including the leading space
    kb.write("(<AUTHOR> <PAGE NUMBER>). ") # type this exact string; the user can replace this themselves

# hook our function to run when the trigger word is typed
kb.add_word_listener(TRIGGER_WORD_HEADER,MLA_HEADER) 
kb.add_word_listener(TRIGGER_WORD_CITATION,MLA_CITATION)
# listen for these words forever or until the user presses the following shortcut
kb.wait("windows + ctrl + esc")
