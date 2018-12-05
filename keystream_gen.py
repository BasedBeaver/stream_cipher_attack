def xor_func(a, b):
    if not a != (not b):
        x = 1
    else:
        x = 0
    return x


def and_func(a, b):
    if a and b:
        x = 1
    else:
        x = 0
    return x


"""
L1
"""
start_seq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # To be discovered by attack
seq = []
print(len(start_seq))
while len(res_f2) < 10000:
    s1, s2 = res_f2[-4], res_f2[-3]
    f = f2_func(s1, s2)
    res_f2.append(f)
    c1, c2, c3 = res_f2[-4], res_f2[-3], res_f2[-2]
    if c1 == 0 and c2 == 0 and c3 == 0:
        res_NL_f2.append(0)
    res_NL_f2.append(f)
if (res_f2[0] == 0 and res_f2[1] == 0 and res_f2[-1] == 0) or\
        (res_f2[0] == 0 and res_f2[-2] == 0 and res_f2[-1] == 0):
    res_NL_f2.append(0)