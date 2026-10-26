intercepted_ciphertext = [0xfe, 0x6c, 0xe1, 0xb0, 0xa5, 0x17]
intercepted_iv = 0xdd

known_values: list[tuple[str, int, list[int]]] = [
    ('garden', 0x2d, [0xdb, 0xfe, 0x6c, 0xc8, 0x32, 0x11]),
    ('planet', 0x1d, [0x2a, 0x0d, 0xe2, 0x6c, 0x9c, 0x7f]),
    ('silver', 0x3b, [0xde, 0xdf, 0xca, 0x8d, 0x7f, 0xe1]),
    ('bridge', 0x18, [0x7e, 0xec, 0xb0, 0x44, 0x2b, 0xd3]),
    ('dream', 0x0c, [0x81, 0xeb, 0xb4, 0xa5, 0x4c]),
    ('cloud', 0xb5, [0x17, 0xc9, 0xa3, 0x17, 0xd6]),
    ('orange', 0x02, [0x2a, 0xf0, 0x63, 0xe1, 0x52, 0xd1])
]

byte_cipher: list[int] = [-1 for _ in range(256)]


def print_byte_cipher() -> None:
    for i in range(16):
        print(f'{' '.join([hex(byte_cipher[i * 16 + j]) for j in range(16)])}')


def main():
    for (plaintext, iv, ciphertext) in known_values:
        last_c = iv
        for i in range(len(ciphertext)):
            m = ord(plaintext[i])
            c = ciphertext[i]
            byte_cipher[(m ^ last_c) % 256] = c
            last_c = c

    # print_byte_cipher()

    plaintext = ''
    last_c = intercepted_iv
    for c in intercepted_ciphertext:
        m = byte_cipher.index(c) ^ last_c
        plaintext += chr(m)
        last_c = c

    print(plaintext)


if __name__ == '__main__':
    main()
