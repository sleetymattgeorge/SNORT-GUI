import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from PIL import ImageTk, Image
import webbrowser


snort = tk.Tk()
snort.title('Help')
snort.geometry("950x700")


# setting up canvas for bg image
canvas = tk.Canvas(snort, width=900, height=700)
canvas.pack(fill=tk.BOTH, expand=True)

# display bg image
img = Image.open(".resources/images/snort1.png")
img = img.resize((950, 700), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, image=img, anchor=tk.NW)

img1 = Image.open(".resources/images/snort2.png")
img1 = img1.resize((300, 200), Image.Resampling.LANCZOS)
img1 = ImageTk.PhotoImage(img1)

sn1 = Image.open(".resources/images/sh1.png")
sn1 = sn1.resize((500, 400), Image.Resampling.LANCZOS)
sn1 = ImageTk.PhotoImage(sn1)

sn2 = Image.open(".resources/images/sh2.png")
sn2 = sn2.resize((500, 400), Image.Resampling.LANCZOS)
sn2 = ImageTk.PhotoImage(sn2)

sn3 = Image.open(".resources/images/sh3.png")
sn3 = sn3.resize((500, 400), Image.Resampling.LANCZOS)
sn3 = ImageTk.PhotoImage(sn3)

sn4 = Image.open(".resources/images/sh4.png")
sn4 = sn4.resize((500, 400), Image.Resampling.LANCZOS)
sn4 = ImageTk.PhotoImage(sn4)

sn5 = Image.open(".resources/images/sh5.png")
sn5 = sn5.resize((500, 400), Image.Resampling.LANCZOS)
sn5 = ImageTk.PhotoImage(sn5)

sn6 = Image.open(".resources/images/sh6.png")
sn6 = sn6.resize((500, 400), Image.Resampling.LANCZOS)
sn6 = ImageTk.PhotoImage(sn6)

sn7 = Image.open(".resources/images/sh7.png")
sn7 = sn7.resize((500, 400), Image.Resampling.LANCZOS)
sn7 = ImageTk.PhotoImage(sn7)

sn8 = Image.open(".resources/images/sh8.png")
sn8 = sn8.resize((500, 400), Image.Resampling.LANCZOS)
sn8 = ImageTk.PhotoImage(sn8)

def callback(url):
   webbrowser.open_new_tab(url)

def getting_started():
    HELP1 = '''
    Snort is the foremost Open Source Intrusion Prevention System (IPS)
    in the world. Snort IPS uses a series of rules that help define malicio
    -us network activity and usesthose rules to find packets that match aga
    -inst them and generates alerts for users.Snort can be deployed inline 
    to stop these packets, as well.

    Snort has three primary uses: As a packet sniffer like tcpdump, as a 
    packet logger — which is useful for network traffic debugging, or it c
    an be used as a full-blown network intrusion prevention system. Snort 
    can be downloaded and configured for personal and business use alike.

    Snort GUI is an application interface developed for everyone who has ju
    -st started using snort. Snort GUI simplifies the writing of rules for 
    the IDS through an API and able to run on both windows and linux. 
    For more information, the Snort Community website:

     ''' 
    st = ScrolledText(snort, width=75, height=30)
    st.place(x=300, y=100)
    st.tag_config('title', font=('Arial', 20, 'bold'), foreground='black',underline=TRUE)
    st.insert('end', '\nGETTING STARTED WITH SNORT\n', ('title', 'black','center'))
    st.tag_configure('center', justify='center')
    link="                  CLICK HERE TO VISIT COMMUNITY WEBSITE"
    text_with_link = f"{HELP1}{link}"
    st.insert(tk.END, text_with_link)
    st.image_create(tk.INSERT, image=img1, padx=180, pady=20)

    st.tag_add("hyperlink", "end-{}c".format(len(link)+2),"20.60")
    st.tag_config("hyperlink", foreground="blue")
    st.tag_bind("hyperlink", "<Enter>", lambda event: st.tag_config("hyperlink", foreground="red"))
    st.tag_bind("hyperlink", "<Leave>", lambda event: st.tag_config("hyperlink", foreground="blue"))
    st.tag_bind("hyperlink", "<Button-1>", lambda event: webbrowser.open("https://www.snort.org/#documents"))
    st.configure(state='disabled')

