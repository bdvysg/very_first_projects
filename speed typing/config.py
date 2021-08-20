import tkinter as tk
root = tk.Tk()
root.maxsize(250,700)
root.minsize(250,150)
listFrame = tk.Frame(root, width = 250, bg='green')  # цвет для наглядности
playerFrame = tk.Frame(root,width = 250, height=100)
listFrame.pack(fill="both", side="top", expand=True)
playerFrame.pack(side="bottom")
a = tk.Button(listFrame, text="bad")
a.pack(side="top")
b = tk.Button(playerFrame,text="good")
b.pack(side="top")
root.mainloop()