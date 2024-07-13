import tkinter as tk
from Encrypt import encrypt

def en_convert(en_text1 , en_text2 ):
    data = en_text1.get("1.0" , tk.END).strip()
    en_text2.delete("1.0" , tk.END)
    obj = encrypt(data)
    result = obj.get_encrypted_data()
    en_text2.insert(tk.END , result)
    en_text1.delete("1.0" , tk.END)