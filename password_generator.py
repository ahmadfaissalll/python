# PASSSWORD GENERATOR

# LIBRARY YANG DIGUNAKAN UNTUK ME-RANDOM WORDLIST
import random
# LIBRARY YANG DIGUNAKAN UNTUK MENGECEK FILE
import os
import sys

# WORDLIST
char = """q w e r t y u i o p a s d f g h j k l m z x c v b n Q W E R T Y U I O P A S D F G H J K L M Z X C V B N
         1 2 3 4 5 6 7 8 9 0 - _ ~ `! @ # $ % ^ & * ( )"""
# UNTUK MENGUBAH STRING DIATAS MENJADI LIST
char = char.split()


# UNTUK MENYIMPAN INPUT LENGTH UNTUK NANTI DIAMBIL OLEH FUNCTION
length = ""

# GENERATOR FUNCTION


def generator():
    # ME-RANDOM ITEM LIST 'char' DAN ME-RETURN SEBANYAK 8 CHARARACTER
    _random = random.choices(char, k=int(length))
    # MERUBAH TYPE LIST DARI RETURN VARIABLE DI ATAS MENJADI STRING
    _random = "".join(_random)
    # UNTUK MEMBUAT PERUBAHAN KE GLOBAL VARIABLE
    global result
    # MENAMBAHKAN NILAI VARIABLE 'y' KE VARIABLE 'result'
    result += _random


# TITLE
print("\n\tPASSWORD GENERATOR\n")


# SELAMA INPUT TIDAK SAMA DENGAN TERMINAL ATAU NOTEPAD MAKA PROGRAM INI AKAN TERUS DIEKSEKUSI
while True:
    # USER OPTION
    option_input = input("  Notepad or Terminal(Here): ")
    # JIKA INPUT SAMA DENGAN 'terminal' ATAU 'notepad' MAKA WHILE LOOPS INI AKAN BERHENTI
    if option_input.lower() == "terminal" or option_input.lower() == "notepad":
        # UNTUK MEN-STOP WHILE LOOPS
        break
    elif option_input.lower() == "quit":
        sys.exit()
    # JIKA INPUT TIDAK SAMA DENGAN 'terminal ATAU 'notepad' MAKA CODE INI KAAN DIEKSEKUSI
    else:
        print("     input tidak valid!!!".upper())


# INPUT LENGTH
# SELAMA TERJADI ERROR MAKA LENGTH AKAN DIKOSONGKAN DAN SELAMA LENGTH KOSONG MAKA INI AKAN TERUS DIEKSEKUSI
while length == "":
    # COBA INI
    try:
        # USER INPUT
        length_input = input("  Length:(type 'quit' to exit) ")
        if length_input.lower() == "quit":
            break
        # int(length_input)
        elif int(length_input) < 1:
            length_input = ""
        # JIKA TIDAK TERJADI ERROR PADA PROGRAM DI ATAS MAKA USER INPUT AKAN DITAMBAHKAN KE VARIABLE 'length'
        # UNTUK DIPAKAI OLEH FUNCTION NANTINYA
        length += str(length_input)
        # JIKA INPUT VALID MAKA PROGRAM WHILE INI BERHENTI KARENA BREAK DIBAWAH

    # JIKA TERJADI ERROR PADA PROGRAM DI ATAS MAKA TANGANI DENGAN INI
    except:
        # VARIABLE 'length' AKAN DIKOSONGKAN SEHINGGA LOOPS AKAN TERUS BERJALAN
        # TIDAK AKAN BERHENTI SAMPE USER HANYA MENGINPUT ANGKA
        length = ""
        # AND LAST PRINT INI
        print("\n\tinput tidak valid!!!".upper())

# STORE HASIL PASSWORD DISINI
result = str()

# LOOP COUNTER
a = 1


# PROGRAM UNTUK PRINT HASIL DI TERMINAL

# JIKA INPUT SAMA DENGAN 'terminal' KETIKA HURUF INPUT DIRUBAH KE HURUF KECIL DENGAN METHOD '.lower()' MAKA PROGRAM INI AKAN DIEKSEKUSI
if option_input.lower() == "terminal" and length_input != "quit":
    while True:
        # COBA EKSEKUSI INI TAPI JIKA TERJADI ERROR MAKA 'except' YANG AKAN MENANGANINYA
        try:
            # HOW MUCH DO YOU WANNA GENERATE (THIS IS USER INPUT)
            numb_input = input("\n\tHow much do you wanna generate:(type 'quit' to exit) ")
            # UNTUK KELUAR DARI PROGRAM
            if numb_input.lower() == "quit":
                break
            elif int(numb_input) < 1:
                numb_input = ""
            # INI AKAN DIEKSEKUSI SAMPAI LOOP COUNTER ('a') SAMA DENGAN 'numb_input'
            while a <= int(numb_input):
                # UNTUK MENULIS BARIS KOSONG (UNTUK JARAK) PADA LOOP PERTAMA (HANYA DIEKSEKUSI SEKALI)
                if a == 1:
                    print("")
                # CALLING FUNCTION YANG BERNAMA GENERATOR
                generator()
                # PRINT HASIL
                print(f"  {a}. {result}")
                # MENGOSONGKAN NILAI VARIABLE 'result' UNTUK MENYIMPAN HASIL LOOPS BERIKUTNYA
                result = ""
                # UNTUK MENAMBAHKAN NILAI 1 KE VARIABLE 'a' DI SETIAP LOOPS ( JIKA INI DIHAPUS MAKA PROGRAM TIDAK AKAN BERHENTI (INFINITY LOOPS) )
                a += 1
            else:
                a = 1
        # JIKA TERJADI ERROR PADA PROGRAM DI ATAS MAKA INI AKAN DIEKSEKUSI
        except:
            print("\n\t  input tidak valid!!! jangan masukkan selain angka atau angka dibawah 1".upper())


# PROGRAM UNTUK MENULIS HASIL DI NOTEPAD

# JIKA INPUT SAMA DENGAN 'terminal' KETIKA HURUF INPUT DIRUBAH KE HURUF KECIL DENGAN METHOD '.lower()' MAKA PROGRAM INI AKAN DIEKSEKUSI
if option_input.lower() == "notepad" and length_input.lower() != "quit":
    # COBA INI
    try:
        # HOW MUCH DO YOU WANNA GENERATE (THIS IS USER INPUT)
        numb_input = input("\n\tHow much do you wanna generate: ")
        # INI AKAN DIEKSEKUSI SAMPAI LOOP COUNTER ('a') SAMA DENGAN 'numb_input'
        while a <= int(numb_input):
            # UNTUK MENGECEK FILE PADA LOOP PERTAMA (HANYA DIEKSEKUSI SEKALI)
            if a == 1:
                if os.path.exists("password_result.txt"):
                    # JIKA FILE ADA MAKA HAPUS FILE
                    os.remove("password_result.txt")
            # CALLING FUNCTION YANG BERNAMA GENERATOR
            generator()
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

    # JIKA TERJADI ERROR PADA PROGRAM DI ATAS MAKA PENANGANANNYA DISERAHKAN KE SINI
    except:
        print("\n  input tidak valid".title())
