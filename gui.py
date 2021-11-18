import tkinter as tk
from bot import Bot

class scheduleStack:
    def __init__(self, username, password, page, label, date):
        self.password = password.get()
        self.username = username.get()
        self.page = page.get()
        self.date = date.get()

        self.label = label


class Gui(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui = self.configure_gui()
        self.widgets = self.create_widgets()
        self.scheduleStack = []

    def configure_gui(self):
        self.master.geometry('1000x700')

    def create_widgets(self):
        scheduleRun = tk.Button(self.master, text="Schedule", font=("Hevatica", 18), padx=10, pady=5, fg="#FFF", bg="#3582e8", command=self.run_bot)
        scheduleRun.grid(column=0, row=5, padx=10, pady=30)

        usernameLabel = tk.Label(self.master, text="Username", font=("Helvatica", 18))
        usernameLabel.grid(column=0, row=0, padx=10, pady=30)

        usernameEntry = tk.Entry(self.master, width=15, font=("Helvatica", 18))
        usernameEntry.grid(column=1, row=0, padx=10, pady=30)

        passwordLabel = tk.Label(self.master, text="Password", font=("Helvatica", 18))
        passwordLabel.grid(column=0, row=1, padx=10, pady=30)

        passwordEntry = tk.Entry(self.master,show="*", width=15, font=("Helvatica", 18))
        passwordEntry.grid(column=1, row=1, padx=10, pady=30)

        
        pageLabel = tk.Label(self.master, text="page", font=("Helvatica", 18))
        pageLabel.grid(column=0, row=2, padx=10, pady=30)

        pageEntry = tk.Entry(self.master, width=15, font=("Helvatica", 18))
        pageEntry.grid(column=1, row=2, padx=10, pady=30)

        
        dateLabel = tk.Label(self.master, text="date", font=("Helvatica", 18))
        dateLabel.grid(column=0, row=3, padx=10, pady=30)

        dateEntry = tk.Entry(self.master, width=15, font=("Helvatica", 18))
        dateEntry.grid(column=1, row=3, padx=10, pady=30)

        return usernameEntry, passwordEntry, pageEntry


    def run_bot(self):
        print("Button clicked")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RIJ Bot")
    main_app = Gui(root)
    main_app.mainloop()