import os
import shutil
import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog


def prompt_password():
    return simpledialog.askstring(
        "Setting up",
        "\nCreate your SNORT administrator password: \n\n"
        "(Note: Once set, it cannot be changed. This should ideally match your Linux sudo password if you intend to allow package installs.)",
        show='*'
    )


def setup_resources(password):
    try:
        os.makedirs(".resources/temp", exist_ok=True)

        # Copying 'alert' folder to current working directory
        if os.path.exists(".resources/alert"):
            shutil.copytree(".resources/alert", "./alert", dirs_exist_ok=True)

        # Store password (ideally this should be hashed, but here it's stored as-is for compatibility)
        with open(".resources/temp/admin.pass", "w") as f:
            f.write(password)

        return True
    except Exception as e:
        messagebox.showerror("Setup Error", f"Failed to set up resources:\n{e}")
        return False


def show_terms_and_conditions():
    snort = tk.Tk()
    snort.geometry('600x420+100+100')
    snort.title('Terms and Conditions')

    terms = '''
You are using the SNORT GUI developed by White Hat Cyberus!
Developed by 4 students from Rajagiri School of Engineering and 
Technology. This is an Open Source Software — feel free to 
check out the code.

GitHub: https://github.com/WhiteHatCyberus

⚠ Disclaimer:
To be used for personal, educational, and enterprise purposes. 

What is SNORT?  
SNORT is an Open Source Intrusion Detection System / Intrusion 
Prevention System maintained by Cisco Talos.

            T&C
         ---------

1. Use this software at your own risk.
2. The authors of this software are not responsible for any 
   damages caused by this software.
3. This software is provided "as is" without warranty of any 
   kind, express or implied.
4. By using this software, you agree to these terms and conditions.

Note: This application will monitor your network in real time and 
access your administrative directories. For proper functioning, 
run the application in 'sudo' mode.

⚠ Manipulating this application for malicious purposes is not 
entertained.
    '''

    def agree():
        if messagebox.askokcancel("Agreement", "By clicking OK, you agree to the T&C."):
            snort.destroy()
            os.system("python3 .resources/resources.py")

    def disagree():
        if not messagebox.askyesno("Decline", "Application needs T&C agreement to continue. Quit?"):
            return
        snort.destroy()

    # Display terms
    T = scrolledtext.ScrolledText(snort, width=70, height=20)
    T.insert(tk.INSERT, terms)
    T.configure(state="disabled")
    T.pack(pady=20)

    # Buttons
    tk.Button(snort, text="Agree", command=agree, bg="#000", fg="#fff", cursor="hand2", relief="groove",
              activebackground="grey72", activeforeground="#fff").place(x=430, y=380)

    tk.Button(snort, text="Disagree", command=disagree, bg="#000", fg="#fff", cursor="hand2", relief="groove",
              activebackground="grey72", activeforeground="#fff").place(x=500, y=380)

    snort.resizable(False, False)
    snort.mainloop()


if __name__ == "__main__":
    password = prompt_password()
    if password is None:
        exit()
    elif not password.strip():
        messagebox.showerror("Input Error", "Password cannot be empty.")
        exit()
    elif setup_resources(password):
        show_terms_and_conditions()
