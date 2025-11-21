input = """
5
5|10
10|20
5
"""

first_gear = int(input.strip().split("\n")[0])
gears = list(input.strip().split("\n")[1:-1])
print(gears)
gears = [[int(gear.split("|")[1]), int(gear.split("|")[0])] for gear in gears]
print(gears)
last_gear = int(input.strip().split("\n")[-1])
factor = 1
previous_gear = first_gear
print("hola", previous_gear)
for gear in gears:
    print("gear", gear)
    factor *= previous_gear / gear[0]
    previous_gear = gear[1]
    print(previous_gear)


print(previous_gear)

factor *= previous_gear / last_gear
print(factor)
print(100 / factor)