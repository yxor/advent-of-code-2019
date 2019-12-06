def parse_opcode(code):
    if code == 1:
        return lambda x, y : x + y
    if code == 2:
        return lambda x, y : x * y
    return None

def get_inputs():
    with open("input.txt", "r") as f:
        return [int(code) for code in  f.read().split(',')]

def get_result(noun, verb):
    int_code = get_inputs()
    int_code[1] = noun
    int_code[2] = verb

    for i in range(0, len(int_code), 4):
        op = parse_opcode(int_code[i])
        if op == None:
            break
        int_code[int_code[i + 3]] = op(int_code[int_code[i + 1]], int_code[int_code[i + 2]])
    
    return int_code[0]

if __name__=="__main__":
    result = 19690720
    for noun in range(0, 100):
        for verb in range(0, 100):
            if get_result(noun, verb) == result:
                print(noun * 100 + verb) # 3749
                exit(0)
