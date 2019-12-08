from computer import IntCodeComputer
from itertools import permutations
path = 'input.txt'

## part one

best = 0
for setting in permutations([0, 1, 2, 3, 4]):
    signal = 0
    for phase in setting:
        computer = IntCodeComputer(path)
        computer.add_input(phase)
        computer.add_input(signal)
        computer.run()
        signal = computer.get_output()
    
    if signal > best:
        best = signal


print(best) # 17440

