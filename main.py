import pyautogui
import keyboard
import time


def sinirsiz_tiklama(x,y,durdurma_tus):
    try:
        print("5 Saniye içinde ilgili sayfaya geçin.")
        time.sleep(5)
        while True:
            pyautogui.click(x,y)
            #time.sleep(0.1)
            if keyboard.is_pressed(durdurma_tus):
                print("Tıklama İşlemi Durduruldu.")
                break

    except KeyboardInterrupt:
        print("Tıklama İşlemi Durduruldu.")

ekran_x = 729
ekran_y = 691

durdurma_tus = "q"

print("Tiklama işlemi başlatildi. Durdurmak için '{}' tuşuna basin.".format(durdurma_tus))

sinirsiz_tiklama(ekran_x,ekran_y,durdurma_tus)