from Stack import Stack


def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while dec_number > 0:
        remainder = dec_number % base
        s.push(remainder)
        dec_number //= base

    bin_string = ''
    while not s.is_empty():
        bin_string += str(digits[s.pop()])

    return bin_string


print(base_converter(211, 2))
print(base_converter(211, 8))
print(base_converter(211, 16))
