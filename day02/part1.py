

def parse_opcode(code):
    if code == 1:
        return lambda x, y : x + y
    if code == 2:
        return lambda x, y : x * y
    
    return None

with open("input.txt", "r") as f:
    int_code = [int(code) for code in  f.read().split(',')]
    int_code[1] = 12
    int_code[2] = 2

    for i in range(0, len(int_code), 4):
        op = parse_opcode(int_code[i])
        if op == None:
            break
        int_code[int_code[i + 3]] = op(int_code[int_code[i + 1]], int_code[int_code[i + 2]])
    
    print(int_code[0])
    # 6730673
