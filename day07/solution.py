from computer import IntCodeComputer
from itertools import permutations
path = 'input.txt'

## part one
with open(path, "r") as f:
    inputs = [int(element) for element in f.read().split(',')]
best = 0
for setting in permutations([0, 1, 2, 3, 4]):
    signal = 0
    for phase in setting:
        computer = IntCodeComputer(inputs[:])
        computer.add_input(phase)
        computer.add_input(signal)
        computer.run()
        signal = computer.get_output()
    
    if signal > best:
        best = signal


print(best) # 17440

## part 2


best = 0
for setting in permutations([5, 6, 7, 8, 9]):
    with open(path, "r") as f:
        inputs = [int(element) for element in f.read().split(',')]
    computers = [IntCodeComputer(inputs[:]) for _ in range(5)]
    signal = 0
    for phase, computer in zip(setting, computers):
        computer.add_input(phase)
    while computers[-1].running:
        for computer in computers:
            computer.add_input(signal)
            computer.run()
            signal = computer.get_output()

    if signal > best:
        best = signal


print(best) # 27561242
