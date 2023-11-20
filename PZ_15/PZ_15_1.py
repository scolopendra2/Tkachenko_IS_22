""".Из заданной строки отобразить только символы пунктуации. Использовать
библиотеку string.
Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"
"""
import sqlite3


def main():
    connect = sqlite3.connect('base.db')
    cursor = connect.cursor()

    try:
        cursor.execute("""CREATE TABLE Товары (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        название VARCHAR,
                        описание VARCHAR,
                        единица_измерения VARCHAR);""")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы:", e)

    try:
        cursor.execute("""CREATE TABLE Магазины (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        название VARCHAR,
                        адрес VARCHAR,
                        телефон VARCHAR);""")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы:", e)

    try:
        cursor.execute("""CREATE TABLE Заявки_магазинов (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        id_магазина INT,
                        дата_заявки DATE,
                        FOREIGN KEY (id_магазина) REFERENCES Магазины(id));""")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы:", e)

    try:
        cursor.execute("""CREATE TABLE Количество_товаров_на_складе (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        id_товара INT,
                        количество INT,
                        FOREIGN KEY (id_товара) REFERENCES Товары(id));""")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы:", e)

    try:
        cursor.execute("""CREATE TABLE Состав (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            id_заявки INT,
                            id_товара INT,
                            количество INT,
                            FOREIGN KEY (id_товара) REFERENCES Товары(id),
                            FOREIGN KEY (id_заявки) REFERENCES Заявки_магазинов(id));""")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы:", e)

    result = cursor.execute("""SELECT название, описание FROM Товары""").fetchall()
    print(result)
    print()

    result = cursor.execute("""SELECT название, адрес FROM Магазины""").fetchall()
    print(result)
    print()

    result = cursor.execute("""SELECT Магазины.название, Заявки_магазинов.дата_заявки
                                FROM Заявки_магазинов
                                JOIN Магазины ON Заявки_магазинов.id_магазина = Магазины.id;
                            """).fetchall()
    print(result)
    print()

    result = cursor.execute("""SELECT Товары.название, Количество_товаров_на_складе.количество
                                    FROM Количество_товаров_на_складе
                                    JOIN Товары ON Количество_товаров_на_складе.id_товара = Товары.id
                                    ORDER BY Количество_товаров_на_складе.количество DESC;
                                """).fetchall()
    print(result)
    print()

    result = cursor.execute("""SELECT Магазины.название, Товары.название
                                        FROM Состав
                                        JOIN Товары ON Состав.id_товара = Товары.id
                                        JOIN Заявки_магазинов ON Состав.id_заявки = Заявки_магазинов.id
                                        JOIN Магазины ON Заявки_магазинов.id_магазина = Магазины.id;
                                    """).fetchall()
    print(result)
    print()

    result = cursor.execute(f"""SELECT Товары.название
                                FROM Товары
                                JOIN Количество_товаров_на_складе
                                ON Товары.id = Количество_товаров_на_складе.id_товара
                                WHERE Количество_товаров_на_складе.количество < 
                                {input('Минимальное допустимое количество товара:')};
                                """).fetchall()
    print(result)
    print()

    result = cursor.execute(f"""SELECT Заявки_магазинов.id, Магазины.название
                                    FROM Заявки_магазинов
                                    JOIN Магазины ON Заявки_магазинов.id_магазина = Магазины.id
                                    WHERE Заявки_магазинов.дата_заявки == '{input('Введите дату заявки:')}';
                                    """).fetchall()
    print(result)
    print()

    result = cursor.execute(f"""SELECT Магазины.название
                                FROM Магазины
                                JOIN Заявки_магазинов ON Магазины.id = Заявки_магазинов.id_магазина
                                JOIN Состав ON Заявки_магазинов.id = Состав.id_заявки
                                JOIN Количество_товаров_на_складе ON Состав.id_товара = 
                                Количество_товаров_на_складе.id_товара
                                GROUP BY Магазины.название
                                HAVING SUM(Количество_товаров_на_складе.количество) < 
                                {input('Введите суммарное количесвто товаров на складе:')};
                                        """).fetchall()
    print(result)
    print()

    product = input('Введите название товара: ')
    cursor.execute(f"""UPDATE Количество_товаров_на_складе
                        SET количество = {input('Введите новое количество товаров: ')}
                        WHERE id_товара IN (SELECT id FROM Товары WHERE название = '{product}');
                    """)

    id_z = input('Введите id заявки: ')
    product_name = input('Введите имя товара: ')
    new_product_name = input('Введите новое имя товара: ')
    cursor.execute(f"""UPDATE Товары
                    SET название = '{new_product_name}'
                    WHERE id IN (SELECT id_товара FROM Состав
                    WHERE id_заявки = {id_z}) AND название = '{product_name}'""")

    id_z = input('Введите id заявки: ')
    product_name = input('Введите имя товара: ')
    kol_vo = input('Введите новое количество товара: ')
    cursor.execute(f"""UPDATE Состав
                        SET количество = '{kol_vo}'
                        WHERE id_заявки = {id_z} AND id_товара IN
                        (SELECT id FROM Товары WHERE название = '{product_name}')""")

    id_z = input('Введите id заявки: ')
    new_adress = input('Введите новый адрес магазина: ')
    cursor.execute(f"""UPDATE Магазины
                        SET адрес = '{new_adress}'
                        WHERE id IN (SELECT id_магазина FROM Заявки_магазинов
                    #WHERE id = {id_z})""")

    id_z = input('Введите id заявки: ')
    name_magaz = input('Введите название магазина: ')
    new_date = input('Введите новую дату заявки: ')
    cursor.execute(f"""UPDATE Заявки_магазинов
                            SET дата_заявки = '{new_date}'
                            WHERE id_магазина IN (SELECT id FROM Магазины
                            WHERE название = '{name_magaz}') AND id = {id_z}""")

    product_list = input('Введите id товара через ",": ')
    new_kolvo = input('Введите новое количество товаров: ')
    cursor.execute(f"""UPDATE Количество_товаров_на_складе
                      SET количество = {new_kolvo}
                      WHERE id_товара IN ({product_list})""")

    """В SQLite нельзя выполнить одновременное обновление двух таблиц в одном SQL-запросе. 
    Вам придется выполнить два отдельных запроса для обновления каждой таблицы."""
    product = input('Введите название товара: ')
    op = input('Введите новое описание товара: ')
    new_kolvo = input('Введите новое количество товара: ')
    cursor.execute(f"""UPDATE Товары
                        SET описание = '{op}'
                        WHERE название = '{product}'
                    """)
    cursor.execute(f"""UPDATE Количество_товаров_на_складе
                        SET количество = {new_kolvo}
                        WHERE id_товара IN (SELECT id FROM Товары
                        WHERE название = '{product}');
                        """)

    id_z = input('Введите id заявки: ')
    new_kolvo = input('Введите новое количество товара: ')
    cursor.execute(f"""UPDATE Количество_товаров_на_складе
                            SET количество = {new_kolvo}
                            WHERE id_товара IN (SELECT id_товара FROM Состав
                            WHERE id_заявки = {id_z});
                            """)

    id_z = input('Введите id заявки: ')
    new_kolvo = input('Введите новое количество товара: ')
    product_name = input('Введите название товара: ')
    cursor.execute(f"""UPDATE Количество_товаров_на_складе
                        SET количество = {new_kolvo}
                        WHERE id_товара IN (SELECT id_товара FROM Состав
                        WHERE id_заявки = {id_z}) AND id_товара IN
                        (SELECT id FROM Товары WHERE название = '{product_name}');
                        """)

    id_z = input('Введите id заявки: ')
    new_name = input('Введите новое название магазина: ')
    new_adress = input('Введите новый адрес магазина: ')
    cursor.execute(f"""UPDATE Магазины
                        SET название = '{new_name}',
                        адрес = '{new_adress}'
                        WHERE id IN (SELECT id_магазина FROM Заявки_магазинов
                        WHERE id = {id_z})""")

    # 11. Обновить название магазина в заявке, которую подал конкретный магазин
    # кривое задание у нас в заявке нет названия магазина, а название магазина напрямую изменятеся через
    # таблицу магазины, тогда при чём строка про заявки???

    # снова, название магазина я могу обновить через название товара, и айди заявки
    # (я так понял заявки это таблица состав) но это не рационально ибо название обновляется напрямую
    # запросом к таблице Магазины

    product_name = input('Введите название товара: ')
    new_kol_vo = input('Введите новое количество товара: ')
    cursor.execute(f"""UPDATE Состав
                            SET количество = '{new_kol_vo}'
                            WHERE id_товара IN (SELECT id FROM Товары
                            WHERE название = '{product_name}')""")

    connect.commit()


if __name__ == '__main__':
    main()
