import dolphin_memory_engine
import sys

dolphin_memory_engine.hook()

def get_input(prompt, input_type):
    while True:
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            print("Invalid input.")

start_address = get_input("Please write the startAdress value: ", lambda x: int(x, 16))
test_value = get_input("Please write the test value: ", float)
step = get_input("Please write the step value: ", int)

offset = 0

print("Loop started, press ctrl + c to cancel.")

while True:
    dolphin_memory_engine.write_float(start_address + offset, test_value)
    #8042D4FCprint(hex(start_address + offset))
    offset += step
