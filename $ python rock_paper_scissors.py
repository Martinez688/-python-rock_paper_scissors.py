import random

def play_game():
    print("Игра 'Камень, ножницы, бумага' против компьютера")
    print("Введите ваш выбор: 1 - Камень, 2 - Ножницы, 3 - Бумага")
    choices = ["Камень", "Ножницы", "Бумага"]
    player_choice = int(input("Ваш выбор: ")) - 1

    if player_choice < 0 or player_choice > 2:
        print("Неправильный выбор! Попробуйте ещё раз.")
        return

    computer_choice = random.randint(0, 2)

    print("Ваш выбор:", choices[player_choice])
    print("Выбор компьютера:", choices[computer_choice])

    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
        print("Вы победили!")
    else:
        print("Компьютер победил!")

def main():
    play_game()

if __name__ == '__main__':
    main()
