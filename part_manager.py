
from tkinter import *

def populate_list():
    print('populate')

def add_item():
    print('Add')

def remove_item():
    print('Remove')

def update_item():
    print('Update')

def clear_input():
    print('Clear Item')    

#create a window object
app = Tk()


#Part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold, 13'), pady=20, padx=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold, 13'), pady=20, padx=20)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

#Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold, 13'), pady=20, padx=20)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

#Prices
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold, 13'), pady=20, padx=20)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# Parts List(Listbox)
parts_list = Listbox(app, height=10, width=70, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#Create a scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

# Buttons
add_btn=Button(app, text ='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn=Button(app, text ='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn=Button(app, text ='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn=Button(app, text ='Clear Input', width=12, command=clear_input)
clear_btn.grid(row=2, column=3, pady=20)

app.title('Part Manager')
app.geometry('800x550')

# Populate data
populate_list()

#Start program
app.mainloop()