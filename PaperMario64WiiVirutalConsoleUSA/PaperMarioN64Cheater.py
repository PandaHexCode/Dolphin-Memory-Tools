import keyboard
import dolphin_memory_engine
import time

dolphin_memory_engine.hook()

key_state = {}

def get_key_down(key):
    global key_state

    if key not in key_state:
        key_state[key] = False

    if keyboard.is_pressed(key) and not key_state[key]:
        key_state[key] = True
        return True
    elif not keyboard.is_pressed(key) and key_state[key]:
        key_state[key] = False
    
    return False

start_time = time.time()
delta_time = 0

while True:
    loop_start_time = time.time()
    #Change position
    
    if keyboard.is_pressed('up'):
        dolphin_memory_engine.write_float(0x81324F14,  dolphin_memory_engine.read_float(0x81324F14) + (855 * delta_time))
    elif keyboard.is_pressed('down'):
       dolphin_memory_engine.write_float(0x81324F14,  dolphin_memory_engine.read_float(0x81324F14) - (355 * delta_time))
    
    if keyboard.is_pressed('a'):
        dolphin_memory_engine.write_float(0x81324F10,  dolphin_memory_engine.read_float(0x81324F10) - (155 * delta_time))
    elif keyboard.is_pressed('d'):
        dolphin_memory_engine.write_float(0x81324F10,  dolphin_memory_engine.read_float(0x81324F10) + (155 * delta_time))
    
    if keyboard.is_pressed('w'):
        dolphin_memory_engine.write_float(0x81324F18,  dolphin_memory_engine.read_float(0x81324F18) - (155 * delta_time))    
    elif keyboard.is_pressed('s'):
        dolphin_memory_engine.write_float(0x81324F18,  dolphin_memory_engine.read_float(0x81324F18) + (155 * delta_time))   

    if keyboard.is_pressed('t'): #FreeDialog
        dolphin_memory_engine.write_float(0x814F03B0,  0)   
    delta_time = time.time() - loop_start_time    