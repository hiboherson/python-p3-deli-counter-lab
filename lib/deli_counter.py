# lib/deli_counter.py

def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_string = "The line is currently: "
        line_string += " ".join(f"{i+1}. {name}" for i, name in enumerate(katz_deli))
        print(line_string)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        name = katz_deli.pop(0)
        print(f"Currently serving {name}.")
