import dolphin_memory_engine
import random
import tkinter as tk

dolphin_memory_engine.hook()

offset = 0
loop_paused = False

def start_loop():
    global loop_active
    global start_address
    global test_value
    loop_active = True
    start_address_int = int(start_address.get(), 16)
    loop(start_address_int, offset)

def stop_loop():
    global loop_active
    loop_active = False

def toogle_pause_loop():
    global loop_paused
    if loop_paused:
        loop_paused = False
        pause_resume_button.config(text="Pause Loop")
    else:
        loop_paused = True
        pause_resume_button.config(text="Resume Loop")

def rehook():
    if dolphin_memory_engine.is_hooked == False:
        dolphin_memory_engine.hook()


def loop(start_addr, offset):
    global loop_active
    global test_value
    global test_value_int
    global step
    global step_int

    while loop_active:
        test_value_int = float(test_value.get())
        step_int = int(step.get())

        memory_address = start_addr + offset
        region = hex(memory_address & -4096)
        output_label.config(text=region + "\n" + hex(memory_address))

        if loop_paused:
            window.update()
            continue

        if random_checkbox_var.get():
            test_value = random.randint(-5000, 5000)
            dolphin_memory_engine.write_float(memory_address, test_value)
            if reverse_checkbox_var.get():
                 offset -= random.randint(0, step_int)
            else:
                 offset += random.randint(0, step_int)
        else:
            dolphin_memory_engine.write_float(memory_address, step_int)      
            if reverse_checkbox_var.get():
                 offset -= step_int
            else:
                 offset += step_int
            
        window.update()

bg_color = '#333333'
fg_color = '#ffffff'

window = tk.Tk()
window.title("Dolphin-Destroyer")
window.config(bg=bg_color)

tk.Label(window, text="Start Address:", bg=bg_color, fg=fg_color).pack()
start_address = tk.StringVar()
start_entry = tk.Entry(window, textvariable=start_address)
start_entry.pack()

tk.Label(window, text="Test Value:", bg=bg_color, fg=fg_color).pack()
test_value = tk.StringVar()
test_entry = tk.Entry(window, textvariable=test_value)
test_entry.pack()

tk.Label(window, text="Step/MaxSteps:", bg=bg_color, fg=fg_color).pack()
step = tk.StringVar()
step_entry = tk.Entry(window, textvariable=step)
step_entry.pack()

output_label = tk.Label(window, text="", bg=bg_color, fg=fg_color)
output_label.pack()

start_button = tk.Button(window, text="Start Loop", command=start_loop)
start_button.pack()

cancel_button = tk.Button(window, text="Stop Loop", command=stop_loop)
cancel_button.pack()

pause_resume_button = tk.Button(window, text="Pause Loop", command=toogle_pause_loop)
pause_resume_button.pack()

random_checkbox_var = tk.BooleanVar()
random_checkbox = tk.Checkbutton(window, text="Randomize", variable=random_checkbox_var)
random_checkbox.pack()

reverse_checkbox_var = tk.BooleanVar()
reverse_checkbox = tk.Checkbutton(window, text="Reverse", variable=reverse_checkbox_var)
reverse_checkbox.pack()

rehook_button = tk.Button(window, text="Rehook", command=rehook)
rehook_button.pack()

loop_active = False

window.mainloop()
