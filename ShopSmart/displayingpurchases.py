import mysql.connector
import tkinter as tk
from tkinter import ttk
connection = mysql.connector.connect(
            host='#######',
            database='shopsmart',
            user='root',
            password='########'
        )

if connection.is_connected():
    cursor = connection.cursor()
def display_purchases_category(selected_category):


    cursor.execute("SELECT category_id FROM categories WHERE category_name=%s",(selected_category,))
    category_id=cursor.fetchone()
    category_id=category_id[0]
    print(category_id)
    cursor.execute(f"SELECT item_name FROM purchases WHERE category_id={category_id}")
    selected_items=cursor.fetchall()
    selected_items_arr=[]
    for i in selected_items:
        print(i)
        selected_items_arr.append(str(i)[2:len(i)-4])
    return selected_items_arr

    


    



    

