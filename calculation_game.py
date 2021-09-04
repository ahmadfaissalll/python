# PERKALIAN GAME

# LIBRARY UNTUK ME-RANDOM
import random

# DIEKSEKUSI TERUS SAMPAI MENGETIKKAN 'quit'
while True:
    # UNTUK MENYIMPAN 2 ANGKA HASIL RANDOM YANG AKAN DIKALIKAN
    question = list()
    # HANYA DIEKSEKUSI DUA KALI SETIAP SATU PUTARAN WHILE LOOP
    for x in range(2):
        # ME-RANDOM ANGKA DARI 1 SAMPAI 10
        y = random.randint(1, 10)
        # MENAMBAHKAN HASIL RANDOM KE LIST 'question'
        question.append(y)
    # USER INPUT
    input_value = input(f"\nberapa hasil {question[0]} x {question[1]}? (type quit to exit) ")

    # MENGEMBALIKAN HASIL OPERASI PERKALIAN
    operasi = question[0] * question[1]

    # JIKA USER INPUT == 'quit' MAKA LOOP BERHENTI
    if input_value.lower() == "quit":
        break

    # COBA INI
    try:
        if int(input_value) == operasi:
            # JIKA JAWABAN BENAR MAKA EKSEKUSI PROGRAM DIBAWAH INI
            print("Jawaban benar")

        # JIKA PERNYATAAN IF DI ATAS False MAKA EKSEKUSI INI
        else:
            print("Jawaban salah")

    # JIKA TERJADI ERROR PADA PROGRAM DIATAS MAKA HANDLING NYA DISERAHKAN KE PROGRAM INI
    except:
        print("INPUT TIDAK VALID")