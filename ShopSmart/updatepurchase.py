import mysql.connector
from tkinter import messagebox
from datetime import datetime
connection = mysql.connector.connect(
            host='#######',
            database='shopsmart',
            user='root',
            password='########'
        )
    
if connection.is_connected():
    cursor = connection.cursor()
def default_value_retrieve(selected_item):


    cursor.execute("select price,quantity,purchase_date from purchases where item_name=%s",(selected_item,))
    result=cursor.fetchone()
    if result is None:
        messagebox.showerror("Error", f"No purchase found for item: {selected_item}")
        return None, None, None  
    else:
        price, quantity, purchase_date = result
        return price, quantity, purchase_date
    
def update_purchase_item(item, price, quantity, date):
    date_obj = datetime.strptime(date, "%d/%m/%Y")  
    date = date_obj.strftime("%Y-%m-%d")   
    cursor.execute("UPDATE purchases SET price=%s, quantity=%s, purchase_date=%s WHERE item_name=%s", (price, quantity, date, item))
    connection.commit()
    messagebox.showinfo("Succesfull", "Purchase Updated Succesfully")

def delete_purchase_item(item):
    cursor.execute("Delete FROM purchases WHERE item_name=%s",(item,))
    connection.commit()
    messagebox.showinfo("Succesfull","Purchase Deleted Succesfully")



