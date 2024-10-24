from functools import reduce

data = open('one.txt').readlines()
data = [int(item.strip()) for item in data]

result = reduce(lambda x, y: ((y // 3) - 2) + x, data, 0)

acc = 0

for n in data:
    initial_fuel = ((n // 3) - 2)
    acc += initial_fuel
    while initial_fuel > 0:
        new_fuel = (initial_fuel // 3) - 2
        if new_fuel > 0:
            acc += new_fuel
        initial_fuel = new_fue
        
print(result)
print(acc)
