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


def lsfr_func(b1, b2, b3, b4, b5, b6, b7, b8):
    return xor_func(xor_func(xor_func(xor_func(xor_func(xor_func(xor_func(b1, b2), b3), b4), b5), b6), b7), b8)


start_seq_L1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # To be discovered by attack
start_seq_L2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # To be discovered by attack
start_seq_L3 = [0] * 17 # To be discovered by attack

"""
LFSR 1
"""
temp = []
out = start_seq_L1 + temp
print(out)
while len(out) < 100:
    out.append(1)
    print(out)

