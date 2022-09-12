import tkinter as tk
import sqlite3
import pandas as pd


def register_customer():
    connection = sqlite3.connect('customer_database.db')

    cursor_db = connection.cursor()

    cursor_db.execute("INSERT INTO customer VALUES(:first_name, :last_name, :email, :phone)",
                      {
                          'first_name': entry_first_name.get(),
                          'last_name': entry_last_name.get(),
                          'email': entry_email.get(),
                          'phone': entry_phone.get()
                      }
                      )
    connection.commit()

    connection.close()

    entry_first_name.delete(0, "end")
    entry_last_name.delete(0, "end")
    entry_email.delete(0, "end")
    entry_phone.delete(0, "end")


def export_customers():
    connection = sqlite3.connect('customer_database.db')

    cursor_db = connection.cursor()

    cursor_db.execute("SELECT *, oid FROM customer")
    registered_customer = cursor_db.fetchall()
    registered_customer = pd.DataFrame(registered_customer,
                                       columns=['first_name', 'last_name', 'email', 'phone', 'Id_database'])
    registered_customer.to_excel('customers_database.xlsx')
    connection.commit()
    connection.close()


# Front End
window = tk.Tk()
window.title('Ferramenta de Cadastro de Clientes')

# Label
label_first_name = tk.Label(window, text='Nome')
label_first_name.grid(row=0, column=0, padx=10, pady=10)

label_last_name = tk.Label(window, text='Sobrenome')
label_last_name.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(window, text='Email')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_phone = tk.Label(window, text='Telefone')
label_phone.grid(row=3, column=0, padx=10, pady=10)

# Entry
entry_first_name = tk.Entry(window, width=30)
entry_first_name.grid(row=0, column=1, padx=10, pady=10)

entry_last_name = tk.Entry(window, width=30)
entry_last_name.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(window, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_phone = tk.Entry(window, width=30)
entry_phone.grid(row=3, column=1, padx=10, pady=10)

# Buttons
button_register = tk.Button(window, text='Cadastrar Cliente', command=register_customer)
button_register.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

button_export = tk.Button(window, text='Exportar Base de Cliente', command=export_customers)
button_export.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

window.mainloop()
