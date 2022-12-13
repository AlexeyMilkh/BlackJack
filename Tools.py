def sum_points(cards):
    card_points = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }
    hand = 0

    for card in cards:
        hand += card_points[card.value]

    if hand > 21:
        for card in cards:
            if card.value == 'A':
                hand -= 10

    return hand
