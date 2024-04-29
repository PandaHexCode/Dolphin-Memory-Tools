import dolphin_memory_engine
import random

dolphin_memory_engine.hook()

def get_input(prompt, input_type):
    while True:
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            print("Invalid input.")

start_address = get_input("Please write the startAdress value: ", lambda x: int(x, 16))

maxSteps = get_input("Please write the maxSteps: ", int)

offset = 0

print("Loop started, press ctrl + c to cancel.")

while True:
    test_value = random.randint(-5000, 5000)
    dolphin_memory_engine.write_float(start_address + offset, test_value)
    offset += random.randint(0, maxSteps)
