import tkinter as tk
from commands import check_balance
from deposit import show_deposit_ui

# Create the main window
root = tk.Tk()

#add a tittle to main window
root.title("ATM Simulator")

# Create a tk frame for main window
frame = tk.Frame(root, padx=50, pady=50 )
frame.grid(row=0, column=0, sticky="nsew")


#Add account number entry
account_number_entry = tk.Entry(frame, width=50)
account_number_entry.grid(column=1, row=1)

#Add check balance button
check_balance_btn = tk.Button(frame, text="Check Balance", command=lambda: check_balance(account_number=account_number_entry.get()))
check_balance_btn.grid(column=2, row=1)

#Add deposit button
deposit_btn = tk.Button(frame, text="Deposit", command=lambda : show_deposit_ui(root))
deposit_btn.grid(column=2, row=3)


#Open the main window
root.mainloop()