from copy import deepcopy

data = open('two.txt').read()
data = data.strip()
data = data.split(',')
data = [int(n) for n in data]
reset = deepcopy(data)

#print(data)



def run_computer(noun, verb, data):
    data[1], data[2] = noun, verb
    for n in range(0, len(data), 4):
        #print('Program Line: ' + str(n // 4))
        #print(data[n], data[n + 1], data[n + 2], data[n + 3])
        if data[n] == 1:
            x_idx, y_idx = data[n + 1], data[n + 2]
            #print('idxs: ' + str(x_idx) + ' ' + str(y_idx))
            x, y = data[x_idx], data[y_idx]
            #print(x, y)
            loc = data[n + 3]
            data[loc] = x + y
        if data[n] == 2:
            x_idx, y_idx = data[n + 1], data[n + 2]
            x, y = data[x_idx], data[y_idx]
            loc = data[n + 3]
            data[loc] = x * y
        if data[n] == 99:
            #print('Program Halted')
            #print('Position 0: ' + str(data[0]))
            #print(data)
            return data[0]

    
success = False    
for i in range(0, 100):
    for j in range(0, 100):
        test = deepcopy(data)
        #print('attempt: ' + str(i) + ' ' + str(j))
        result = run_computer(i, j, test)
        if result == 19690720:
            success = True
            print('answer:')
            print(i, j)
            break
    if success == True:
        break

print(run_computer(67, 18, data))
