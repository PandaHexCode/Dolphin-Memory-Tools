import dolphin_memory_engine
import random
import tkinter as tk
import time
from threading import Thread

dolphin_memory_engine.hook()

offset = 0
loop_paused = False

def start_stop_loop():
    global loop_active
    if not loop_active:
        start_loop()
    else:
        stop_loop()

def start_loop():
    global loop_active
    global start_address
    global test_value
    loop_active = True
    start_address_int = int(start_address.get(), 16)
    start_stop_button.config(text="Stop Loop")

    thread = Thread(target=loop, args=(start_address_int, offset))
    thread.start()

def stop_loop():
    global loop_active
    loop_active = False
    start_stop_button.config(text="Start Loop")

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
            test_value_rnd = random.randint(-5000, 5000)
            dolphin_memory_engine.write_float(memory_address, test_value_rnd)
            if reverse_checkbox_var.get():
                 offset -= random.randint(0, step_int)
            else:
                 offset += random.randint(0, step_int)
        else:
            dolphin_memory_engine.write_float(memory_address, test_value_int)      
            if reverse_checkbox_var.get():
                 offset -= step_int
            else:
                 offset += step_int
            
        window.update()
        loop_delay = float(delay.get())
        if loop_delay != 0.0:
           time.sleep(loop_delay)
           # window.after(int(loop_delay * 1000))

bg_color = '#333333'
fg_color = '#ffffff'

window = tk.Tk()
window.title("Dolphin-Destroyer")
window.config(bg=bg_color)

tk.Label(window, text="Start Address:", bg=bg_color, fg=fg_color).pack()
start_address = tk.StringVar()
start_entry = tk.Entry(window, textvariable=start_address)
if not start_entry.get():
    start_entry.insert(0, "80B48F6C")
start_entry.pack()

tk.Label(window, text="Test Value:", bg=bg_color, fg=fg_color).pack()
test_value = tk.StringVar()
test_entry = tk.Entry(window, textvariable=test_value)
if not test_entry.get():
    test_entry.insert(0, "700")
test_entry.pack()

tk.Label(window, text="Step/MaxSteps:", bg=bg_color, fg=fg_color).pack()
step = tk.StringVar()
step_entry = tk.Entry(window, textvariable=step)
if not step_entry.get():
    step_entry.insert(0, "4")
step_entry.pack()

tk.Label(window, text="Loop Delay:", bg=bg_color, fg=fg_color).pack()
delay = tk.DoubleVar()
delay_entry = tk.Entry(window, textvariable=delay)
if not delay_entry.get():
    delay_entry.insert(0, "0.0")
delay_entry.pack()

output_label = tk.Label(window, text="", bg=bg_color, fg=fg_color)
output_label.pack()

start_stop_button = tk.Button(window, text="Start Loop", command=start_stop_loop)
start_stop_button.pack()

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
