from tkinter import Tk
from tkinter import Label, Listbox, Entry, Scrollbar, Button, messagebox
from tkinter import StringVar, END
from backend import Restaurants

restaurants = Restaurants()


class Window:
    def __init__(self, window):
        self.window = window
        self.window.wm_title("Restaurants Yelp")
        self.l1 = Label(window, text='Restaurant Name')
        self.l1.grid(row=0, column=0, sticky='w')

        self.l2 = Label(window, text='Address')
        self.l2.grid(row=1, column=0, sticky='w')

        self.l3 = Label(window, text='Average Price (Less than)')
        self.l3.grid(row=0, column=2, sticky='w')

        self.l4 = Label(window, text='Distance (Less than)')
        self.l4.grid(row=1, column=2, sticky='w')

        self.l5 = Label(window, text='Nationality')
        self.l5.grid(row=2, column=0, sticky='w')

        self.name_text = StringVar()
        self.e1 = Entry(window, textvariable=self.name_text)
        self.e1.bind("<Button-1>", self.clear_box)
        self.e1.grid(row=0, column=1)

        self.address_text = StringVar()
        self.e2 = Entry(window, textvariable=self.address_text)
        self.e2.bind("<Button-1>", self.clear_box)
        self.e2.grid(row=1, column=1)

        self.avgp_text = StringVar()
        self.e3 = Entry(window, textvariable=self.avgp_text)
        self.e3.bind("<Button-1>", self.clear_box)
        self.e3.grid(row=0, column=3)

        self.distance_text = StringVar()
        self.e4 = Entry(window, textvariable=self.distance_text)
        self.e4.bind("<Button-1>", self.clear_box)
        self.e4.grid(row=1, column=3)

        self.nationality_text = StringVar()
        self.e5 = Entry(window, textvariable=self.nationality_text)
        self.e5.bind("<Button-1>", self.clear_box)
        self.e5.grid(row=2, column=1)

        self.l0 = Label(window, text='')
        self.l0.grid(row=3, column=0)

        self.b0 = Button(window, text='Search By Input', width=17,
                         command=self.search_command)
        self.b0.grid(row=2, column=3)

        self.list1 = Listbox(window)
        self.list1.grid(row=4, column=1, rowspan=5, columnspan=3, sticky='ew')

        self.sb1 = Scrollbar(window)
        self.sb1.grid(row=4, column=4, rowspan=5, sticky='ns')

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.b1 = Button(window, text='View All', width=12,
                         command=self.view_command)
        self.b1.grid(row=4, column=0)

        self.l6 = Label(window, text='Search: ')
        self.l6.grid(row=5, column=0)

        self.b2 = Button(window, text='By Location',
                         width=12, command=self.search_by_location_command)
        self.b2.grid(row=6, column=0)

        self.b3 = Button(window, text='By High Price',
                         width=12, command=self.search_by_high_price_command)
        self.b3.grid(row=7, column=0)

        self.b4 = Button(window, text='By Low Price',
                         width=12, command=self.search_by_low_price_command)
        self.b4.grid(row=8, column=0)

        self.b5 = Button(window, text='Close', width=12, command=self.close)
        self.b5.grid(row=9, column=0, columnspan=4)

    def view_command(self):
        self.list1.delete(0, END)
        for restaurant in restaurants.view():
            self.list1.insert(END, restaurant)

    def search_by_high_price_command(self):
        self.list1.delete(0, END)
        for restaurant in restaurants.search_by_price(lowest=False):
            self.list1.insert(END, restaurant)

    def search_by_low_price_command(self):
        self.list1.delete(0, END)
        for restaurant in restaurants.search_by_price():
            self.list1.insert(END, restaurant)

    def search_by_location_command(self):
        self.list1.delete(0, END)
        for restaurant in restaurants.search_by_location():
            self.list1.insert(END, restaurant)

    def search_command(self):
        self.list1.delete(0, END)
        try:
            searched = restaurants.search(self.name_text.get(), self.address_text.get(
            ), self.avgp_text.get(), self.distance_text.get(), self.nationality_text.get())
            if searched:
                for restaurant in searched:
                    self.list1.insert(END, restaurant)
            else:
                messagebox.showwarning(
                    title="No Restaurant", message="Cannot find any restaurant, try again")
        except ValueError:
            messagebox.showerror(
                title="Wrong Input", message="Average Price and Distance must be a decimal number")

    def clear_box(self, event):
        event.widget.delete(0, END)

    def close(self):
        self.window.destroy()


window = Tk()
Window(window)
window.mainloop()