def doc():
    HELP2 = '''             
    1. Snort User Manual - Comprehensive guide to Snort usage and configura       -tion.
    2. Snort Rule Writing - Guide to creating custom Snort rules.
    3. Snort FAQs - Frequently asked questions about Snort.

    For more information, refer to the Snort website.

'''

    st = ScrolledText(snort, width=75, height=30)
    st.place(x=300, y=100)
    st.tag_config('title', font=('Arial', 20, 'bold'), foreground='black')
    st.insert('end', '\nSNORT DOCUMENTATION\n', ('title', 'black','center'))
    st.tag_configure('center', justify='center')
    link1="             CLICK HERE TO VISIT DOCUMENTATION"
    text_with_link1 = f"{HELP2}{link1}"
    st.insert(tk.END, text_with_link1)
    st.image_create(tk.END, image=img1,padx=100,pady=20)
   
    st.tag_add("hyperlink", "end-{}c".format(len(link1)+2), "10.46")
    st.tag_config("hyperlink", foreground="blue")
    def on_enter(event):
        st.tag_config("hyperlink", foreground="red")

    def on_leave(event):
        st.tag_config("hyperlink", foreground="blue")
    def open_link(event):
     webbrowser.open("http://books.gigatux.nl/mirror/snortids/0596006616/snortids-CHP-5.html")
    st.tag_bind("hyperlink", "<Enter>", on_enter)
    st.tag_bind("hyperlink", "<Leave>", on_leave)
    st.tag_bind("hyperlink", "<Button-1>", open_link)
    st.configure(state='disabled')
def use():
    T1="USING SNORT GUI"
    HELP3 = '''
    1. Open terminal and go to snortgui folder.

    2. Run the command "sudo python3 snortgui.py".

    3. Enter the admin password that was previously set and press ok.

    4. Click on generate rules and enter addmin password.
    
    5. To set the appropriate rules and click generate rule.
    
    6. Save them as a .rule file by pressing options and save as.

    7. Click Run Snort to run the ids in the background.

    8. Enter the time in hours ,select network interface from the dropdown
       menu.

    9. Select the .conf file and click on run snort.

    10. After the set time selct log analyzer and select the log you want.
    
    11. Click on the protocol and if its not icmmp protocol click on the 
        port.
    12.(Optional)Select configuration file to add changes manually.    

'''


    st = ScrolledText(snort, width=75, height=30)
    st.place(x=300, y=100)
    st.tag_config('title', font=('Arial', 20, 'bold'), foreground='black',underline=TRUE)
    st.insert('end', '\nUSING SNORT GUI\n', ('title', 'black','center'))
    st.tag_configure('center', justify='center')
    st.insert(tk.INSERT, HELP3)
    st.image_create(10.0, image=sn1,padx=50,pady=20)
    st.image_create(12.0, image=sn2,padx=50,pady=20)
    st.image_create(16.0, image=sn3,padx=50,pady=20)
    st.image_create(18.0, image=sn4,padx=50,pady=20)
    st.image_create(22.0, image=sn5,padx=50,pady=20)
    st.image_create(25.0, image=sn6,padx=50,pady=20)
    st.image_create(27.0, image=sn7,padx=50,pady=20)
    st.image_create(29.0, image=sn8,padx=50,pady=20)
    st.configure(state='disabled')

# add widgets here
b1 = tk.Button(text='Getting started with snort', command=getting_started)
b1.place(x=70, y=150)
b2 = tk.Button(text='Important Documentation', command=doc)
b2.place(x=70, y=200)
b3 = tk.Button(text='Snort GUI(How to use)', command=use)
b3.place(x=70, y=250)

snort.resizable(False, False)
snort.mainloop()
