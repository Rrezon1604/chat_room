import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox, font
import os

# ======================================== CHAT PAGE ================================================


def chat_page():

    def back_to_home():
        chat_root.destroy()
        home()

    email = email_login
    with open('users.csv', 'r') as file:
        a = file.readlines()
        for i in a:
            data = i.split()
            if email in data:
                username = f'{data[2]} {data[4]}'

    def load_messages():
        if os.path.exists('messages.txt'):
            with open('messages.txt', 'r') as file:
                messages = file.readlines()
            return [message.strip() for message in messages]
        return []

    def save_message(username, message):
        with open('messages.txt', 'a') as file:
            file.write(f"{username} : {message}\n")

    def wrap_text(text, width):
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + len(current_line) > width:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)
        lines.append(" ".join(current_line))
        return lines

    def add_message(event=None):
        message = entry_message.get()
        if username and message:
            formatted_message = f"{username} : {message}"
            wrapped_message = wrap_text(formatted_message, 140)
            for line in wrapped_message:
                listbox.insert(tk.END, line)
                listbox.itemconfig(tk.END, {'bg': '#489C54', 'fg': 'white'})
            listbox.insert(tk.END, "")
            save_message(username, message)
            entry_message.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Message cannot be empty!")

    num_users = 1
    with open('users.csv', 'r') as file:
        num_lines = file.readlines()
        for line in num_lines:
            if line.startswith(str(num_users)):
                num_users += 1
                participants_num = num_users - 1

    chat_root = tk.Tk()
    chat_root.title("Chat Application")
    chat_root.state('zoomed')

    custom_font = font.Font(family="Helvetica", size=12)

    chat_root.configure(bg="#D8D8D8")

    header_frame = tk.Frame(chat_root, bg="#336699", pady=10)
    header_frame.pack(fill=tk.X)

    header_label = tk.Label(header_frame, text="Welcome to Our Chat",
                            font=("Helvetica", 25), fg="white", bg="#336699")
    header_label.pack()

    participants = tk.Label(chat_root, text=f'Participants: {participants_num} Users',
                            font=(custom_font, 15), bg='#D8D8D8', fg='black')
    participants.pack()

    frame_messages = tk.Frame(chat_root, bg="#ffffff")
    frame_messages.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(frame_messages)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame_messages, width=100, height=20,
                         yscrollcommand=scrollbar.set, font=(custom_font, 15))
    listbox.pack(fill=tk.BOTH, expand=True)

    scrollbar.config(command=listbox.yview)

    messages = load_messages()
    for message in messages:
        wrapped_message = wrap_text(message, 140)
        for line in wrapped_message:
            listbox.insert(tk.END, line)
        listbox.insert(tk.END, "")

    frame_input = tk.Frame(chat_root, bg="#f0f0f0")
    frame_input.pack(pady=10)

    label_username = tk.Label(
        frame_input, text="Username:", bg="#f0f0f0", font=(custom_font, 15))
    label_username.pack(side=tk.LEFT, padx=10)

    entry_username = tk.Label(
        frame_input, text=username, width=20, font=(custom_font, 15))
    entry_username.pack(side=tk.LEFT, padx=10)

    entry_message = tk.Entry(chat_root, width=80, font=(custom_font, 15))
    entry_message.pack(pady=10)

    send_button = tk.Button(chat_root, text="Send", command=add_message,
                            font=(custom_font, 15), bg="#336699", fg="white", pady=5, width=20)
    send_button.pack()

    space = tk.Label(chat_root, text='', height=1, bg='#D8D8D8')
    space.pack()

    logut_button = tk.Button(chat_root, text='Logout', command=back_to_home,
                             font=(custom_font, 15), bg="red", fg="white", pady=5, width=20)
    logut_button.pack()

    chat_root.bind('<Return>', add_message)

    chat_root.mainloop()


# =====================================================================================================


# ============================================= LOGIN PAGE ===========================================

