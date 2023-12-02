def incr(pwd):
    # check if we need to skip forward to avoid the first occurance of an invalid character
    skip = [s for s in (pwd.find('i'), pwd.find('l'), pwd.find('o')) if s > -1]
    if len(skip):
        skip = min(skip)
        pwd = pwd[0:skip] + chr(ord(pwd[skip]) + 1) + 'a'*(len(pwd) - skip - 1)
    # increment
    npwd = ''
    carry = 1
    for i in range(len(pwd) - 1, -1, -1):
        n = chr(ord(pwd[i]) + carry)
        if carry and n in ('i', 'l', 'o'): # skip an invalid character
           n = chr(ord(n) + 1)
        npwd = ('a' if n == '{' else n) + npwd
        carry = 1 if n == '{' else 0
    return npwd

def rule1(pwd):
    for i in range(len(pwd) - 2):
        if ord(pwd[i]) + 1 == ord(pwd[i + 1]) and ord(pwd[i]) + 2 == ord(pwd[i + 2]):
            return True
    return False

def rule2(pwd):
    return not ('i' in pwd and 'l' in pwd and 'o' in pwd)

def rule3(pwd):
    pairs = {}
    i = 0
    while True:
        if i > len(pwd) - 2:
            break
        i += 1
        if pwd[i - 1] == pwd[i]:
            pairs[pwd[i]] = 1
            i += 1
    return len(pairs) > 1

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
    for npwd in lines:
        for i in range(2):
            if i == 1:
                npwd = incr(npwd)
            while True:
                if all((rule1(npwd), rule2(npwd), rule3(npwd))):
                    break
                npwd = incr(npwd)
            print("Part {}: {}".format(i + 1,  npwd))
