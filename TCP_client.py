import socket
from tkinter import *
from tkinter import messagebox, simpledialog

class AviationStackClientGUI:
    def __init__(self, master):
        self.master = master
        master.title("Aviation Stack Client")
        master.configure(background='light blue')

        self.label = Label(master, text="✈️  ✈️  ✈️   Welcome to Aviation Stack   ✈️  ✈️  ✈️", font="Consolas 16 bold", background='light blue')
        self.label.pack(pady=15)

        self.name_label = Label(master, text="Enter your name:", font="Arial 12", background='light blue')
        self.name_label.pack()

        self.name_entry = Entry(master, font="Arial 12")
        self.name_entry.pack()

        self.log_in_button = Button(master, text="Log in", command=self.log_in, background='green', font="Arial 12 bold", fg='white')
        self.log_in_button.pack(pady=15)

        self.option_a_button = Button(master, text="a. All arrived flights", command=lambda: self.send_option('a'), font="Arial 12")
        self.option_a_button.pack()

        self.option_b_button = Button(master, text="b. All delayed flights", command=lambda: self.send_option('b'), font="Arial 12")
        self.option_b_button.pack()

        self.option_c_button = Button(master, text="c. All flights from a specific airport", command=self.option_c, font="Arial 12")
        self.option_c_button.pack()

        self.option_d_button = Button(master, text="d. Details of a particular flight", command=self.option_d, font="Arial 12")
        self.option_d_button.pack()

        self.text_box = Text(master, height=25, width=90, font=("Arial", 10))
        self.text_box.pack(pady=20)

        self.exit_button = Button(master, text="QUIT", command=self.exit_program, background='red', font="Arial 12 bold", fg='white')
        self.exit_button.pack()
    def log_in(self):
        client_name = self.name_entry.get()
        if client_name != "":
            self.send_message(client_name)
            self.receive_and_display_message()
        else:
            messagebox.showerror("Error", "Plase enter your name ")

    def option_c(self):
        airport_icao = simpledialog.askstring("Input", "Enter the departure IATA:")
        if airport_icao:
            self.send_option('c')
            self.send_message(airport_icao)
            self.receive_and_display_message()

    def option_d(self):
        Fligth_IATA = simpledialog.askstring("Input", "Enter Fligth IATA:")
        if Fligth_IATA:
            self.send_option('d')
            self.send_message(Fligth_IATA)
            self.receive_and_display_message()

    def send_option(self, option):
        self.send_message(option)
        if option == 'a' or option == 'b':
            self.receive_and_display_message()
        else:
            pass

    def exit_program(self):
        self.send_message('q')
        self.master.destroy()

    def send_message(self, message):
        try:
            sc.send(message.encode('utf-8'))
        except socket.error as e:
            messagebox.showerror("Error", f"Socket error: {e}")
            self.master.destroy()

    def receive_and_display_message(self):
        response = sc.recv(65000).decode('utf-8')
        self.text_box.delete(1.0, END)  # Clear previous text
        self.text_box.insert(INSERT, response)

if __name__ == "__main__":
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = '127.0.0.2'
    port = 50000

    try:
        sc.connect((address, port))
        root = Tk()             
        gui = AviationStackClientGUI(root)
        root.mainloop()
    except ConnectionError as e:
        print(f" Connection error: {e}")
    finally:
        sc.close()
