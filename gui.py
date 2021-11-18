import tkinter as tk
from bot import Bot


class Gui(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui = self.configure_gui()
        self.widgets = self.create_widgets()

    def configure_gui(self):
        self.master.geometry('1000x700')

    def create_widgets(self):
        scheduleRun = tk.Button(self.master, text="Schedule", font=("Hevatica", 18), padx=10, pady=5, fg="#FFF", bg="#3582e8", command=self.run_bot)
        scheduleRun.grid(column=0, row=5, padx=10, pady=30)

        usernameLabel = tk.Label(self.master, text="Username", font=("Helvatica", 18))
        usernameLabel.grid(column=0, row=0, padx=10, pady=30)


    def run_bot(self):
        print("Button clicked")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RIJ Bot")
    main_app = Gui(root)
    main_app.mainloop()