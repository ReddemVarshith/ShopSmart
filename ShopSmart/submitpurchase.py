from tkinter import messagebox
import mysql.connector
from datetime import datetime
def submitPurchase(item,price,quantity,date,category_name):
    connection = mysql.connector.connect(
            host='########',
            database='shopsmart',
            user='root',
            password='########'
        )

    if connection.is_connected():
        cursor = connection.cursor()
    cursor.execute("SELECT category_id FROM categories WHERE category_name = %s", (category_name,))

    
    date_obj = datetime.strptime(date, "%d/%m/%Y")
    date = date_obj.strftime("%Y-%m-%d")

    category=cursor.fetchone()
    if category is None:
                print(f"Error: Category '{category_name}' does not exist.")
                return
    
    category_id = category[0]
    cursor.execute("INSERT INTO PURCHASES (item_name ,price ,quantity , purchase_date,category_id) VALUES (%s , %s , %s , %s , %s)",(item,price,quantity,date,category_id))
    connection.commit()

    messagebox.showinfo("Succesfull", "Purchase Added Succesfully")
