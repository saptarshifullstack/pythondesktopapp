#Saptarshi
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\USER\Documents\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Budget tracker")

window.geometry("700x600")
window.configure(bg = "#FFFFFF")

expenses = 1400

def submit_handler():
    global expenses
    new_expense_amt = float(entry_2.get())
    expenses += new_expense_amt
    income = canvas.itemcget("income", "text")
    # Convert the fetched value to an integer (assuming it's in the format "$ 4,032")
    income_value = int(income.split("$ ")[1].replace(",", ""))
    balance = float(income_value) - expenses
    canvas.itemconfig("expense", text=f"$ {expenses}")
    canvas.itemconfig("balance", text=f"$ {balance}")



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    700.0,
    71.0,
    fill="#4B2FF7",
    outline="")

canvas.create_text(
    24.0,
    17.0,
    anchor="nw",
    text="Budget tracker",
    fill="#FFFFFF",
    font=("MontserratRoman ExtraBold", 30 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    171.0,
    134.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    188.5,
    393.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E2E1D6",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=58.0,
    y=372.0,
    width=261.0,
    height=41.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    188.5,
    475.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E2E1D6",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=58.0,
    y=454.0,
    width=261.0,
    height=41.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    346.0,
    236.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    521.0,
    134.0,
    image=image_image_3
)

canvas.create_text(
    51.0,
    107.0,
    anchor="nw",
    text="Income",
    fill="#000000",
    font=("MontserratRoman Bold", 12 * -1)
)

canvas.create_text(
    51.0,
    210.0,
    anchor="nw",
    text="Balance",
    fill="#000000",
    font=("MontserratRoman Bold", 12 * -1)
)

canvas.create_text(
    401.0,
    107.0,
    anchor="nw",
    text="Expense",
    fill="#000000",
    font=("MontserratRoman Bold", 12 * -1)
)

canvas.create_text(
    51.0,
    129.0,
    anchor="nw",
    text="$ 5432",
    fill="#000000",
    font=("MontserratRoman Bold", 24 * -1),
    tags="income"
)

canvas.create_text(
    51.0,
    232.0,
    anchor="nw",
    text="$ 4032",
    fill="#000000",
    font=("MontserratRoman Bold", 24 * -1),
    tags="balance"
)

canvas.create_text(
    401.0,
    129.0,
    anchor="nw",
    text="$ 1400",
    fill="#000000",
    font=("MontserratRoman Bold", 24 * -1),
    tags="expense"
)

canvas.create_text(
    42.0,
    302.0,
    anchor="nw",
    text="Add expense",
    fill="#000000",
    font=("MontserratRoman Bold", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=submit_handler,
    relief="flat"
)
button_1.place(
    x=37.0,
    y=518.0,
    width=313.0,
    height=70.0
)

canvas.create_text(
    42.0,
    342.0,
    anchor="nw",
    text="Name",
    fill="#857272",
    font=("MontserratRoman Bold", 16 * -1)
)

canvas.create_text(
    42.0,
    424.0,
    anchor="nw",
    text="Amount ($)",
    fill="#857272",
    font=("MontserratRoman Bold", 16 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    567.0,
    437.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    642.0,
    35.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()
