import pyautogui
import time

def koordinat_al():
    print("2 Saniye içinde konuma fareyi ulaştırın.")
    time.sleep(2)
    x,y = pyautogui.position()
    print("Tıklanan Koordinatlar:",x,y)
    return x,y


ekran_x,ekran_y = koordinat_al()

print("Ekranın koordinatları:", ekran_x, ekran_y)