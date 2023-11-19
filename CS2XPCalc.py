from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

root = Tk()
root.title('CS2 XP Calculator')
root.geometry('210x210')
root.resizable(False, False)

# lists with modes and boost for Combobox
mode_list = ["Premier/Competitive", "Wingman", "Casual", "Deathmatch"]
boost_list = ["Max boost (x4)", "Normal boost (x2)", "No boost (x1)", "Penalty (x0.175)"]

# default vars for Combobox
default_mode = StringVar(value=mode_list[0])
default_rounds = IntVar(value=0)
default_boost = StringVar(value=boost_list[0])

def update_label(event): # function for update round_label 
    mode = mode_combobox.get()

    if mode == "Premier/Competitive":
        round_label['text'] = 'Rounds won:'
    elif mode == "Wingman":
        round_label['text'] = 'Rounds won:'
    elif mode == "Casual":
        round_label['text'] = 'Score:'
    elif mode == "Deathmatch":
        round_label['text'] = 'Score:'
    else:
        round_label['text'] = 'Rounds won:'

def exp_calc(): # function for calculate experience
    mode = mode_combobox.get()
    boost = boost_combobox.get()

    if mode == "Premier/Competitive":
        exp = 30
    elif mode == "Wingman":
        exp = 15
    elif mode == "Casual":
        exp = 4
    elif mode == "Deathmatch":
        exp = 0.2
    else: 
        showerror(title="CS2 XP Calculator", message="Error! Please select game mode!")

    if boost == "Max boost (x4)":
        boost = 4
    elif boost == "Normal boost (x2)":
        boost = 2
    elif boost == "No boost (x1)":
        boost = 1
    elif boost == "Penalty (x0.175)":
        boost = 0.175
    else:
        showerror(title="CS2 XP Calculator", message="Error! Please select XP multiplier")

    while True: 
        try:
            rounds = int(rounds_entry.get())
            if rounds > 0:
                result = (exp*rounds)*boost
                result_label['text'] = "Result:", result, "exp"
            else:
                showerror(title="CS2 XP Calculator", message="Error! Please enter a number greater than 0")
            break
        except ValueError: # detecting text in round_entry and show error
            showerror(title="CS2 XP Calculator", message="Error! Please enter a number")
            break

mode_label = Label(root, text='Game mode:', font='Verdana 12')
mode_combobox = ttk.Combobox(root, font='Verdana 10', values=mode_list, textvariable=default_mode)
round_label = Label(root, text='Rounds won:', font='Verdana 12')
rounds_entry = Entry(root, font='Verdana 10', textvariable=default_rounds)
boost_label = Label(root, text='XP multiplier:', font='Verdana 12')
boost_combobox = ttk.Combobox(root, font='Verdana 10', values=boost_list, textvariable=default_boost)
calc_button = Button(root, text='Calculate', width=10, height=1, command=exp_calc)
result_label = Label(root, text='Result: 0 exp', font='Verdana 12')

mode_combobox.bind("<<ComboboxSelected>>", update_label) # "bind" for update_label function

mode_label.pack()
mode_combobox.pack()
round_label.pack()
rounds_entry.pack()
boost_label.pack()
boost_combobox.pack()
calc_button.pack(pady=10)
result_label.pack()

root.mainloop()