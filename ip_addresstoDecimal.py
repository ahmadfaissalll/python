# TITLE
print("\n\tIP ADDRESS TO BINER CONVERTER\n")

# USER INPUT
ipaddress_input = input("Enter IP Address (separated by dot): ")

# MENGUBAH USER INPUT MENJADI LIST (NOTE: ANGKA AKAN BERUBAH MENJADI STRING)
list_ip = ipaddress_input.split(".")

# USER INPUT UNTUK DITAMPILKAN KEMBALI DI AKHIR
ipaddress_result = ipaddress_input

# UNTUK MENYIMPAN HASIL
result = str()

# LOOPING SEBANYAK ITEM DI LIST 'list_ip'
for x in list_ip:
    # UNTUK MENYIMPAN VALUE VARIABLE 'x' AGAR BISA HABIS DIBAGI
    ip = int(x)
    # SELAMA VARIABLE 'ip' LEBIH DARI 0 LOOP AKAN TERUS DIEKSEKUSI
    while ip > 0:
        # VARIABLE YANG ME-RETURN SISA BAGI DARI VALUE VARIABLE 'ip' DIBAGI 2
        operasi = ip % 2
        # MENAMBAHKAN HASIL OPERASI KE VARIABLE 'result' (VARIABLE HASIL'
        result += str(operasi)
        # AGAR VARIABLE 'ip' TERUS BERKURANG SAMPE NILAINYA 0
        ip //= 2
        # UNTUK MENAMBAHKAN SPASI SETIAP SATU OPERASI
        if ip == 0:
            result += " "
# UNTUK MERUBAH STRING MENJADI LIST
result = result.split()

# UNTUK MENYIMPAN HASIL AKHIR (INI YANG AKAN DIPRINT)
hasil_akhir = str()

# AGAR ANGKA DESIMAL 1 (IN TABLE IN MY MIND) DIMULAI DARI KIRI (MEMBALIK SETIAP STRING)
for i in result:
    x = list(i)
    x.reverse()
    x = "".join(x)
    hasil_akhir += x + " "

# PRINT HASIL
print(f"\n{ipaddress_result} = {hasil_akhir} biner")