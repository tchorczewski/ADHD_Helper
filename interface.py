from tkinter import *
from tkinter import ttk
from program_list import GetProgramList


class Interface:

    def __init__(self, root):
        self.root = root
        self.root.title('ADHD Helper')
        program_list = GetProgramList()
        self.app_list = program_list.get_program_list()
        self.selected_apps = []
        self.frm = ttk.Frame(self.root)
        self.label = ttk.Label(self.frm, text='Select applications to block:')
        self.label.pack()
        self.listbox = Listbox(self.frm, selectmode='multiple')
        for app in self.app_list:
            self.listbox.insert(END, app)
        self.listbox.pack()
        self.block_button = ttk.Button(self.frm, text='Block Apps', command=self.block_selected_apps)
        self.block_button.pack()
        self.duration_label = ttk.Label(self.frm, text='Enter duration')
        self.duration_label.pack()
        self.duration_entry = ttk.Entry(self.frm)
        self.duration_entry.pack()
        self.frm.pack()
    def block_selected_apps(self):
        return 0
    def refresh_list(self):
        return 0
