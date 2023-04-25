import tkinter as tk

class SelectCareButton:
    def __init__(self, master, pheresis_category):
        self.master = master
        self.pheresis_category = pheresis_category
        
        for button_title in self.pheresis_category:
            button = tk.Button(self.master, text=button_title, command=lambda button_title=button_title: self.button_clicked(button_title))
            button.pack()
            
        self.label = tk.Label(self.master, text="")
        self.label.pack()        

        
    def button_clicked(self, button_title):
        self.label.configure(text=button_title)
        
root = tk.Tk()

pheresis_category = ["CHDF", "PMX", "CART"," PE "] # ここにボタンに表示するタイトルをリストとして格納します
app = SelectCareButton(root, pheresis_category)

root.mainloop()

import tkinter as tk

class RadioButtonsFrame(tk.Frame):
    def __init__(self, master=None, options=[]):
        super().__init__(master)
        self.selected_option = tk.StringVar()
        self.selected_option.set(options[0])
        for option in options:
            tk.Radiobutton(self, text=option, variable=self.selected_option, value=option, command=self.show_selected_option).pack(side=tk.LEFT)
        self.label = tk.Label(self)
        self.label.pack(side=tk.LEFT)

    def show_selected_option(self):
        self.label.config(text="選択されたオプション: " + self.selected_option.get())

if __name__ == '__main__':
    options = ['オプション1', 'オプション2', 'オプション3']
    root = tk.Tk()
    radio_buttons_frame = RadioButtonsFrame(root, options)
    radio_buttons_frame.pack()
    root.mainloop()
