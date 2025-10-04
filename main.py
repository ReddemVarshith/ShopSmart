import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

app = tk.Tk()
app.title("Shop Smart")
width = 960
height = int((width / 16) * 9) 
app.geometry(f"{width}x{height}")
app.resizable(False, False)

button_frame =  tk.Frame(app, width=225, height=600, bg="lightblue")
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
def add_purchase():
    def submitPurchase():
        print("Success")
    
    global right_frame
    vcmd = app.register(digitornot)  
    if right_frame is None:
        right_frame = tk.Frame(app, padx=40, pady=20, bg="white")
        right_frame.pack_propagate(False)
        right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        item_label = tk.Label(right_frame, text="Item", font=("Arial", 12))
        category_label = tk.Label(right_frame, text="Category", font=("Arial", 12))
        price_label = tk.Label(right_frame, text="Price", font=("Arial", 12))
        quantity_label = tk.Label(right_frame, text="Quantity", font=("Arial", 12))
        date_label = tk.Label(right_frame, text="Date", font=("Arial", 12))

        item_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="solid")
        price_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="solid", validate="key", validatecommand=(vcmd, '%P'))
        quantity_entry = tk.Entry(right_frame, font=("Arial", 12), bd=2, relief="solid", validate="key", validatecommand=(vcmd, '%P'))
        date_entry = DateEntry(right_frame, selectmode='day', date_pattern='dd/mm/yyyy')

        selected_option = tk.StringVar()
        selected_option.set("Select an option")
        combobox = ttk.Combobox(right_frame, textvariable=selected_option, values=categories)

        add_purchase_button = tk.Button(right_frame, text="Add the Purchase", command=submitPurchase)

        # Layout using grid
        item_label.grid(row=0, column=0, sticky="w", pady=10, padx=10)
        item_entry.grid(row=0, column=1, sticky="w", pady=10, padx=10)

        category_label.grid(row=1, column=0, sticky="w", pady=10, padx=10)
        combobox.grid(row=1, column=1, sticky="w", pady=10, padx=10)

        price_label.grid(row=2, column=0, sticky="w", pady=10, padx=10)
        price_entry.grid(row=2, column=1, sticky="w", pady=10, padx=10)

        quantity_label.grid(row=3, column=0, sticky="w", pady=10, padx=10)
        quantity_entry.grid(row=3, column=1, sticky="w", pady=10, padx=10)

        date_label.grid(row=4, column=0, sticky="w", pady=10, padx=10)
        date_entry.grid(row=4, column=1, sticky="w", pady=10, padx=10)

        add_purchase_button.grid(row=5, column=0, columnspan=2, pady=20, padx=10, sticky="ew")

        # Column configuration to expand the width
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_columnconfigure(1, weight=3)

        app.grid_columnconfigure(1, weight=1)
    else:
        print("Already displayed")

def quit():
    app.quit()
    

AddPurchase = tk.Button(button_frame, text="Add Purchase",width=225,command=add_purchase)
AddPurchase.pack(side="top", pady=(20, 20))

UpdatePurchase = tk.Button(button_frame, text="Update Purchase",width=225)
UpdatePurchase.pack(pady=20)

DeletePurchase=tk.Button(button_frame,text="Delete a Purchase",width=225)
DeletePurchase.pack(pady=20)

ViewPurchase=tk.Button(button_frame,text="View all Purchases",width=225)
ViewPurchase.pack(pady=20)

summary=tk.Button(button_frame,text="Summary/Report",width=225)
summary.pack(pady=20)

Exit=tk.Button(button_frame,text="Exit",width=225,command=quit)
Exit.pack(pady=20)



app.mainloop()