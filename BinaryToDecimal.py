# Binary to Decimal Converter

def binary_to_decimal(binary):
    result = 0
    pangkat = len(binary) - 1

    for bit in binary:
        result += int(bit) * pow(2, pangkat)
        pangkat -= 1

    return str(result)
        
print('\nDecimal:', '.'.join(map(binary_to_decimal, input("Binary (separated by '.'): ").split('.'))))
