import re


max_password = 675869
min_password = 172851

# part 1
# dummy way (very very very slow)
valids = 0
for password in range(min_password, max_password):
    ## one double at least
    flag = False
    found = False
    for i in range(len(str(password)) - 1):
        if(str(password)[i] == str(password)[i+1]):
            found = True
        
        if(str(password)[i] > str(password)[i+1]):
            flag = True
    if flag:
        continue

    if not found:
        continue

    valids += 1

#print(valids) # 1660



# part 2
# dummy way (very very very slow also)
valids = 0
for password in range(min_password, max_password):
    pswd = str(password)
    flag = False
    found = False
    for i in range(len(pswd) - 1):
        if(pswd[i] == pswd[i+1] and (i == 0 or  pswd[i-1] != pswd[i]) and (i+2 == len(pswd) or pswd[i+2] != pswd[i])):
            found = True
        
        if(str(password)[i] > str(password)[i+1]):
            flag = True
    if flag:
        continue

    if not found:
        continue

    valids += 1


print(valids) # 1135
    

    