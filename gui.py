import tkinter as tk
from tkinter import StringVar, filedialog
import os


class my_gui():
    def __init__(self, title, download_function):
        self.window = tk.Tk()

        self.window.title(title)

        self.path_label = tk.Label(text='Dateipfad:')
        self.link_label = tk.Label(text='Link:')
        self.finished_text = tk.StringVar()
        self.finished_label = tk.Label(textvariable=self.finished_text)

        self.file_path = self.get_path_from_file()
        self.link = ''

        self.path_label.grid(row=0)
        self.link_label.grid(row=1)
        self.finished_label.grid(row=3)

        self.path_button = tk.Button(
            text='Durchsuchen', command=lambda: self.get_path_from_filedialog())
        self.link_entry = tk.Entry()

        self.path_button.grid(row=0, column=1)
        self.link_entry.grid(row=1, column=1)

        self.confirm_button = tk.Button(
            text='Download', command=lambda: self.download(download_function))
        self.confirm_button.grid(row=3, column=2)
        self.mainloop()

    def write_path_to_file(self, path):
        with open('path.txt', 'w') as f:
            f.write(path)

    def get_link(self):
        self.link = self.link_entry.get()
        return self.link
    
    def finished(self):
        self.finished_text.set('Finished!')
    

    def downloading(self):
        self.finished_text.set('Downloading...')
        
    def get_path_from_file(self):
        if os.path.isfile('path.txt'):
            with open('path.txt', 'r') as f:
                return f.read()

    def get_path_from_filedialog(self):
        path = filedialog.askdirectory()
        if path:
            self.write_path_to_file(path)
            self.file_path = self.get_path_from_file()

    def mainloop(self):
        self.window.mainloop()
    
    def download(self, download_function):
        self.downloading()
        self.window.update_idletasks()
        download_function()
        self.finished()
        self.window.update_idletasks()
