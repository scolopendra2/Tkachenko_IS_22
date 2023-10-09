def main():
    """Дни недели пронумерованы следующим образом: 1 — понедельник,
2 — вторник, ..., 6 — суббота, 7 — воскресенье. Дано целое число K, лежащее в диапазоне
1-365. Определить номер дня недели для K-го дня года, если известно, что в этом году 1
января было субботой."""
    K = input("Введите номер дня года (1-365): ")

    if (not K.isdigit()) or (not 1 <= int(K) <= 365):  # Обработка исключений
        print('Error')
    else:
        # Номер дня недели первого января
        first_day = 6  # суббота

        # Находим номер дня недели для K-го дня года
        day_of_week = (int(K) + first_day - 1) % 7
        print(f'Номер дня недели для {K} дня года: {day_of_week if day_of_week != 0 else 7}')


if __name__ == '__main__':
    main()
