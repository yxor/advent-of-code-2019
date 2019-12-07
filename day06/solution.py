d = dict()
with open("input.txt", "r") as f:
    d = {line.split(')')[1]:line.split(')')[0] for line in f.read().split('\n')}

## part one
sum = 0
for k in d.keys():
    temp = k
    while temp != 'COM':
        sum += 1
        temp = d[temp]

print(sum) # 200001

## part two

sum = 0
you = 'YOU'
san = 'SAN'
you_path = []
san_path = []
while you != 'COM':
    you = d[you]
    you_path.append(you)

while san != 'COM':
    san = d[san]
    san_path.append(san)

intersection = next((value for value in you_path if value in san_path)) 


print(you_path.index(intersection) + san_path.index(intersection)) # 379
