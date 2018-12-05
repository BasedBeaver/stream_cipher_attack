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


# LFSR feedback function is the same for all 3 LFSR's.
def lsfr_func(b1, b2, b3, b4, b5, b6, b7, b8):
    return xor_func(xor_func(xor_func(xor_func(xor_func(xor_func(xor_func(b1, b2), b3), b4), b5), b6), b7), b8)


def lsfr(a1, a2, a3, a4, a5, a6, a7, a8):
    temp = []
    out = start_seq_L1 + temp
    while len(out) < 193:
        f = lsfr_func(out[-a1], out[-a2], out[-a3], out[-a4], out[-a5], out[-a6], out[-a7], out[-a8])
        out.append(f)
    return len(out), out


start_seq_L1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # To be discovered by attack
start_seq_L2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # To be discovered by attack
start_seq_L3 = [0] * 17  # To be discovered by attack
res = "11101000000111110010000011000101110110100111000010001011001100011001111000010000" \
      "01011111010001010111101110101101101000101010101111001011011100011000111100000111" \
      "101111101110110000101010010101101"

print(lsfr(13, 11, 10, 7, 6, 4, 2, 1))
