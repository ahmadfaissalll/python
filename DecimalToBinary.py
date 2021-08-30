# Decimal To Binary Converter

# TITLE
print("\n\tDecimal To Binary Converter")
# DECIMAL INPUT
decimal_input = input("\nMasukkan angka desimal: ")

# AGAR JARAK ANTARA INPUT DAN OPERASI OPERASI TIDAK BERDEKATAN
print("")

# UNTUK MENAMPUNG ANGKA UNTUK DITAMPILKAN DI AKHIR
decimal_result = decimal_input
numbers = ""

# LOGIKA OPERASI
try:
    while int(decimal_input) > 0:
        operasi1 = int(decimal_input) // 2
        operasi2 = int(decimal_input) % 2
        numbers += str(operasi2)
        print(f"{decimal_input} / 2 = {operasi1} sisa bagi = {operasi2}")
        decimal_input = int(decimal_input)
        decimal_input //= 2

except ValueError:
    raise Exception("Input tidak valid!!!".upper())

# AGAR URUTANNYA BENAR
numbers = list(numbers)
numbers.reverse()
numbers = "".join(numbers)

# HASIL AKHIR
print(f"\n{decimal_result} in decimal = {numbers} in binary")