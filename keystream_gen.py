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


def or_func(a, b):
    if a or b:
        return 1
    else:
        return 0


def key_stream_gen():
    res = []
    L1 = lsfr(start_seq_L1, 13, 11, 10, 7, 6, 4, 2, 1)
    L2 = lsfr(start_seq_L2, 15, 13, 11, 10, 7, 6, 4, 2)
    L3 = lsfr(start_seq_L3, 17, 16, 13, 10, 8, 5, 4, 2)
    for i in range(0, 193):
        if L1[i] + L2[i] + L3[i] >= 2:
            res.append(1)
        else:
            res.append(0)
    return res


# LFSR feedback function is the same for all 3 LFSR's.
def lsfr_func(b1, b2, b3, b4, b5, b6, b7, b8):
    return xor_func(xor_func(xor_func(xor_func(xor_func(xor_func(xor_func(b1, b2), b3), b4), b5), b6), b7), b8)


# LFSR, given start seq and feedback indices
def lsfr(start_seq, a1, a2, a3, a4, a5, a6, a7, a8):
    temp = []
    out = start_seq + temp
    while len(out) < 193:
        f = lsfr_func(out[-a1], out[-a2], out[-a3], out[-a4], out[-a5], out[-a6], out[-a7], out[-a8])
        out.append(f)
    return out


start_seq_L1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # K1, to be discovered by attack
start_seq_L2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # K2, to be discovered by attack
start_seq_L3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # K3, to be discovered by attack

# Sequence given by assignment to find key for
res = "11101000000111110010000011000101110110100111000010001011001100011001111000010000" \
      "01011111010001010111101110101101101000101010101111001011011100011000111100000111" \
      "101111101110110000101010010101101"

# L1 = (13, 11, 10, 7, 6, 4, 2, 1)
print(lsfr(start_seq_L1, 13, 11, 10, 7, 6, 4, 2, 1))

# L2 = (15, 13, 11, 10, 7, 6, 4, 2)
print(lsfr(start_seq_L2, 15, 13, 11, 10, 7, 6, 4, 2))

# L3 = (17, 16, 13, 10, 8, 5, 4, 2)
print(lsfr(start_seq_L3, 17, 16, 13, 10, 8, 5, 4, 2))

print(key_stream_gen())
