def xor_func(a, b):
    if not a != (not b):
        x = 1
    else:
        x = 0
    return x


def key_stream_gen(k1, k2, k3):
    res = []
    L1 = lsfr(k1, 13, 11, 10, 7, 6, 4, 2, 1)
    L2 = lsfr(k2, 15, 13, 11, 10, 7, 6, 4, 2)
    L3 = lsfr(k3, 17, 16, 13, 10, 8, 5, 4, 2)
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


def hamming_func(seq_1):
    sum = 0
    for i in range(0, 193):
        if seq_1[i] == int(res_seq[i]):
           sum = sum + 1
    return sum / 193


# Sequence given by assignment to find key for
res_seq = "11101000000111110010000011000101110110100111000010001011001100011001111000010000" \
      "01011111010001010111101110101101101000101010101111001011011100011000111100000111" \
      "101111101110110000101010010101101"

# """
# hc start sequences
# """
# hc_1 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]  # prob = 0.7098445595854922
# hc_2 = [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1]  # prob = 0.8186528497409327
# hc_3 = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]  # prob = 0.7098445595854922

# Calculating binary start sequence which produces the largest hamming value for LFSR 1
largest_lfsr1 = 0.0
k_1 = []
for x in range(0, 8192):
    b_string = [int(char) for char in list('{0:013b}'.format(x))]
    res = lsfr(b_string, 13, 11, 10, 7, 6, 4, 2, 1)
    prob = hamming_func(res)
    if prob > largest_lfsr1:
        largest_lfsr1 = prob
        k_1 = b_string
print(largest_lfsr1, k_1)

# Calculating binary start sequence which produces the largest hamming value for LFSR 2
largest_lfsr2 = 0.0
k_2 = []
for x in range(0, 32768):
    b_string = [int(char) for char in list('{0:015b}'.format(x))]
    res = lsfr(b_string, 15, 13, 11, 10, 7, 6, 4, 2)
    prob = hamming_func(res)
    if prob > largest_lfsr2:
        largest_lfsr2 = prob
        k_2 = b_string
print(largest_lfsr2, k_2)

# Calculating binary start sequence which produces the largest hamming value for LFSR 3
largest_lfsr3 = 0.0
k_3 = []
for x in range(0, 131072):
    b_string = [int(char) for char in list('{0:017b}'.format(x))]
    res = lsfr(b_string, 17, 16, 13, 10, 8, 5, 4, 2)
    prob = hamming_func(res)
    if prob > largest_lfsr3:
        largest_lfsr3 = prob
        k_3 = b_string
print(largest_lfsr3, k_3)

# Check if our derived key produces the same sequence
res_total = key_stream_gen(k_1, k_2, k_3)
res_string = ""
for digit in res_total:
    res_string += str(digit)
print(res_string)
print(res_seq)
if res_string == res_seq:
    print("Attack successful")
