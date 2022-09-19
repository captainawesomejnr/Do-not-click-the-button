import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Do not press this button.", width=40)
button.pack(padx=10, pady=10)
ClickCount = 0
def OnClick(event):
    global ClickCount
    ClickCount = ClickCount + 1
    if ClickCount == 1:
        button.configure(text="Seriously?! Do. Not. Press. It.")
    elif ClickCount == 2:
        button.configure(text="Gah! Next time, no more button.")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", OnClick)
window.mainloop()
