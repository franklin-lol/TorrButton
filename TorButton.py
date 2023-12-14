import tkinter as tk
from subprocess import Popen, PIPE

def toggle_nipe():
    global nipe_running
    if nipe_running:
        # Останавливаем Nipe
        process = Popen(["sudo", "perl", "nipe.pl", "stop"], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode == 0:
            status_label.config(text="Nipe остановлен")
        else:
            status_label.config(text=f"Ошибка: {error.decode()}")
        nipe_running = False
    else:
        # Запускаем Nipe
        process = Popen(["sudo", "perl", "nipe.pl", "start"], stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode == 0:
            status_label.config(text="Nipe запущен")
        else:
            status_label.config(text=f"Ошибка: {error.decode()}")
        nipe_running = True

    toggle_button.config(text="Остановить" if nipe_running else "Запустить")

# Инициализация Tkinter
root = tk.Tk()
root.title("Nipe Control GUI")

nipe_running = False

# Создание виджетов
toggle_button = tk.Button(root, text="Запустить", command=toggle_nipe)
toggle_button.pack(pady=10)

status_label = tk.Label(root, text="Nipe не запущен")
status_label.pack(pady=10)

# Запуск главного цикла
root.mainloop()
