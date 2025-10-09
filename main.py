import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import font as tkFont
from submitpurchase import submitPurchase
from displayingpurchases import display_purchases_category
from updatepurchase import default_value_retrieve,update_purchase_item,delete_purchase_item
import mysql.connector


connection = mysql.connector.connect(
            host='########',
            database='shopsmart',
            user='root',
            password='#########'  #Replaced the actual password
        )

if connection.is_connected():
    cursor = connection.cursor()

app = tk.Tk()
app.title("Shop Smart")
width = 960
height = int((width / 16) * 9)
app.geometry(f"{width}x{height}")
app.resizable(False, False)

button_frame = tk.Frame(app, width=225, height=600, bg="lightblue")
button_frame.pack_propagate(False)
button_frame.pack(side="left", fill="y", padx=5, pady=5)

MenuLabel = tk.Label(button_frame, text="Menu", font=("Helvetica", 16, "bold"), bg="lightblue")
MenuLabel.pack(side="top", pady=(0, 10))

categories = [
    "Groceries",
    "Household Supplies",
    "Utilities",
    "Clothing & Accessories",
    "Health & Fitness",
    "Education & Books",
    "Personal Care",
    "Fuel & Transport",
    "Travel & Vacations",
    "Dining & Restaurants",
    "Entertainment & Subscriptions",
    "Hobbies & Games",
    "Electronics & Appliances",
    "Software & Apps",
    "Rent & Mortgage",
    "Loans & EMIs",
    "Savings & Investments",
    "Gifts & Celebrations",
    "Donations & Charity",
    "Other"
]

def digitornot(text):
    if text.isdigit() or text == "":
        return True
    else:
        return False

right_frame = None

def clear_right_frame():
    global right_frame
    
    if right_frame is not None:
        right_frame.destroy()
        right_frame = None

