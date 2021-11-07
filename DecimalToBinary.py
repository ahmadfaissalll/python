# Decimal To Binary Converter

def decimal_to_binary(decimal):

    decimal = int(decimal)

    result = ''

    while ( decimal ):
        result += str(decimal % 2)
        decimal //= 2

    while ( len(result) < 8 ):
        result += '0'

    return result[::-1]


print('\nBinary:','.'.join(map(decimal_to_binary, input('Decimal: ').split('.'))))
