#!/usr/bin/python3
## Usage

'''
DH_brute-force.py b^emodk=r
```

* b: the base (b>0)
* e: the exponent (leave as e)
* k: the divisor (k>0)
* r: the remainder (r>0)
'''
import sys

expo = sys.argv[1].split('mod')[0]
base = int(expo.split('^')[0])
equation = sys.argv[1].split('mod')[1]
mod = int(equation.split('=')[0])
equal = int(equation.split('=')[1])

def calculate(exponent):
    global base
    if exponent == 1:
        result = base % mod
        #print(str(base) + "^1mod" + str(mod) + "=" + str(result))
        two_power = 1
    for i in range(2, exponent + 1):
        if i == 2:
            result = (base ** i) % mod
            #print(str(base) + "^" + str(i) + "mod" + str(mod) + "=" + str(result))
            two_power = i
        elif i % (2 * two_power) == 0:
            result = (result * result) % mod
            #print(str(base) + "^" + str(i) + "mod" + str(mod) + "=" + str(result))
            two_power = i
    return result, two_power

exponent = 1
while True:
    print("trying", str(exponent))
    result_list = []
    power_list = []
    while True:
        max_power = 0
        for i in power_list:
            max_power += int(i)
        #print("max_power=" + str(max_power))
        exponent1 = exponent - max_power
        if exponent1 > 0:
            result, two_power = calculate(exponent1)
        else:
            break
        result_list.append(result)
        power_list.append(two_power)
        #print("result_list=" + str(result_list))
        #print("power_list=" + str(power_list) + "\n")

    result = result_list[0]
    if len(result_list) == 1:
        result = result % mod
    else:
        for i in range(0, len(result_list) - 1):
            result = (result * result_list[i+1]) % mod
    if result == equal:
        break
    exponent += 1

print("found e=" + str(exponent))
