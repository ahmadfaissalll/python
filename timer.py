import time
import keyboard

tm = time.localtime()

hour = tm.tm_hour
minute = list(str(tm.tm_min))
second = tm.tm_sec


if len(minute) == 1:
    minute.insert(0,'0')

# TIPE DATA VARIABEL minute DIRUBAH DARI LIST MENJADI STRING
minute = "".join(minute)

a = 0

while True:
    a += 1
    mytm = time.localtime()
    print(f"{a} second")
    time.sleep(1)
    # TEKAN ESC SELAMA SEPERSEKIAN DETIK UNTUK MEM-STOP PROGRAM DENGAN BENAR
    if (keyboard.is_pressed('esc')):
        print(f'\ndari {hour}:{minute}:{second}')
        print(f'sampe {mytm.tm_hour}:{mytm.tm_hour}:{mytm.tm_sec}')
        current_minute = (a // 60)
        current_second = (a % 60)

        if (a >= 60): ##
            print("\nselesai",current_minute, 'Menit', current_second,'detik')
            ##
        else: ##
            print(f"\nselesai {a} detik")
        ##
        break
