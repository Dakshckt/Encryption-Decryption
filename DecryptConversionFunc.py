import tkinter as tk
from Decrypt import decrypt

def dn_convert(dn_text1 , dn_text2):
    data = dn_text1.get("1.0" , tk.END).strip()
    dn_text2.delete("1.0" , tk.END)
    obj = decrypt(data)
    result = obj.get_decrypted_data()
    dn_text2.insert(tk.END , result)
    dn_text1.delete("1.0" , tk.END)