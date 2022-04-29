import tkinter as tk
from message1 import Message

def on_submit():
    message = message_var.get()
    message = message.lower()
    if message == '':
        return
    my_message = Message(message, 3)
    encoded_var.set(my_message.encrypted)
    

root = tk.Tk()
root.title('Caeser Cipher')
root.geometry('600x600')
root.columnconfigure(1, weight=1)

#first row of information
message_label = tk.Label(
    root,
    text = 'Enter a message to encode:',
    font = ('Arial 16 bold'),
    bg = 'light blue',
    fg = 'black'
)
message_label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=25)
message_var = tk.StringVar(root) # holds the text message_input
message_input = tk.Entry(
        root,
        textvariable=message_var
)
message_input.grid(row=0, column=1, sticky=(tk.N,tk.E,tk.W,tk.S), padx=10)

# row 2
encoded_label = tk.Label(
    root,
    text = 'Your encoded message is here:',
    font = ('Arial 16 bold'),
    bg = 'light green',
    fg = 'black'
)
encoded_label.grid(row=1, column=0, sticky=(tk.W,tk.E), padx=25)
encoded_var = tk.StringVar(root) # holds the text message_input
encoded_input = tk.Entry(
        root,
        textvariable=encoded_var
)
encoded_input.grid(row=1, column=1, sticky=(tk.N,tk.E,tk.W,tk.S), padx=10)

#row 3
submit_btn = tk.Button(
    root,
    text = 'Encode'
)
submit_btn.grid(row=2,column=1, sticky=(tk.E), padx=10, pady=10)
submit_btn.configure(command=on_submit)

root.mainloop()