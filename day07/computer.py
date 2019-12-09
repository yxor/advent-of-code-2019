from queue import SimpleQueue, Empty
# the Intcode computer from day 5

class IntCodeComputer:
    POSITION_MODE = '0'
    VALUE_MODE = '1'

    def __init__(self, instructs):
        self.instructs = instructs
        self.pointer = 0
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
            if self.paused:
                break

    
    def execute(self):
        # parsing the arguments
        jumpFlag = True
        opcode = str(self.instructs[self.pointer])
        argc = self.argc(opcode)
        argv = self.instructs[self.pointer + 1: self.pointer + argc]
        args = [(k, v) for (k, v) in zip(argv, opcode.zfill(argc + 1)[:-2][::-1])]
        
        if opcode.endswith('1'):    # addition
            self.instructs[args[2][0]] = self.get_value(args[0]) + self.get_value(args[1])

        elif opcode.endswith('2'):  # multiplication
            self.instructs[args[2][0]] = self.get_value(args[0]) * self.get_value(args[1])

        elif opcode.endswith('3'):  # input
            if self.inputs.empty():
                raise Empty("something went wrong")
            self.instructs[args[0][0]] = self.inputs.get()

        elif opcode.endswith('4'):  # output
            self.inputs.put(self.get_value(args[0]))
            self.paused = True # pause the execution

        elif opcode.endswith('5'):  # jump if true
            if self.get_value(args[0]) != 0:
                jumpFlag = False
                self.instructs[self.pointer] = self.get_value(args[1])

        elif opcode.endswith('6'):  # jump if false
            if self.get_value(args[0]) == 0 :
                jumpFlag = False
                self.instructs[self.pointer] = self.get_value(args[1])

        elif opcode.endswith('7'):  # less than
            self.instructs[args[2][0]] = 1 if self.get_value(args[0]) < self.get_value(args[1]) else 0

        elif opcode.endswith('8'):  # equal
            self.instructs[args[2][0]] = 1 if self.get_value(args[0]) == self.get_value(args[1]) else 0
        
        elif opcode.endswith('99'):
            self.running = False

        if jumpFlag:
            self.pointer += argc
        else:
            self.pointer = self.instructs[self.pointer]
        

    def get_value(self, arg : tuple) -> int:
        if arg[1] == self.POSITION_MODE:
            return self.instructs[arg[0]]
        return arg[0]
        

    
    @staticmethod
    def argc(code : int) -> int:
        opcode = str(code)
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
