import tkinter as tk
from tkinter.ttk import *
from DecryptConversionFunc import dn_convert


class decryptionDisplay:
    def __init__(self , Decryption):
        dn_label = Label(Decryption , text="Decrypt Your Data")
        dn_text1 = tk.Text(Decryption , width=30 , height=4)
        dn_button = Button(Decryption , text="Decrypt" , command=lambda : dn_convert(dn_text1 , dn_text2))
        dn_text2 = tk.Text(Decryption , width=40 , height=8)
        dn_label.pack(pady=10)
        dn_text1.pack(pady=10)
        dn_button.pack(pady=10)
        dn_text2.pack(pady=10)