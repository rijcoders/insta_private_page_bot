import tkinter as tk
import time
import datetime

from bot import Bot

# Scheduler will add later
class ScheduleStack:
    def __init__(self, username, password, page, label, fileTypeEntry):
        self.password = password.get()
        self.username = username.get()
        self.page = page.get()
        self.fileTypeEntry = fileTypeEntry.get()
        self.timeStamp = time.mktime(datetime.datetime.strptime(self.date, "%Y-%m-%d %H:%M").timetuple())

        self.label = label


class Gui(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui = self.configure_gui()
        self.widgets = self.create_widgets()
        self.scheduleStack = []

    def configure_gui(self):
        self.master.geometry('700x700')

    def create_widgets(self):
        scheduleRun = tk.Button(self.master, text="Download", font=("Hevatica", 18), padx=10, pady=5, fg="#FFF", bg="#3582e8", command=self.run_bot)
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

        
        fileTypeEntry = tk.Label(self.master, text="post/video", font=("Helvatica", 18))
        fileTypeEntry.grid(column=0, row=3, padx=10, pady=30)

        fileTypeEntry = tk.Entry(self.master, width=15, font=("Helvatica", 18))
        fileTypeEntry.grid(column=1, row=3, padx=10, pady=30)

        return usernameEntry, passwordEntry, pageEntry, fileTypeEntry


    def run_bot(self):
        username, password, page, file_type = self.widgets
        resultLabel = tk.Label(self.master, anchor="e", justify=tk.LEFT, text=" * Page: " + page.get() + " | Date: " + file_type.get() + "Download is Finished", font=("Helvatica", 13))
        resultLabel.grid(column=0, row=len(self.scheduleStack) + 6, padx=10, pady=2)

        Bot(username=username.get(), password=password.get(), page=page.get(), file_type=file_type.get())



        # scheduleStack = ScheduleStack(username=username, password=password, page=page, label=resultLabel, date=date)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("RIJ Bot")
    main_app = Gui(root)
    main_app.mainloop()