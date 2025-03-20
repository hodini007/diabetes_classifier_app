



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\raiyan\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("750x550")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 750,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    87.0,
    750.0,
    547.0,
    fill="#B4FF8C",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    750.0,
    87.0,
    fill="#42F784",
    outline="")

canvas.create_text(
    20.0,
    17.0,
    anchor="nw",
    text="Diabetes Detector using machine learning",
    fill="#FF69DE",
    font=("Itim Regular", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    385.0,
    132.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFDD00",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=291.0,
    y=113.0,
    width=188.0,
    height=36.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    624.0,
    132.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#42F784",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=530.0,
    y=113.0,
    width=188.0,
    height=36.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    138.0,
    132.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FF69DE",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=44.0,
    y=113.0,
    width=188.0,
    height=36.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    138.0,
    207.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#7B8A53",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=44.0,
    y=188.0,
    width=188.0,
    height=36.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    138.0,
    282.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#66869E",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=44.0,
    y=263.0,
    width=188.0,
    height=36.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    624.0,
    282.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#E9BC54",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=530.0,
    y=263.0,
    width=188.0,
    height=36.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    385.0,
    207.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#698EFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=291.0,
    y=188.0,
    width=188.0,
    height=36.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    624.0,
    207.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#8A537E",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=530.0,
    y=188.0,
    width=188.0,
    height=36.0
)

canvas.create_text(
    35.0,
    90.0,
    anchor="nw",
    text="age(years)",
    fill="#000000",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    273.0,
    90.0,
    anchor="nw",
    text="gender(m/f)",
    fill="#000000",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    511.0,
    161.0,
    anchor="nw",
    text="hypertensive(y/n)",
    fill="#000000",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    30.0,
    234.0,
    anchor="nw",
    text="systolic_bp",
    fill="#000000",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    511.0,
    236.0,
    anchor="nw",
    text="diastolic_bp",
    fill="#000000",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    511.0,
    90.0,
    anchor="nw",
    text="blood sugar",
    fill="#000000",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    35.0,
    164.0,
    anchor="nw",
    text="BMI",
    fill="#000000",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    272.0,
    161.0,
    anchor="nw",
    text="family_diabetes(y/n)",
    fill="#000000",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    69.0,
    474.0,
    anchor="nw",
    text="Result",
    fill="#FFFFFF",
    font=("Itim Regular", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=269.0,
    y=352.0,
    width=232.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
