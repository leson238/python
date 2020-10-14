import os

from tkinter import filedialog, Tk, StringVar
from tkinter import Entry, Label, Button, Listbox, messagebox
from tkinter import END

import manage

main_win = Tk()
main_win.sourceFolder = ''
currdir = os.getcwd()

def chooseDir(entry):
    def wrapper():
        main_win.sourceFolder =  filedialog.askdirectory(parent=main_win, initialdir= currdir, title='Please select a directory')
        entry.insert(END,main_win.sourceFolder)
    return wrapper


Label(main_win, text='Input Folder').grid(row=0, sticky='W')
input_value= StringVar()
input_path = Entry(main_win, textvariable=input_value)
input_path.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
b_input = Button(main_win, text = "Browse...", command = chooseDir(input_path))
b_input.grid(row=0, column = 3, padx=5, pady=5)

Label(main_win, text='Output Folder').grid(row=1, sticky='W')
output_value = StringVar()
output_path = Entry(main_win, textvariable=output_value)
output_path.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
b_output = Button(main_win, text = "Browse...", command = chooseDir(output_path))
b_output.grid(row=1, column = 3, padx=5, pady=5)

test_result = Listbox(main_win)
test_result.grid(row=3, column=0, columnspan = 4, sticky='NESW')

def tests_suite():
    tests = manage.manage(input_value.get(), output_value.get())()
    for test in tests:
        test_result.insert(END, test)

def create_report():
    manage.manage(input_value.get(), output_value.get())
    result = messagebox.askyesno('Show Report File', 'Do you want to open Reports.txt? ')
    if result:
        os.system('start "" {}\\reports.txt'.format(output_value.get()))

b_test = Button(main_win, text='Test Input Quality', command=tests_suite)
b_test.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='NESW')

b_create = Button(main_win, text='Create Reports.txt', command=create_report)
b_create.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky='NESW')

main_win.mainloop()