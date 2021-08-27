# PASSSWORD GENERATOR

# LIBRARY YANG DIGUNAKAN UNTUK MEN-GENERARATE WORDLIST
import random
# LIBRARY YANG DIGUNAKAN UNTUK MENGECEK FILE
import os

# WORDLIST
names = "q w e r t y u i o p a s d f g h j k l m z x c v b n 1 2 3 4 5 6 7 8 9 0 - _ ~ `! @ # $ % ^ & * ( )"
# WORDLIST 2 (UPPERCASE LETTER)
names2 = "q w e r t y u i o p a s d f g h j k l m z x c v b n".upper()
# UNTUK MENGUBAH STRING DIATAS MENJADI LIST
names = names.split()
names2 = names2.split()
# MENG-COMBINE LIST 'names2' KE LIST 'names'
names.extend(names2)

# STORE HASIL PASSWORD DISINI
result = str()

# LOOP COUNTER
a = 1

# TITLE
print("\n\tPASSWORD GENERATOR\n")

# VARIABLE UNTUK MENYIMPAN HASIL DARI VALUE VARIABLE YANG SAMA YANG ADA DI WHILE
option_input = ""

# SELAMA INPUT TIDAK SAMA DENGAN TERMINAL ATAU NOTEPAD MAKA PROGRAM INI AKAN TERUS DIEKSEKUSI
while option_input != "terminal" or option_input != "notepad":
    # USER OPTION
    option_input = input("  Notepad or Terminal(Here): ")
    # JIKA INPUT SAMA DENGAN 'terminal' ATAU 'notepad' MAKA WHILE LOOPS INI AKAN BERHENTI
    if option_input.lower() == "terminal" or option_input.lower() == "notepad":
        # UNTUK MEN-STOP WHILE LOOPS
        break
    # JIKA INPUT TIDAK SAMA DENGAN 'terminal ATAU 'notepad' MAKA CODE INI AKAN DIEKSEKUSI
    elif option_input != "terminal" or option_input != "notepad":
        print("\n     input tidak valid!!!\n".upper())


# PROGRAM UNTUK PRINT HASIL DI TERMINAL

# JIKA INPUT SAMA DENGAN 'terminal' KETIKA HURUF INPUT DIRUBAH KE HURUF KECIL DENGAN METHOD '.lower()' MAKA PROGRAM INI AKAN DIEKSEKUSI
if option_input.lower() == "terminal":
    # COBA EKSEKUSI INI TAPI JIKA TERJADI ERROR MAKA 'except' YANG AKAN MENANGANINYA
    try:
        # HOW MUCH DO YOU WANNA GENERATE (THIS IS USER INPUT)
        numb_input = int(input("\n\tHow much do you wanna generate: "))
        # INI AKAN DIEKSEKUSI SAMPAI LOOP COUNTER ('a') SAMA DENGAN 'numb_input'
        while a <= numb_input:
            # UNTUK MENULIS BARIS KOSONG (UNTUK JARAK) PADA LOOP PERTAMA (HANYA DIEKSEKUSI SEKALI)
            if a == 1:
                print("")
            # FOR LOOPS UNTUK MEN-GENERATE PASSWORD DAN MENYIMPAN HASILNYA DI VARIABLE 'result'
            for x in range(1, 9):
                # AGAR SESUAI DENGAN JUMLAH ITEM DI LIST 'names' MENURUT INDEX
                index = len(names) - 1
                # ME-RANDOM ANGKA SEBANYAK INDEX ITEM DI LIST 'names'
                _random = random.randint(0, index)
                # MENGHAPUS ITEM YANG TELAH DI-RANDOM DAN ME-RETURNNYA (TUJUAN CODE INI ADALAH AGAR ITEM
                # YANG TELAH DI RANDOM BISA DITAMBAHKAN KE VARIABLE 'result' (VARIABLE UNTUK MENYIMPAN HASIL PASSWORD))
                y = names.pop(_random)
                # MEMASUKKAN KEMBALI ITEM YANG TELAH DIHAPUS DI ATAS KE LIST (AGAR ITEM TIDAK BERKURANG)
                names.insert(_random, y)
                # MENAMBAHKAN NILAI VARIABLE 'y' KE VARIABLE 'result'
                result += y
            # PRINT HASIL
            print(f"  {a}. {result}")
            # MENGOSONGKAN NILAI VARIABLE 'result' UNTUK MENYIMPAN HASIL LOOPS BERIKUTNYA
            result = ""
            # UNTUK MENAMBAHKAN NILAI 1 KE VARIABLE 'a' DI SETIAP LOOPS ( JIKA INI DIHAPUS MAKA PROGRAM TIDAK AKAN BERHENTI (INFINITY LOOPS) )
            a += 1
    # JIKA TERJADI ERROR PADA PROGRAM DI ATAS MAKA INI AKAN DIEKSEKUSI
    except:
        print("\n  input tidak valid".title())