def add_purchase():
    global right_frame
    vcmd = app.register(digitornot)
    
    clear_right_frame()  
    
    right_frame = tk.Frame(app, padx=40, pady=20, bg="white")
    right_frame.pack_propagate(False)
    right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    heading_font = tkFont.Font(family="Arial", size=16, weight="bold")

    heading_label = tk.Label(
        right_frame,
        text="Shop Smart",
        font=heading_font,
        fg="navy blue", 
        bg="lightgray", 
        padx=10,         
        pady=5           
    )


    item_label = tk.Label(right_frame, text="Item", font=("Arial", 12))
    category_label = tk.Label(right_frame, text="Category", font=("Arial", 12))
    price_label = tk.Label(right_frame, text="Price", font=("Arial", 12))
    quantity_label = tk.Label(right_frame, text="Quantity", font=("Arial", 12))
    date_label = tk.Label(right_frame, text="Date", font=("Arial", 12))

    item_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="solid")
    price_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="solid", validate="key", validatecommand=(vcmd, '%P'))
    quantity_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="solid", validate="key", validatecommand=(vcmd, '%P'))
    date_entry = DateEntry(right_frame, selectmode='day', date_pattern='dd/mm/yyyy')

    selected_option_category = tk.StringVar()
    selected_option_category.set("Select an option")
    combobox = ttk.Combobox(right_frame, textvariable=selected_option_category, values=categories)

    add_purchase_button = tk.Button(right_frame, text="Add the Purchase", command=lambda: submitPurchase(item_entry.get(), price_entry.get(), quantity_entry.get(), date_entry.get(), selected_option_category.get()))

    heading_label.grid(row=0, column=0, columnspan=2, sticky="n", pady=10, padx=10)
    item_label.grid(row=1, column=0, sticky="w", pady=10, padx=10)
    item_entry.grid(row=1, column=1, sticky="w", pady=10, padx=10)

    category_label.grid(row=2, column=0, sticky="w", pady=10, padx=10)
    combobox.grid(row=2, column=1, sticky="w", pady=10, padx=10)

    price_label.grid(row=3, column=0, sticky="w", pady=10, padx=10)
    price_entry.grid(row=3, column=1, sticky="w", pady=10, padx=10)

    quantity_label.grid(row=4, column=0, sticky="w", pady=10, padx=10)
    quantity_entry.grid(row=4, column=1, sticky="w", pady=10, padx=10)

    date_label.grid(row=5, column=0, sticky="w", pady=10, padx=10)
    date_entry.grid(row=5, column=1, sticky="w", pady=10, padx=10)

    add_purchase_button.grid(row=6, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

    
    right_frame.grid_columnconfigure(0, weight=3)
    right_frame.grid_columnconfigure(1, weight=3)

    app.grid_columnconfigure(1, weight=1)

def update_purchase():

    def ok_button_item(selected_item):
        price,quantity,date=default_value_retrieve(selected_item)
        if price is None:  
            return
        price_label = tk.Label(right_frame, text="Price", font=("Arial", 12))
        quantity_label = tk.Label(right_frame, text="Quantity", font=("Arial", 12))
        date_label = tk.Label(right_frame, text="Date", font=("Arial", 12))

        price_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="solid", validate="key", validatecommand=(vcmd, '%P'))
        quantity_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="solid", validate="key", validatecommand=(vcmd, '%P'))
        date_entry = DateEntry(right_frame, selectmode='day', date_pattern='dd/mm/yyyy')

        price_entry.insert(0,int(price))
        quantity_entry.insert(0,quantity)
        formatted_date = date.strftime("%d/%m/%Y")
        date_entry.delete(0, 'end')
        date_entry.insert(0, formatted_date)


        update_purchase_button = tk.Button(right_frame, text="Update the Purchase",command=lambda :update_purchase_item(selected_item,price_entry.get(),quantity_entry.get(),date_entry.get()))
        update_purchase_button.grid(row=6, column=0, columnspan=2, pady=20, padx=10, sticky="ew")
        
        price_label.grid(row=3, column=0, sticky="w", pady=10, padx=10)
        price_entry.grid(row=3, column=1, sticky="w", pady=10, padx=10)

        quantity_label.grid(row=4, column=0, sticky="w", pady=10, padx=10)
        quantity_entry.grid(row=4, column=1, sticky="w", pady=10, padx=10)

        date_label.grid(row=5, column=0, sticky="w", pady=10, padx=10)
        date_entry.grid(row=5, column=1, sticky="w", pady=10, padx=10)


        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_columnconfigure(1, weight=3)

        app.grid_columnconfigure(1, weight=1)

        
        
    def ok_button_category(selected_category):
        selected_option_item = display_purchases_category(selected_category)
        item_label = tk.Label(right_frame, text="Select the Item", font=("Arial", 12))
        
      
        selected_option_item_var = tk.StringVar()
        selected_option_item_var.set("Select The Item")  
        
     
        combobox_item = ttk.Combobox(right_frame, textvariable=selected_option_item_var, values=selected_option_item)
        
        
        okbutton_item=tk.Button(right_frame,text="Ok",command=lambda: ok_button_item(selected_option_item_var.get()))
        
        item_label.grid(row=2, column=0, sticky="w", pady=10, padx=10)
        combobox_item.grid(row=2, column=1, sticky="w", pady=10, padx=10)
        okbutton_item.grid(row=2, column=2, sticky="w", pady=10, padx=10)
        

    global right_frame
    vcmd = app.register(digitornot)

    clear_right_frame()  

    right_frame = tk.Frame(app, padx=40, pady=20, bg="white")
    right_frame.pack_propagate(False)
    right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    category_label = tk.Label(right_frame, text="Select the Category", font=("Arial", 12))

    heading_font = tkFont.Font(family="Arial", size=16, weight="bold")

    heading_label = tk.Label(
        right_frame,
        text="Shop Smart",
        font=heading_font,
        fg="navy blue", 
        bg="lightgray", 
        padx=10,         
        pady=5           
    )

    selected_option_category = tk.StringVar()
    selected_option_category.set("Select an option")
    combobox_category = ttk.Combobox(right_frame, textvariable=selected_option_category, values=categories)

    heading_label.grid(row=0, column=0, columnspan=2, sticky="n", pady=10, padx=10)
    category_label.grid(row=1, column=0, sticky="w", pady=10, padx=10)
    combobox_category.grid(row=1, column=1, sticky="w", pady=10, padx=10)

    okbutton=tk.Button(right_frame,text="Ok",command=lambda: ok_button_category(selected_option_category.get()))
    okbutton.grid(row=1, column=2, sticky="w", pady=10, padx=10)

    



    right_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_columnconfigure(1, weight=3)

