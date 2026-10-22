import tkinter as tk
import math

root = tk.Tk()
root.title("Кнопки по кругу")
root.geometry("500x500")
root.configure(bg="#202938")

center_x = 250
center_y = 250
radius = 150
count = 12
i = 0

while i < count:
    angle = 2 * math.pi * i / count
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    button = tk.Button(
        root,
        text=f"Кнопка {i + 1}",
        bg="#2563eb",
        fg="white",
        font=("Arial", 10, "bold"),
        width=10
    )
    button.place(x=x, y=y, anchor="center")
    i += 1

root.mainloop()