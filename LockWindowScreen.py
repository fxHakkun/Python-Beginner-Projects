'''This is a code to just put screen on your desktop and freeze your keyboard input. It can be cancelled by just click on Done? button on edge.
Why doing this? My nephew just love touch my pc, and to avoid anything happened. Let's just do this LOL

Btw This code is combination of snippets I found and just combine altogether. I adjust something and hence the result. Sorry if it's messy(Im not sure if it is)
'''

import tkinter as tk
import random
import pynput

def foo():
    pass

root = tk.Tk()

picture = ["1699305751985.png", "1699305041539.png", "1699305912325.png"] #put image files in your directory and put the name in this.
# Now it will look for the image in the specified directory
bg = tk.PhotoImage(file= random.choice(picture))

label1 = tk.Label( root, image = bg) 
label1.place(x = 0,y = 0) 

root.attributes("-fullscreen", True, "-topmost", True,)
root.protocol("WM_DELETE_WINDOW", foo)

but = tk.Button(root, text = "Done?", command=root.destroy)
but.grid()

#Disable keyboard events
keyboard_listener = pynput.keyboard.Listener(suppress=True)
keyboard_listener.start()

root.mainloop()