from queue import SimpleQueue, Empty
# the Intcode computer from day 5

class IntCodeComputer:
    POSITION_MODE = '0'
    VALUE_MODE = '1'
    RELATIVE_MODE = '2'
    PAUSE_ON_OUTPUT = True

    def __init__(self, instructs):
        self.instructs = instructs
        self.pointer = 0
        self.relative_base = 0
        self.running = True
        self.paused = False
        self.inputs = SimpleQueue()

    def add_input(self, n):
        self.inputs.put(n)
    
    def get_output(self):
        if self.inputs.empty():
            raise Empty("something went wrong")
        return self.inputs.get()

    def run(self):
        self.paused = False
        while self.running:
            self.execute()
            if self.paused and self.PAUSE_ON_OUTPUT:
                break

    
    def execute(self):
        # parsing the arguments
        jumpFlag = True
        opcode = str(self.instructs[self.pointer])
        argc = self.argc(opcode)
        argv = self.instructs[self.pointer + 1: self.pointer + argc]
        args = [(k, v) for (k, v) in zip(argv, opcode.zfill(argc + 1)[:-2][::-1])]

        if opcode.endswith('99'):
            self.running = False

        elif opcode.endswith('1'):   # addition
            self.instructs[self.get_position(args[2])] = self.get_value(args[0]) + self.get_value(args[1])

        elif opcode.endswith('2'):  # multiplication
            self.instructs[self.get_position(args[2])] = self.get_value(args[0]) * self.get_value(args[1])

        elif opcode.endswith('3'):  # input
            if self.inputs.empty():
                raise Empty("something went wrong: no inputs")
            self.instructs[self.get_position(args[0])] = self.inputs.get()

        elif opcode.endswith('4'):  # output
            self.inputs.put(self.get_value(args[0]))
            self.paused = True # pause the execution

        elif opcode.endswith('5'):  # jump if true
            if self.get_value(args[0]) != 0:
                jumpFlag = False
                self.pointer = self.get_value(args[1])

        elif opcode.endswith('6'):  # jump if false
            if self.get_value(args[0]) == 0 :
                jumpFlag = False
                self.pointer = self.get_value(args[1])

        elif opcode.endswith('7'):  # less than
            self.instructs[self.get_position(args[2])] = 1 if self.get_value(args[0]) < self.get_value(args[1]) else 0

        elif opcode.endswith('8'):  # equal
            self.instructs[self.get_position(args[2])] = 1 if self.get_value(args[0]) == self.get_value(args[1]) else 0
        
        elif opcode.endswith('9'): # add to the relative position
            self.relative_base += self.get_value(args[0])


        if jumpFlag:
            self.pointer += argc

        


    def get_position(self, arg : tuple) -> int:
        if arg[1] == self.POSITION_MODE:
            return arg[0]
        if arg[1] == self.RELATIVE_MODE:
            return arg[0] + self.relative_base

        raise Exception(f"something went wrong in getting the position {arg}")

    def get_value(self, arg : tuple) -> int:
        if arg[1] == self.POSITION_MODE:
            return self.instructs[arg[0]]

        if arg[1] == self.RELATIVE_MODE:
            return self.instructs[arg[0] + self.relative_base]

        if arg[1] == self.VALUE_MODE:
            return arg[0]
        
        raise Exception(f"something went wrong in getting the value {arg}")


    
    @staticmethod
    def argc(opcode : str) -> int:

        if opcode.endswith('99'):
            return 1
        if opcode.endswith('1'):
            return 4
        if opcode.endswith('2'):
            return 4
        if opcode.endswith('3'):
            return 2
        if opcode.endswith('4'):
            return 2
        if opcode.endswith('5'):
            return 3
        if opcode.endswith('6'):
            return 3
        if opcode.endswith('7'):
            return 4
        if opcode.endswith('8'):
            return 4
        if opcode.endswith('9'):
            return 2
        
        raise Exception(f"Unvalid opcode {opcode}")
