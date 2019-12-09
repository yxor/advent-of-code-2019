from computer import IntCodeComputer

## Part one

HEAP_SIZE = 1000
with open("input.txt", "r") as f:
    inputs = [int(element) for element in f.read().split(',')] + [0 for _ in range(HEAP_SIZE)]

computer = IntCodeComputer(inputs[:])
computer.add_input(1)
computer.run()
print(computer.get_output()) # 2662308295
