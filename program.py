from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("CheckList Application")
root.iconbitmap("check.ico")
root.geometry("500x500+400+100")
root.resizable(1, 1)

font = ("Kanit", 10)
color = "pink"
root.config(bg=color)

# ----------------------------- Functions -----------------------------
def addItem():
    data = inputEntry.get()
    if data.strip():
        Listbox.insert(END, data)
        inputEntry.delete(0, END)

def removeItem():
    Listbox.delete(ANCHOR)

def clearList():
    Listbox.delete(0, END)

def saveList():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        initialfile="text.txt",
        title="บันทึกไฟล์รายการ"
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            items = Listbox.get(0, END)
            for item in items:
                file.write(item + "\n")

def loadList():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="เปิดไฟล์รายการ"
    )
    if file_path:
        Listbox.delete(0, END)
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                Listbox.insert(END, line.strip())

# ----------------------------- Frames -----------------------------
input_frame = Frame(root, bg=color)
output_frame = Frame(root, bg=color)
button_frame = Frame(root, bg=color)

input_frame.pack(pady=10)
output_frame.pack()
button_frame.pack(pady=10)

# ----------------------------- Input Section -----------------------------
inputEntry = Entry(input_frame, width=25, font=font)
btnOpen = Button(input_frame, text="เปิดไฟล์", font=font, command=loadList)
btnAdd = Button(input_frame, text="เพิ่มรายการ", font=font, command=addItem)

btnOpen.grid(row=0, column=0, padx=5, pady=5, ipadx=10)
inputEntry.grid(row=0, column=1, padx=5, pady=5, ipady=5)
btnAdd.grid(row=0, column=2, padx=5, pady=5, ipadx=10)

# ----------------------------- Listbox Section -----------------------------
Listbox = Listbox(output_frame, width=35, height=12, font=font)
Listbox.grid(row=0, column=0, padx=5, pady=5)

# ----------------------------- Buttons Section -----------------------------
btnRemove = Button(button_frame, text="ลบรายการ", font=font, command=removeItem)
btnClear = Button(button_frame, text="ล้างรายการ", font=font, command=clearList)
btnSave = Button(button_frame, text="บันทึก", font=font, command=saveList)
btnQuit = Button(button_frame, text="ปิดโปรแกรม", font=font, command=root.destroy)

btnRemove.grid(row=0, column=0, padx=2, pady=2, ipadx=10)
btnClear.grid(row=0, column=1, padx=2, pady=2, ipadx=10)
btnSave.grid(row=0, column=2, padx=2, pady=2, ipadx=10)
btnQuit.grid(row=1, column=1, padx=2, pady=2, ipadx=10)

# ----------------------------- Run Application -----------------------------
root.mainloop()
