import random


class Card:
    HEARTS = 'Hearts'  # Масть "Черви"
    DIAMONDS = 'Diamonds'  # Масть "Бубны"
    CLUBS = 'Clubs'  # Масть "Пики"
    SPADES = 'Spades'  # Масть "Трефы"

    def __init__(self, value, suit):
        self.value = value  # Значение карты (2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_icons = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}

    def __str__(self):  # Отображение информации об объекте класса
        return f'{self.value}{self.suit_icons[self.suit]}'

    def equal_suit(self, other_card):  # Проверяет, одинаковые ли масти у карт
        return self.suit == other_card.suit

    def __gt__(self, other_card):  # Magic-метод проверяют, какая карта имеет большее значение
        if Deck.suits.index(self.value) == Deck.suits.index(other_card.suit):
            return Deck.suits.index(self.suit) > Deck.suits.index(other_card.suit)
        else:
            return Deck.values.index(self.suit) > Deck.values.index(other_card.suit)

    def __eq__(self, other_card):  # Magic-метод делает проверку на равенство
        return self.value == other_card.value and self.suit == other_card.suit

    def __lt__(self, other_card):  # Magic-метод проверяют, какая карта имеет меньшее значение
        return not self > other_card and not self == other_card


class Deck:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                self.cards.append(Card(value, suit))

    def __str__(self):
        return f"cards[{len(self.cards)}]{', '.join([str(card) for card in self.cards])}"

    def __getitem__(self, index):
        return self.cards[index]

    def draw(self, x):
        draw_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return draw_cards

    def shuffle(self):
        random.shuffle(self.cards)
