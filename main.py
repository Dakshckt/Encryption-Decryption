import tkinter as tk
from tkinter.ttk import *
from EncryptionDisplay import encryptionDisplay
from DecryptionDisplay import decryptionDisplay

base = tk.Tk()
base.title("Encryption and decryption")
base.geometry("400x400")


nb = Notebook()

Encryption = Frame(nb)
Decryption = Frame(nb)

EncryptObj = encryptionDisplay(Encryption)
decryptObj = decryptionDisplay(Decryption)

Encryption.pack(fill=tk.BOTH , expand=True)
Decryption.pack(fill=tk.BOTH , expand=True)


nb.pack(fill=tk.BOTH , expand=True)

nb.add(Encryption , text="Encryption")
nb.add(Decryption , text="Decryption")

base.mainloop()