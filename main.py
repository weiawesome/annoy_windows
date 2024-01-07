import tkinter as tk
from tkinter import messagebox

annoy_titles = ["Annoy_windows", "Fooling program?", "Virus program?", "Normal annoy_windows"]
annoy_contents = ["This is a joke.",
                  "You have noticed that right?",
                  "Right, you can't close the windows.",
                  "HAHAHA~~~~",
                  "Actually you can close it.\nUsing taskkill or Enter the \"exit\" in the "
                  "field.\nHave a nice trip~",
                  ]

index = 0
entry_text = "Try to write something..."
button_text = "Try to click"
warning_title = "Warning"
warning_text = "You have clicked the button. But what so? HAHAHA~~~"
exit_text = "exit"
wrong_exit_text = "Wrong text in here. HAHAHA~~~"

font_size = 60
padding = [20, 10]


def center_window(r: tk.Tk, width: int = 400, height: int = 300):
    # 獲取螢幕尺寸以及計算中心點
    screen_width = r.winfo_screenwidth()
    screen_height = r.winfo_screenheight()

    # 計算視窗的x和y座標
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    r.geometry('%dx%d+%d+%d' % (width, height, x, y))


def create_main_window(i: int):
    window = tk.Tk()
    center_window(window, 400, 300)
    window.title(annoy_titles[min(i, len(annoy_titles) - 1)])

    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)

    window.grid_columnconfigure(0, weight=1)

    label = tk.Label(window, text=annoy_contents[min(i, len(annoy_contents) - 1)], font=font_size)
    label.grid(row=0, padx=padding[0], pady=padding[1], sticky="ew")

    def on_button_click():
        messagebox.showwarning(warning_title, warning_text)

    button = tk.Button(window, text=button_text, command=on_button_click)
    button.grid(row=1, padx=padding[0], pady=padding[1], sticky="ew")

    def on_entry_click(event):
        if entry.get() == entry_text:
            entry.delete(0, "end")
            entry.insert(0, '')
            entry.config(fg='black')

    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, entry_text)
            entry.config(fg='grey')

    def on_enter_press(event):
        current_text = entry.get()
        if current_text == exit_text:
            window.destroy()
            exit(1)
        else:
            messagebox.showwarning(warning_title, wrong_exit_text)

    entry = tk.Entry(window)
    entry.insert(0, entry_text)
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)
    entry.bind('<Return>', on_enter_press)
    entry.grid(row=2, padx=padding[0], pady=padding[1], sticky="ew")

    window.protocol("WM_DELETE_WINDOW", lambda: open_new_window(window, i))

    return window


def open_new_window(r: tk.Tk, i: int):
    r.destroy()
    new_root = create_main_window(i + 1)
    new_root.mainloop()


root = create_main_window(index)
root.mainloop()