def login_form():

    def go_to_chat():
        login_root.destroy()
        chat_page()

    def start_chat(event=None):
        global email_login
        email_login = email_entry.get()
        password_login = password_entry.get()

        with open('users.csv', 'r') as file:
            a = file.readlines()
            for i in a:
                data = i.split()
                if email_login in data and password_login in data:
                    messagebox.showinfo('Shenim!', f'Welcome {
                                        data[2]} {data[4]}')
                    go_to_chat()
                    break
            else:
                messagebox.showerror(
                    'Shenim!', 'Keni gabuar email-in ose password-in!!!')

    def back_to_home():
        login_root.destroy()
        home()

    global login_root
    login_root = tk.Tk()
    login_root.title('Login')
    login_root.state('zoomed')
    login_root.config(bg='darkorchid')

    space = tk.Label(login_root, text='', height=1, bg='darkorchid')
    space.pack()

    frame = tk.Frame(login_root)
    frame.pack()

    frame1 = tk.Frame(frame)
    frame1.grid(row=0, column=0, padx=(200, 0))

    image_frame = tk.Frame(frame)
    image_frame.grid(row=0, column=1, padx=(150, 150))

    space = tk.Label(image_frame, text='')
    space.pack()

    img = tk.PhotoImage(file='Capture3.PNG')
    image_label = tk.Label(image_frame, image=img)
    image_label.pack()

    space1 = tk.Label(frame1, text='', height=15)
    space1.pack()

    login_label = tk.Label(frame1, text='LOGIN', font=('Arial', 30))
    login_label.pack()

    line = tk.Canvas(frame1, height=5, highlightthickness=0,
                     bg='purple', width=400)
    line.pack()

    space2 = tk.Label(frame1, text='', height=2)
    space2.pack()

    frame2 = tk.Frame(frame1)
    frame2.pack()

    email_label = tk.Label(frame2, text='Email:', font=('Arial', 15))
    email_label.grid(row=0, column=0, padx=(0, 35))
    email_entry = tk.Entry(frame2, font=('Arial', 15))
    email_entry.grid(row=0, column=1, padx=(10, 0))

    space3 = tk.Label(frame2, text='', height=1)
    space3.grid(row=1)

    password_label = tk.Label(frame2, text='Password:', font=('Arial', 15))
    password_label.grid(row=2, column=0)
    password_entry = tk.Entry(frame2, font=('Arial', 15), show='*')
    password_entry.grid(row=2, column=1, padx=(10, 0))

    space4 = tk.Label(frame1, text='', height=5)
    space4.pack()

    sign_in_button = tk.Button(frame1, text='SIGN IN', font=('Arial', 15),
                               width=30, bg='purple', fg='white', command=start_chat)
    sign_in_button.pack()

    space5 = tk.Label(frame1, text='', height=2)
    space5.pack()

    back_button = tk.Button(frame1, text='BACK', font=('Arial', 15), bg='red', width=30,
                            fg='white', command=back_to_home)
    back_button.pack()

    space6 = tk.Label(frame1, text='', height=10)
    space6.pack()

    login_root.bind('<Return>', start_chat)

    login_root.mainloop()

# ======================================================================================================


# ========================================= SIGNUP PAGE ===============================================

def signup_form():

    def back_to_home():
        signup_root.destroy()
        home()

    def create_acc(event=None):
        first_name = firstname_entry.get()
        last_name = lastname_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        i = 1
        if first_name == '' or last_name == '' or email == '' or password == '' or confirm_password == '':
            messagebox.showerror(
                'Shenim!', 'Ju lutem plotesoni te gjitha fushat!!!')
        else:
            if '@' not in email:
                messagebox.showerror(
                    'Shenim!', 'Ju lutem shtoni "@" ne email-in tuaj!!!')
            elif confirm_password != password:
                messagebox.showerror('Shenim!', 'Fjalkalimet nuk perputhen!!!')
            else:
                with open('users.csv', 'r') as file:
                    num_lines = file.readlines()
                    for line in num_lines:
                        if line.startswith(str(i)):
                            i += 1

                with open('users.csv', 'r') as file:
                    data = file.read()
                if email in data:
                    messagebox.showerror(
                        'Shenim!', 'Ky email tashme eshte i regjistruar!!')
                else:
                    with open('users.csv', 'a') as file:
                        file.write(
                            f'\n{i}.\t-\t{first_name}\t-\t{last_name}\t-\t{email}\t-\t{password}')
                        file.flush()
                        messagebox.showinfo('Shenim!', 'Success')
                        signup_root.destroy()
                        login_form()

    global signup_root
    signup_root = tk.Tk()
    signup_root.title('Sign Up')
    signup_root.state('zoomed')
    signup_root.config(bg='slategray')

    space1 = tk.Label(signup_root, text='', height=5, bg='slategray')
    space1.pack()

    frame1 = tk.Frame(signup_root)
    frame1.pack()
    frame1.config(highlightbackground='black', highlightthickness=5, )

    space = tk.Label(frame1, text='', height=3)
    space.pack()

    sign_up_label = tk.Label(frame1, text='SIGN UP', font=("Arial", 40))
    sign_up_label.pack()

    line = tk.Canvas(frame1, height=5, highlightthickness=0,
                     width=400, bg='maroon')
    line.pack()

    space2 = tk.Label(frame1, text='', height=2)
    space2.pack()

    frame = tk.Frame(frame1)
    frame.pack()

    firstname_label = tk.Label(frame, text='FIRST NAME:', font=('Arial', 15))
    firstname_label.grid(row=0, column=0, padx=(105, 10))
    firstname_entry = tk.Entry(frame, font=('Arial', 15))
    firstname_entry.grid(row=0, column=1, padx=(10, 100))

    space3 = tk.Label(frame, text='', height=1)
    space3.grid(row=1)

    lastname_label = tk.Label(frame, text='LAST NAME:', font=('Arial', 15))
    lastname_label.grid(row=2, column=0, padx=(100, 10))
    lastname_entry = tk.Entry(frame, font=('Arial', 15))
    lastname_entry.grid(row=2, column=1, padx=(10, 100))

    space4 = tk.Label(frame, text='', height=1)
    space4.grid(row=3)

    email_label = tk.Label(frame, text='EMAIL:', font=("Arial", 15))
    email_label.grid(row=4, column=0, padx=(100, 55))
    email_entry = tk.Entry(frame, font=('Arial', 15))
    email_entry.grid(row=4, column=1, padx=(10, 100))

    space5 = tk.Label(frame, text='', height=1)
    space5.grid(row=5)

    password_label = tk.Label(frame, text='PASSWORD:', font=('Arial', 15))
    password_label.grid(row=6, column=0, padx=(100, 10))
    password_entry = tk.Entry(frame, font=('Arial', 15), show='*')
    password_entry.grid(row=6, column=1, padx=(10, 100))

    space9 = tk.Label(frame, text='', height=1)
    space9.grid(row=7)

    confirm_password_label = tk.Label(
        frame, text='CONFIRM\nPASSWORD:', font=('Arial', 15))
    confirm_password_label.grid(row=8, column=0, padx=(100, 10))
    confirm_password_entry = tk.Entry(frame, font=('Arial', 15), show='*')
    confirm_password_entry.grid(row=8, column=1, padx=(10, 100))

    space6 = tk.Label(frame1, text='', height=3)
    space6.pack()

    sign_up_button = tk.Button(frame1, text='SIGN UP', font=('Arial', 15), width=30, bg='black',
                               fg='white', command=create_acc)
    sign_up_button.pack()

    space7 = tk.Label(frame1, text='', height=3)
    space7.pack()

    back_button = tk.Button(frame1, text='BACK', bg='red', fg='white', font=('Arial', 15),
                            width=30, command=back_to_home)
    back_button.pack()

    space8 = tk.Label(frame1, text='', height=3)
    space8.pack()

    signup_root.bind('<Return>', create_acc)

    signup_root.mainloop()

