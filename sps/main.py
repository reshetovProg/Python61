import random
import os

clear = lambda: os.system('cls')
game_type=int(input('какой будет режим игры? 1-игрок,2-компьютер: '))
if game_type==2:
    result_win_pc = 0
    result_win_pl = 0
    while True:
        win_pc = 0
        win_pl = 0
        while True:

            while True:
                pl = int(input("Введите число: "))
                if pl == 1:
                    print("игрок загадал камень")
                    break
                elif pl == 2:
                    print("игрок загадал ножницы")
                    break
                elif pl == 3:
                    print("игрок загадал бумага")
                    break
                else:
                    print("Не корректное значение введите число от 1 до 3")

            pc = random.randint(1,3)
            if pc==1:
                print("компьютер загадал камень")
            elif pc==2:
                print("компьютер загадал ножницы")
            else:
                print("компьютер загадал бумага")

            if pc < pl or pc == 3 and pl == 1:
                print("---Компьютер победил---")
                win_pc += 1
            elif pc == pl:
                print("---Ничья---")
            else:
                print("---Победа игрока---")
                win_pl += 1

            if win_pc == 3:
                print(f"со счетом {win_pc}:{win_pl}")
                result_win_pc += 1
                break
            elif win_pl == 3:
                print(f"со счетом {win_pl}:{win_pc}")
                result_win_pl += 1
                break

            print(f"текущий счет: PC {win_pc}:PL {win_pl}")
        print(f"Итоговый счет:PC {result_win_pc}:PL {result_win_pl}")
        a = input("Вы хотите сыграть еще(Y/N)?")
        if a != "Y":
            break
        # Очистка консоли
        clear()
else:
    result_win_pl1 = 0
    result_win_pl2 = 0
    while True:
        win_pl1 = 0
        win_pl2 = 0
        while True:
            while True:
                pl1 = int(input("первый игрок вводит число: "))
                if pl1 == 1:
                    print("первый игрок загадал камень")
                    break
                elif pl1 == 2:
                    print("первый игрок загадал ножницы")
                    break
                elif pl1 == 3:
                    print("первый игрок загадал бумага")
                    break
                else:
                    print("Не корректное значение введите число от 1 до 3")
            # Очистка консоли
            clear()

            while True:
                pl2 = int(input("второй игрок вводит число: "))
                if pl2 == 1:
                    print("второй игрок загадал камень")
                    break
                elif pl2 == 2:
                    print("второй игрок загадал ножницы")
                    break
                elif pl2 == 3:
                    print("второй игрок загадал бумага")
                    break
                else:
                    print("Не корректное значение введите число от 1 до 3")
            # Очистка консоли
            clear()

            if pl1 < pl2 or pl1 == 3 and pl2 == 1:
                print("---игрок 1 победил---")
                win_pl1 += 1
            elif pl1 == pl2:
                print("---Ничья---")
            else:
                print("---игрок 2 победил---")
                win_pl2 += 1

            if win_pl1 == 3:
                print(f"со счетом {win_pl1}:{win_pl2}")
                result_win_pl1 += 1
                break
            elif win_pl2 == 3:
                print(f"со счетом {win_pl2}:{win_pl1}")
                result_win_pl2 += 1
                break

            # Очистка консоли
            clear()

            print(f"текущий счет: Pl1 {win_pl1}:PL2 {win_pl2}")

        print(f"Итоговый счет:Pl1 {result_win_pl1}:PL2 {result_win_pl2}")
        a = input("Вы хотите сыграть еще(Y/N)?")
        if a != "Y":
            break
        # Очистка консоли
        clear()
