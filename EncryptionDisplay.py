import tkinter as tk
from tkinter.ttk import *
from EncryptConvertionFunc import en_convert

class encryptionDisplay:
    def __init__(self , Encryption):
        en_label = Label(Encryption , text="Encrypt Your Data")
        en_text1 = tk.Text(Encryption , width=30 , height=4)
        en_button = Button(Encryption , text="Encrypt" , command=lambda : en_convert(en_text1 , en_text2))
        en_text2 = tk.Text(Encryption , width=40 , height=8)
        en_label.pack(pady=10)
        en_text1.pack(pady=10)
        en_button.pack(pady=10)
        en_text2.pack(pady=10)