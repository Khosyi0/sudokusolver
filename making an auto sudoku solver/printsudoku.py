import pyautogui

# Baca file sdkrslt.txt
with open('sdkrslt.txt', 'r') as file:
    lines = file.readlines()

# Membalikkan baris-genap
for i in range(1, len(lines), 2):
    lines[i] = ' '.join(lines[i].split()[::-1]) + '\n'
    
# Hapus karakter newline (\n) pada setiap baris
lines = [line.strip() for line in lines]

count = 0
# Perulangan untuk mengetikkan angka-angka secara berurutan
for line in lines:
    # Pisahkan angka-angka pada setiap baris
    numbers = line.split()

    # Perulangan untuk mengetikkan angka-angka pada setiap baris
    for number in numbers:
        # Mengetikkan angka
        pyautogui.typewrite(number)

        if count % 18 < 9:

            # Pindah ke kanan
            pyautogui.press('right')
        else:
            # Pindah ke kiri
            pyautogui.press('left')
            
        count += 1

    # Pindah ke bawah
    pyautogui.press('down')