def delete_purchase():
    def ok_button_item(selected_item):
 
        delete_purchase_button = tk.Button(right_frame, text="Delete the Purchase",command=lambda :delete_purchase_item(selected_item))
        delete_purchase_button.grid(row=5, column=0, columnspan=2, pady=20, padx=10, sticky="ew")


        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_columnconfigure(1, weight=3)

        app.grid_columnconfigure(1, weight=1)

        
        
    def ok_button_category(selected_category):
        selected_option_item = display_purchases_category(selected_category)
        item_label = tk.Label(right_frame, text="Select the Item", font=("Arial", 12))
        
      
        selected_option_item_var = tk.StringVar()
        selected_option_item_var.set("Select The Item")  
        
     
        combobox_item = ttk.Combobox(right_frame, textvariable=selected_option_item_var, values=selected_option_item)
        
        
        okbutton_item=tk.Button(right_frame,text="Ok",command=lambda: ok_button_item(selected_option_item_var.get()))
        
        item_label.grid(row=2, column=0, sticky="w", pady=10, padx=10)
        combobox_item.grid(row=2, column=1, sticky="w", pady=10, padx=10)
        okbutton_item.grid(row=2, column=2, sticky="w", pady=10, padx=10)
        

    global right_frame
    vcmd = app.register(digitornot)

    clear_right_frame()  

    right_frame = tk.Frame(app, padx=40, pady=20, bg="white")
    right_frame.pack_propagate(False)
    right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    category_label = tk.Label(right_frame, text="Select the Category", font=("Arial", 12))

    heading_font = tkFont.Font(family="Arial", size=16, weight="bold")

    heading_label = tk.Label(
        right_frame,
        text="Shop Smart",
        font=heading_font,
        fg="navy blue", 
        bg="lightgray", 
        padx=10,         
        pady=5           
    )

    selected_option_category = tk.StringVar()
    selected_option_category.set("Select an option")
    combobox_category = ttk.Combobox(right_frame, textvariable=selected_option_category, values=categories)

    heading_label.grid(row=0, column=0, columnspan=2, sticky="n", pady=10, padx=10)
    category_label.grid(row=1, column=0, sticky="w", pady=10, padx=10)
    combobox_category.grid(row=1, column=1, sticky="w", pady=10, padx=10)

    okbutton=tk.Button(right_frame,text="Ok",command=lambda: ok_button_category(selected_option_category.get()))
    okbutton.grid(row=1, column=2, sticky="w", pady=10, padx=10)

    
    






    right_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_columnconfigure(1, weight=3)

def view_purchase():
    global right_frame

    clear_right_frame()  

    right_frame = tk.Frame(right_frame, padx=40, pady=20, bg="white")
    right_frame.pack_propagate(False)
    right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)
    tree = ttk.Treeview(right_frame, show='headings')
    table_name = "purchases"
    cursor.execute(f"SELECT item_name,price,quantity,purchase_date FROM {table_name}")
    columns = [desc[0] for desc in cursor.description] 
    tree["columns"] = columns

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center') 
    for row in cursor:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill='both')

    

def quit():
    app.quit()

AddPurchase = tk.Button(button_frame, text="Add Purchase", width=225, command=add_purchase)
AddPurchase.pack(side="top", pady=(20, 20))

UpdatePurchase = tk.Button(button_frame, text="Update Purchase", width=225, command=update_purchase)
UpdatePurchase.pack(pady=20)

DeletePurchase = tk.Button(button_frame, text="Delete a Purchase", width=225,command=delete_purchase)
DeletePurchase.pack(pady=20)

ViewPurchase = tk.Button(button_frame, text="View all Purchases", width=225,command=view_purchase)
ViewPurchase.pack(pady=20)


Exit = tk.Button(button_frame, text="Exit", width=225, command=quit)
Exit.pack(pady=20)

app.mainloop()