# PROGRAM UNTUK MENULIS HASIL DI NOTEPAD

# JIKA INPUT SAMA DENGAN 'terminal' KETIKA HURUF INPUT DIRUBAH KE HURUF KECIL DENGAN METHOD '.lower()' MAKA PROGRAM INI AKAN DIEKSEKUSI
elif option_input.lower() == "notepad":
    try:
        # HOW MUCH DO YOU WANNA GENERATE (THIS IS USER INPUT)
        numb_input = int(input("\n\tHow much do you wanna generate: "))
        # INI AKAN DIEKSEKUSI SAMPAI LOOP COUNTER ('a') SAMA DENGAN 'numb_input'
        while a <= numb_input:
            # UNTUK MENGECEK FILE PADA LOOP PERTAMA (HANYA DIEKSEKUSI SEKALI)
            if a == 1:
                if os.path.exists("password_result.txt"):
                    # JIKA FILE ADA MAKA HAPUS FILE
                    os.remove("password_result.txt")
            # FOR LOOPS UNTUK MEN-GENERATE PASSWORD DAN MENYIMPAN HASILNYA DI VARIABLE 'result'
            for x in range(1, 9):
                # AGAR SESUAI DENGAN JUMLAH ITEM DI LIST 'names' MENURUT INDEX
                index = len(names) - 1
                # ME-RANDOM ANGKA SEBANYAK INDEX ITEM DI LIST 'names'
                _random = random.randint(0, index)
                # MENGHAPUS ITEM YANG TELAH DI-RANDOM DAN ME-RETURNNYA (TUJUAN CODE INI ADALAH AGAR ITEM
                # YANG TELAH DI RANDOM BISA DITAMBAHKAN KE VARIABLE 'result' (VARIABLE UNTUK MENYIMPAN HASIL PASSWORD))
                y = names.pop(_random)
                # MEMASUKKAN KEMBALI ITEM YANG TELAH DIHAPUS DI ATAS KE LIST (AGAR ITEM TIDAK BERKURANG)
                names.insert(_random, y)
                # MENAMBAHKAN NILAI VARIABLE 'y' KE VARIABLE 'result'
                result += y
            # MENULIS KE NOTEPAD
            f = open("password_result.txt", "a")
            f.write(f"{a}. {result}\n")
            # MENGOSONGKAN NILAI VARIABLE 'result' UNTUK MENYIMPAN HASIL LOOPS BERIKUTNYA
            result = ""
            # UNTUK MENAMBAHKAN NILAI 1 KE VARIABLE 'a' DI SETIAP LOOPS ( JIKA INI DIHAPUS MAKA PROGRAM TIDAK AKAN BERHENTI (INFINITY LOOPS) )
            a += 1
        # INI AKAN DIEKSEKUSI KETIKA LOOPS SELESAI
        else:
            print("\n  Written Done")

    # JIKA TERJADI ERROR PADA PROGRAM DI ATAS MAKA INI AKAN DIEKSEKUSI
    except:
        print("\n  input tidak valid".title())