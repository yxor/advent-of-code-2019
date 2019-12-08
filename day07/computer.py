from queue import SimpleQueue
# the Intcode computer from day 5

class IntCodeComputer:
    POSITION_MODE = '0'
    VALUE_MODE = '1'

    def __init__(self, path_to_code):
        with open(path_to_code, "r") as f:
            self.instructs = f.read().split(',')
        self.pointer = 0
        self.running = True
        self.inputs = SimpleQueue()

    def add_input(self, n):
        self.inputs.put(n)
    
    def get_output(self):
        return self.inputs.get()

    def run(self):
        while self.running:
            self.execute()

    
    def execute(self):
        # parsing the arguments
        jumpFlag = True
        opcode = self.instructs[self.pointer]
        argc = self.argc(opcode)
        argv = self.instructs[self.pointer + 1: self.pointer + argc]
        args = [(k, v) for (k, v) in zip(argv, opcode.zfill(argc + 1)[:-2][::-1])]
        
        if opcode.endswith('1'):    # addition
            self.instructs[int(args[2][0])] = str(self.get_value(args[0]) + self.get_value(args[1]))
        elif opcode.endswith('2'):  # multiplication
            self.instructs[int(args[2][0])] = str(self.get_value(args[0]) * self.get_value(args[1]))
        elif opcode.endswith('3'):  # input
            self.instructs[int(args[0][0])] = self.inputs.get()

        elif opcode.endswith('4'):  # output

            self.inputs.put(self.get_value(args[0]))
        elif opcode.endswith('5'):  # jump if true
            if self.get_value(args[0]) != 0:
                jumpFlag = False
                self.instructs[self.pointer] = str(self.get_value(args[1]))
        elif opcode.endswith('6'):  # jump if false
            if self.get_value(args[0]) == 0 :
                jumpFlag = False
                self.instructs[self.pointer] = str(self.get_value(args[1]))
        elif opcode.endswith('7'):  # less than
            self.instructs[int(args[2][0])] = '1' if self.get_value(args[0]) < self.get_value(args[1]) else '0'
        elif opcode.endswith('8'):  # equal
            self.instructs[int(args[2][0])] = '1' if self.get_value(args[0]) == self.get_value(args[1]) else '0'
        
        elif opcode.endswith('99'):
            self.running = False

        if jumpFlag:
            self.pointer += argc
        else:
            self.pointer = int(self.instructs[self.pointer])
        

    def get_value(self, arg : tuple) -> int:
        if arg[1] == self.POSITION_MODE:
            return int(self.instructs[int(arg[0])])
        return int(arg[0])
        

    
    @staticmethod
    def argc(opcode : str) -> int:
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
        if opcode.endswith('99'):
            return 1
        
        return None
