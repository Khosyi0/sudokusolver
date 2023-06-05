import subprocess
import keyboard

# Fungsi untuk menjalankan program Sudoku
def run_sudoku_program():
    # Execute sudokusolver.py
    subprocess.run(["python", "sudokusolver.py"])

    # Execute printsudoku.py
    subprocess.run(["python", "printsudoku.py"])

# Fungsi yang akan dipanggil ketika tombol ditekan
def on_key_press(event):
    if event.name == 's':
        run_sudoku_program()

# Mengatur fungsi on_key_press sebagai listener saat tombol ditekan
keyboard.on_press(on_key_press)

# Menjalankan program secara berkelanjutan
keyboard.wait()
