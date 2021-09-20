# COUNTDOWN TIMER SEDERHANA

import time
import keyboard

hour = time.localtime().tm_hour
minute = list(str(time.localtime().tm_min))
second = time.localtime().tm_sec

if len(minute) == 1:
    minute.insert(0,'0')

# TIPE DATA VARIABEL minute DIRUBAH DARI LIST MENJADI STRING
minute = "".join(minute)

# PR → NEXT TAMBAHKAN DETIK
a = 0

while True:
    a += 1
    print(a,'second')
    time.sleep(1)
    # TEKAN ESC SELAMA SEPERSEKIAN DETIK UNTUK MEM-STOP PROGRAM DENGAN BENAR
    if (keyboard.is_pressed('esc')):
        print(f'\ndari {hour}:{minute}:{second}')

        current_minute = (a // 60)
        current_second = (a % 60)

        if (a >= 60): ##
            print("\nselesai",current_minute, 'Menit', current_second,'detik')
            ##
        else: ##
            print("\nselesai",a, "detik")
        ##
        break