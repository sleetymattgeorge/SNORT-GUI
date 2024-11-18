import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import ImageTk, Image
snort=tk.Tk()
snort.title('ABOUT')
snort.geometry('600x515')
tc='''
 SNORT-GUI is a Open Source Application developed by WhiteHatCyberus  for enterprise intrusion detection systems and cyber-forensic        analysis.
 --------------------------------------------------------------------

        ,,_     -*> Snort! <*-
        o"  )~   Version 2.9.15.1 GRE (Build 15125) 
        """"    By Martin Roesch & The Snort Team: 

                http://www.snort.org/contact#team

                Copyright (C) 2014-2019 Cisco and/or its affiliates. 
                All rights reserved.
                
                Copyright (C) 1998-2013 Sourcefire, Inc., et al.
                -------------------------------------------------
                Using libpcap version 1.10.1 (with TPACKET_V3)
                Using PCRE version: 8.39 2016-06-14
                Using ZLIB version: 1.2.11

'''
################################3
# create a canvas to display the background image
canvas = tk.Canvas(snort, width=600, height=515)
canvas.pack(fill=tk.BOTH, expand=True)

# load and display the background image

img = Image.open('.resources/info/images/snort_about.jpg')
img = img.resize((600, 515), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor=tk.NW)

###################################################3

T=scrolledtext.ScrolledText(snort,width=69, height=28)
T.insert(tk.INSERT,tc)
T.config(state='disabled')
# place the text widget on top of the image
canvas.create_window( 15, 10, anchor=tk.NW, window=T)

snort.resizable(False, False)
snort.mainloop()
