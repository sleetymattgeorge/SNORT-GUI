import os
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from PIL import ImageTk, Image

# Global password reuse
stored_pass_path = '.resources/temp/admin.pass'
if not os.path.exists(stored_pass_path):
    messagebox.showerror("Error", "Admin password not found. Please reconfigure the app.")
    exit()

with open(stored_pass_path, 'r') as file:
    sudo_passwd = file.read().strip()

# GUI password validation
max_attempts = 3
for attempt in range(max_attempts):
    sudo_password = simpledialog.askstring("Authentication", "Enter your administrator password:", show='*')

    if sudo_password is None:
        exit()
    elif sudo_password == "":
        messagebox.showerror("Error", "Enter password")
    elif sudo_password == sudo_passwd:
        break
    else:
        messagebox.showerror("Error", f"ⓘ Incorrect password. Attempts left: {max_attempts - attempt - 1}")
else:
    messagebox.showerror("Access Denied", "Too many incorrect attempts. Exiting.")
    exit()


# -------------- GUI Starts ----------------
try:
    root = tk.Tk()
    root.title('SNORT IDS GUI - w/❤ by WhiteHatCyberus')
    root.geometry('1200x650+100+50')
    root.resizable(False, False)

    # Canvas for background image
    canvas = tk.Canvas(root, width=1200, height=650)
    canvas.pack(fill=tk.BOTH, expand=True)

    try:
        img = Image.open('.resources/info/images/snort.jpg')
        img = img.resize((1200, 650), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, image=img, anchor=tk.NW)
    except Exception as e:
        messagebox.showwarning("Image Load Error", f"Could not load background image: {e}")

    # --- Functions ---
    def run_with_sudo(command):
        try:
            process = subprocess.Popen(
                f"sudo -S {command}",
                shell=True,
                stdin=subprocess.PIPE,
                preexec_fn=os.setsid
            )
            process.stdin.write(sudo_password.encode('utf-8') + b'\n')
            process.stdin.flush()
        except Exception as e:
            messagebox.showerror("Execution Error", str(e))

    def generate_rules():
        run_with_sudo("python3 .resources/rule_generator.py")

    def open_files():
        filename = filedialog.askopenfilename(
            initialdir='/etc/snort/rules/',
            title='Select File',
            filetypes=(('SNORT Rules', '*.rules'), ('Config Files', '*.conf'))
        )
        if filename:
            run_with_sudo(f"gedit '{filename}'")

    def run_ids():
        run_with_sudo("python3 .resources/run_ids.py")

    def log_analyser():
        run_with_sudo("python3 .resources/loganalyzer.py")

    def about():
        os.system("python3 .resources/about.py")

    def help():
        os.system("python3 .resources/help.py")

    def exit_app():
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            root.destroy()

    # --- Buttons ---
    btn_opts = {
        'width': 20, 'height': 2, 'font': ('TkDefaultFont', 15),
        'bg': '#000', 'fg': '#fff', 'relief': 'groove', 'cursor': 'hand2',
        'activebackground': '#f00', 'activeforeground': '#fff'
    }

    tk.Button(root, text='GENERATE RULES', command=generate_rules, **btn_opts).place(x=45, y=100)
    tk.Button(root, text='CONFIGURATION FILES', command=open_files, **btn_opts).place(x=45, y=225)
    tk.Button(root, text='LOG ANALYZER', command=log_analyser, **btn_opts).place(x=45, y=350)
    tk.Button(root, text='RUN SNORT', command=run_ids, **btn_opts).place(x=45, y=475)

    # --- Menu ---
    menu_bar = tk.Menu(root)

    option_menu = tk.Menu(menu_bar, tearoff=0)
    option_menu.add_command(label='Help', command=help)
    option_menu.add_command(label='Exit', command=exit_app)
    menu_bar.add_cascade(label='Options', menu=option_menu)

    about_menu = tk.Menu(menu_bar, tearoff=0)
    about_menu.add_command(label='SNORT-GUI', command=about)
    menu_bar.add_cascade(label='About', menu=about_menu)

    root.config(menu=menu_bar)
    root.mainloop()

except tk.TclError:
    exit()
