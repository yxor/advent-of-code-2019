

def fuel_required(mass):
    fuel = int(mass) // 3 - 2
    if fuel <= 0: # base case
        return 0
    
    return fuel + fuel_required(fuel)

with open("input.txt", "r") as f:
    print(sum(map(fuel_required, f.readlines())))
    # 4940159

