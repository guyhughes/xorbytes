KEY=bytearray("1984")
with open('raw.in', 'rb') as file:
    b = bytearray(file.read())

    for i in range(len(b)):
        b[i] ^= KEY[i%len(KEY)]


    open('xor.out','wb').write(b)


