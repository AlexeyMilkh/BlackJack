from Classes import Deck, Card
from Tools import sum_points

condition = True
player_money = 100  # Деньги игрока

while condition:
    print('Деньги игрока:', player_money)
    rate_value = int(input('Введите ставку: '))  # Размер ставки

    while True:
        if (player_money - rate_value) < 0:  # Если денег на новую ставку недостаточно, то игра заканчивается
            print("У вас закончились деньги. Игра окончена!")
            break
        print(f"Игрок делает ставку: {rate_value}")
        # 1. В начале игры создаем колоду и перемешиваем ее
        deck = Deck()
        deck.shuffle()
        # 2. Игроку выдаем две карты
        player_cards = deck.draw(2)
        # 3. Дилер берет одну карту
        dealer_cards = deck.draw(1)
        # 4. Отображаем в консоли карты игрока и дилера
        print('Карты игрока:', end='\t')
        for i in player_cards:
            print(i, end='\t')
        print('\n')
        print('Карты дилера:', end='\t')
        for i in dealer_cards:
            print(i)
        # 5. Проверяем нет ли у игрока БлэкДжека (21 очко)
        if sum_points(player_cards) == 21:
            # Выплачиваем выигрыш 3 и 2
            player_money += rate_value * 1.5
            print(f"Black Jack!!! Вы победили, ваш выигрыш {rate_value * 1.5}")
            # Заканчиваем игру
            break
        # Если нет БлэкДжека, то
        while True:  # Игрок добирает карты пока не скажет "достаточно" или не сделает перебор (>21)
            player_choice = input("еще(1)/достаточно(0): ")
            if player_choice == "1":
                # Раздаем еще одну карту
                player_cards += deck.draw(1)
                print('Карты игрока:', end='\t')
                for i in player_cards:
                    print(i, end='\t')
                print(end='\n')
            elif player_choice == "0":  # Заканчиваем добирать карты
                break
            else:  # Обработка некорректного ввода
                print('Вы ввели неверную цифру')

        if sum_points(player_cards) > 21:  # Если перебор (>21), заканчиваем добор
            print(f"Перебор: {sum_points(player_cards)} очков. Вы проиграли!")
            player_money -= rate_value
            break
        elif sum_points(player_cards) < 21:  # Если у игрока не 21 (БлэкДжек) и нет перебора, то
            print("Дилер добирает карты")
            while True:  # дилер начинает набирать карты.
                if sum_points(dealer_cards) < 17:  # Смотри подробные правила добора дилера в задании
                    dealer_cards += deck.draw(1)
                print('Карты дилера:', end='\t')
                for i in dealer_cards:
                    print(i, end='\t')
                else:
                    break
            print(end='\n')

        if sum_points(player_cards) > sum_points(dealer_cards):  # Выясняем кто набрал больше очков.
            # Выплачиваем/забираем ставку
            player_money += rate_value * 2
            print(f"Вы победили! Ваш выигрыш {rate_value * 2}")
            break
        else:
            print("Вы проиграли!")
            player_money -= rate_value
            break

    print('Партия окончена')
    player_choice = input("сыграть еще партию(1)/покинуть стол(нажмите любую кнопку): ")
    if player_choice == "1":
        condition = True
    else:
        condition = False

