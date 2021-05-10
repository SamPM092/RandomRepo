from tkinter import *
from random import randint

root = Tk()
root.title('Picking something')
# root.iconbitmap('d:icon.ico')
root.geometry("400x400")


jumlah1 = randint(1, 257)
jumlah2 = int(jumlah1)


topLabel = Label(root, text="Welcum", font=("Arial", 24))
topLabel.pack(pady=20)
beforeLabel = Label(root, text="Urutan anime selanjutnya adalah : ", font=("Helvetica", 15))
beforeLabel.pack(pady=10)
randLabel = Label(root, text=jumlah2, font=("Arial", 24))
randLabel.pack(pady=50)


root.mainloop()
