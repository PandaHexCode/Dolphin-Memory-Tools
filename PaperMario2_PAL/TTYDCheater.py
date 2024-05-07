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
        dolphin_memory_engine.write_float(0x80B48F70,  dolphin_memory_engine.read_float(0x80B48F70) + (855 * delta_time))
    elif keyboard.is_pressed('down'):
       dolphin_memory_engine.write_float(0x80B48F70,  dolphin_memory_engine.read_float(0x80B48F70) - (355 * delta_time))
    
    if keyboard.is_pressed('a'):
        dolphin_memory_engine.write_float(0x80B48F6C,  dolphin_memory_engine.read_float(0x80B48F6C) - (155 * delta_time))
    elif keyboard.is_pressed('d'):
        dolphin_memory_engine.write_float(0x80B48F6C,  dolphin_memory_engine.read_float(0x80B48F6C) + (155 * delta_time))
    
    if keyboard.is_pressed('w'):
        dolphin_memory_engine.write_float(0x80B48F74,  dolphin_memory_engine.read_float(0x80B48F74) - (155 * delta_time))    
    elif keyboard.is_pressed('s'):
        dolphin_memory_engine.write_float(0x80B48F74,  dolphin_memory_engine.read_float(0x80B48F74) + (155 * delta_time))       
    
    #Speed
    if keyboard.is_pressed('1'):
        dolphin_memory_engine.write_float(0x8042D4FC,  1.2)    
    if keyboard.is_pressed('2'):
        dolphin_memory_engine.write_float(0x8042D4FC,  3)        
    if keyboard.is_pressed('3'):
        dolphin_memory_engine.write_float(0x8042D4FC,  15)        
    if keyboard.is_pressed('4'):
        dolphin_memory_engine.write_float(0x8042D4FC,  5)     

    if keyboard.is_pressed('t'): #FreeDialog
        dolphin_memory_engine.write_float(0x80B48EE0,  1.40129846e-45)
        dolphin_memory_engine.write_float(0x80B48EEF,  0)        
        dolphin_memory_engine.write_float(0x80B48F18,  0)           
        dolphin_memory_engine.write_float(0x800366EC,  -1.59394449e-38)  
        dolphin_memory_engine.write_float(0x803E4D90,  3.58732407e-43)  
    delta_time = time.time() - loop_start_time    