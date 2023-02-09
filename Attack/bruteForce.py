def calculate(exponent, base, mod):
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

