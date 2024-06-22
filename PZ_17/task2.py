from tkinter import *


def main(num):
    num_str = str(num)
    all_numbers = len(num_str)
    sum_numbers = 0
    for digit in num_str:
        sum_numbers += int(digit)
    return (
        f'Длина строки: {all_numbers}\n'
        f'Сумма цифр в строке: {sum_numbers}'
    )


def check_power():
    num = input_entry.get()
    if num.isdigit():
        result = main(int(num))
        label_print.config(text=result)
    else:
        label_print.config(text="ERROR: это не число")


window = Tk()
window.title('Практическая работа № 4 | Задание - 2')
window.geometry('300x250')

header_text = Label(text="Калькулятор вычисления:\nделения нацело и взятия остатка от "
                         "деления\nи нахождения количества\nи суммы его цифр."
                    )
header_text.pack(pady=10)

input_entry = Entry(width=10)
input_entry.pack(pady=10)

check_button = Button(text="Рассчитать", command=check_power)
check_button.pack(pady=5)

label_print = Label(text="")
label_print.pack(pady=10)

window.mainloop()
