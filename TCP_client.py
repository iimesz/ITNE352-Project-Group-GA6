import socket
from tkinter import *
from tkinter import messagebox, simpledialog

def log_in():
    client_name = name_entry.get()
    if client_name != "":
        send_message(client_name)
        display()
    else:
        messagebox.showerror("Error", "Please enter your name ")

def option_c():
    departure_IATA = simpledialog.askstring("Input", "Enter the departure IATA:")
    if departure_IATA:
        send_option('c')
        send_message(departure_IATA)
        display()

def option_d():
    flight_iata = simpledialog.askstring("Input", "Enter Flight IATA:")
    if flight_iata:
        send_option('d')
        send_message(flight_iata)
        display()

def send_option(option):
    send_message(option)
    if option == 'a' or option == 'b':
        display()

def exit_program():
    send_message('q')
    root.destroy()

def send_message(message):
    try:
        sc.send(message.encode('utf-8'))
    except socket.error as e:
        messagebox.showerror("Error", f"Socket error: {e}")
        root.destroy()

def display():
    response = sc.recv(65000).decode('utf-8')
    text_box.delete(1.0, END)
    text_box.insert(INSERT, response)

if __name__ == "__main__":
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = '127.0.0.2'
    port = 50000

    try:
        sc.connect((address, port))
        root = Tk()
        root.title("Aviation Stack Client")
        root.configure(background='light blue')

        label = Label(root, text="✈  ✈  ✈   Welcome to Aviation Stack   ✈  ✈  ✈", font="Consolas 16 bold",
                      background='light blue')
        label.pack(pady=15)

        name_label = Label(root, text="Enter your name:", font="Arial 12", background='light blue')
        name_label.pack()

        name_entry = Entry(root, font="Arial 12")
        name_entry.pack()

        log_in_button = Button(root, text="Log in", command=log_in, background='green', font="Arial 12 bold", fg='white')
        log_in_button.pack(pady=15)

        option_a = Button(root, text="a. All arrived flights", command=lambda: send_option('a'), font="Arial 12")
        option_a.pack()

        option_b = Button(root, text="b. All delayed flights", command=lambda: send_option('b'), font="Arial 12")
        option_b.pack()

        options_c = Button(root, text="c. All flights from a specific airport", command=option_c,font="Arial 12")
        options_c.pack()

        options_d = Button(root, text="d. Details of a particular flight", command=option_d, font="Arial 12")
        options_d.pack()

        text_box = Text(root, height=25, width=90, font=("Arial", 10))
        text_box.pack(pady=20)

        exit_button = Button(root, text="QUIT", command=exit_program, background='red', font="Arial 12 bold", fg='white')
        exit_button.pack()

        root.mainloop()
    except ConnectionError as e:
        print(f" Connection error: {e}")
    finally:
        sc.close()