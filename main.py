from tkinter import *
from aes_util import encryptText, decryptText
from tkinter import filedialog


window = Tk()
window.geometry("420x420")
window.title("AES Cipher")

icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
window.config(background="black") # galima ir HEX

label = Label(window,
              text="AES Cipher",
              font=('Arial', 15, 'bold'),
              fg="#FF00FF",
              bg="black")
label.pack()
#lable.place(x=0, y=0)


def click():

    if messageT.get() == "" or key.get() == "":
        outputWindow.delete("1.0", END)
        outputWindow.insert("1.0", "Enter message and key")
        return


    if operationBtn.get() == 0:
        result = encryptText(messageT.get(), key.get(), mode.get(), keySize.get())
    else:
        result = decryptText(messageT.get(), key.get(), mode.get(), keySize.get())

    outputWindow.delete("1.0", END)
    outputWindow.insert("1.0", result)



def delete():
    messageT.delete(0, END)
    key.delete(0, END)
    outputWindow.delete("1.0", END)

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text File", "*.txt")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            file_msg = file.read()
        messageT.delete(0, END)
        messageT.insert(0, file_msg)


def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
    if filepath:
        file = open(filepath, "w", encoding="utf-8")
        file.write(outputWindow.get("1.0", END).strip())
        file.close()


operation = ["Encrypt", "Decrypt"]
operationBtn = IntVar(value=0)
for index in range(len(operation)):
    radioBtn = Radiobutton(window,
                         text=operation[index],
                         variable=operationBtn,
                         value=index,
                         fg="#FF00FF",
                         bg="black",
                         selectcolor="black",
                         activeforeground="#FF00FF",
                         activebackground="black")
    radioBtn.pack()



mode = StringVar()
mode.set("ECB")

mode_choice = OptionMenu(window, mode, "ECB", "CBC", "CFB")
mode_choice.config(font=('Arial', 7, 'bold'), fg="#FF00FF", bg="black",)
mode_choice.pack()

keySize = StringVar()
keySize.set("128 bits")

keySize_choice = OptionMenu(window, keySize, "128 bits", "192 bits", "256 bits")
keySize_choice.config(font=('Arial', 7, 'bold'), fg="#FF00FF", bg="black",)
keySize_choice.pack()

messageT = Entry(window,
                font=('Arial', 7, 'bold'),
                fg="black",
                bg="#FF00FF")
messageT.pack()

key = Entry(window,
            font=('Arial', 7, 'bold'),
            fg="black",
            bg="#FF00FF")
key.pack()
####### OPEN
openBtn = Button(window,text="OPEN", command=open_file,
                 font=('Arial', 7, 'bold'),
                 fg="#FF00FF",
                 bg="black",
                 activeforeground="#FF00FF")
openBtn.pack()
####### SAVE
saveBtn = Button(window,text="SAVE", command=save_file,
                 font=('Arial', 7, 'bold'),
                 fg="#FF00FF",
                 bg="black",
                 activeforeground="#FF00FF")
saveBtn.pack()
####### GO
button = Button(window,
                text="GO!",
                 command=click,
                 font=('Arial', 7, 'bold'),
                 fg="#FF00FF",
                 bg="black",
                 activeforeground="#FF00FF")
button.pack()




deleteBtn = Button(window,
                   text="Clear all",
                   command=delete,
                   font=('Arial', 7, 'bold'),
                   fg="#FF00FF",
                   bg="black",
                   activeforeground="#FF00FF")
deleteBtn.pack()

outputWindow = Text(window,
                     font=('Arial', 15, 'bold'),
                     fg="#FF00FF",
                     bg="black",)

outputWindow.pack()


window.mainloop()



