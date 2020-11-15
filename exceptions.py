def enter_exc():
    while True:
        try:
            n = float(input("Введите число: "))
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")

        else:
            return float(n)
