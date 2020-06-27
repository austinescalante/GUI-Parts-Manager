from tkinter import *

#window object
app = Tk()

#Create label for part
part_text = StringVar()
part_label = Label(app, text='Part Name',font=('bold',14),pady=20)
#Place part label in grid. Align to west
part_label.grid(row=0,column=0,stick=W)

#Entry for Part Name: row 0, column 1
part_entry= Entry(app, textvariable=part_text)
part_entry.grid(row=0,column=1)


#Customer
customer_text = StringVar()
customer_label = Label(app, text='Customer',font=('bold',14),pady=20)
#Place customer label in grid. Align to west
customer_label.grid(row=0,column=2,stick=W)

#Entry for Customer Name: row 0, column 1
customer_entry= Entry(app, textvariable=customer_text)
customer_entry.grid(row=0,column=3)

#Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer',font=('bold',14),pady=20)
#Place retailer label in grid. Align to west
retailer_label.grid(row=1,column=0,stick=W)

#Entry for Retailer Name: row 0, column 1
retailer_entry= Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1,column=1)

#Price
price_text = StringVar()
price_label = Label(app, text='Price',font=('bold',14),pady=20)
#Place price label in grid. Align to west
price_label.grid(row=1,column=2,stick=W)

#Entry for Price Name: row 0, column 1
price_entry= Entry(app, textvariable=price_text)
price_entry.grid(row=1,column=3)




#Parts List(Listbox), Border listed at 0 if no items in list
parts_list=Listbox(app,height=8,width=50,border=0)
parts_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)


#Scrollbar
scrollbar=Scrollbar(app)
scrollbar.grid(row=3,column=3)

#Set Scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)


app.title('Part Manager')
app.geometry('700x350')

#Start program
app.mainloop()
