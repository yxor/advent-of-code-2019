

with open("input.txt", "r") as f:
    print(sum(map(lambda x : int(x) // 3 - 2, f.readlines())))
    # 3295424