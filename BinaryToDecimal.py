# REGEX (REGULAR EXPRESSION) LIBRARY
import re

# BINER INPUT
biner_input = input("\nMasukkan angka biner: ")

# REGEX UNTUK MENCARI DAN MENGEKSTRAK 0, 1 dan space
y = re.findall("[0-1- ]", biner_input)

# REGEX UNTUK MENCARI DAN MENGEKSTRAK 0 DAN 1
x = re.findall("[0-1]", biner_input)

# LIST BINER
binerList = list(x)

# AGAR URUTANNYA SAMA DENGAN URUTAN SAAT BINER DIINPUT
binerList.reverse()

# UNTUK PANGKAT
a = 0

# UNTUK MENYIMPAN HASIL OPERASI
result = list()
# UNTUK MENJUMLAHKAN SEMUA ANGKA DI VARIABLE 'result' DI ATAS
result = sum(result)

# FOR LOOPS (HANYA BERJALAN KETIKA ADA NILAI '1' YANG DIINPUT)
for x in binerList:
    # SETIAP DI 'binerList' DIKALIKAN 2 PANGKAT 0 DST
    operasi = int(x) * pow(2,a)
    # MENAMBAHKAN HASIL OPERASI KE VARIABLE 'result'
    result += operasi
    # MENAMBAHKAN NILAI PANGKAT
    a += 1

# AGAR URUTAN BINER SESUAI DENGAN SAAT BINER DIINPUT
binerList.reverse()
# UNTUKK MERUBAH LIST KE STRING
y = "".join(y)
# PRINT HASIL
print(f"\n{y} in binary = {result} in decimal")