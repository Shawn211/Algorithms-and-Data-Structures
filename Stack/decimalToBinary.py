from Stack import Stack


def binary_converter(dec_number):
    s = Stack()
    while dec_number > 0:
        remainder = dec_number % 2
        s.push(remainder)
        dec_number //= 2

    bin_string = ''
    while not s.is_empty():
        bin_string += str(s.pop())

    return bin_string


print(binary_converter(1))
print(binary_converter(21))
print(binary_converter(211))