# =====================================================================================================


# ======================================== HOME PAGE ================================================

def home():
    global home_root
    home_root = tk.Tk()
    home_root.title("StudyChat")
    home_root.state('zoomed')
    home_root.config(bg='midnightblue')

    def go_to_login():
        home_root.destroy()
        login_form()

    def go_to_signup():
        home_root.destroy()
        signup_form()

    header = tk.Frame(home_root)
    header.pack()
    header.config(bg='midnightblue')

    chat_logo = tk.PhotoImage(file='chatt.PNG')
    logo_header = tk.Label(header, image=chat_logo)
    logo_header.config(bg='midnightblue')
    logo_header.grid(row=0, column=0)

    logo_txt = tk.Label(header, text='Study chat', font=('Arial', 20),
                        bg='midnightblue', fg='white')
    logo_txt.grid(row=0, column=1)

    login_button = tk.Button(header, text='LOGIN', width=15,
                             bg='mediumvioletred', fg='white', font=('Arial', 15), command=go_to_login)
    login_button.grid(row=0, column=2, padx=(750, 0))

    sign_up_button = tk.Button(header, text='SIGN UP', width=15,
                               bg='mediumvioletred', fg='white', font=('Arial', 15), command=go_to_signup)
    sign_up_button.grid(row=0, column=3, padx=(20, 10))

    space1 = tk.Label(home_root, text='', height=1, bg='midnightblue')
    space1.pack()

    line = tk.Canvas(home_root, bg='bisque', width=2000,
                     highlightthickness=0, height=5)
    line.pack()

    # ====================== CONTENT ========================

    space1 = tk.Label(home_root, text='', height=3, bg='midnightblue')
    space1.pack()

    content = tk.Frame(home_root)
    content.config(bg='#04A4B7')
    content.pack()

    text_part = tk.Frame(content)
    text_part.config(bg='#04A4B7')
    text_part.grid(row=0, column=0)

    image_part = tk.Frame(content)
    image_part.grid(row=0, column=1, padx=(200, 0))

    space2 = tk.Label(text_part, text='', height=5, bg='#04A4B7')
    space2.pack()

    text1 = tk.Label(text_part, text='Have your', fg='white', font=('Copperplate', 80),
                     bg='#04A4B7')
    text1.pack()

    text2 = tk.Label(text_part, text='      best chat', fg='white', font=('Copperplate', 80),
                     bg='#04A4B7')
    text2.pack()

    space3 = tk.Label(text_part, text='', height=8, bg='#04A4B7')
    space3.pack()

    photo_image = tk.PhotoImage(file='chat_with_us.PNG')
    image = tk.Label(image_part, image=photo_image, width=600, height=300)
    image.pack()

    # =============== FOOTER ==============================

    footer = tk.Frame(home_root)
    footer.pack()
    footer.config(bg='midnightblue')

    text3 = tk.Label(footer, text='Fast, easy, unlimited', fg='white',
                     font=('Copperplate', 30), bg='blue')
    text3.grid(row=0, column=1, padx=(20, 100))

    chat_services_button = tk.Button(footer, text='chat services', font=('Copperplate', 25),
                                     fg='white', bg='mediumvioletred', command=go_to_login)
    chat_services_button.grid(row=0, column=2)

    img2 = tk.PhotoImage(file='footer_img.PNG')
    image2 = tk.Label(footer, image=img2, bg='midnightblue')
    image2.grid(row=0, column=0)

    home_root.mainloop()


# ==================================================================================================

home()
