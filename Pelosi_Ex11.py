import random

class Card:
    """Represents a standard playing card."""

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank):
        self.suit = suit      
        self.rank = rank      

    def __str__(self):
        return f"{Card.ranks[self.rank]} of {Card.suits[self.suit]}"


class Deck:
    """Deck of 52 cards."""

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

def deal_poker_hand(deck):
    """Deals a 5-card Poker hand."""
    return [deck.deal() for _ in range(5)]


def replace_cards(hand, deck, indices):
    """Replaces selected cards in the player's hand."""
    for i in indices:
        hand[i - 1] = deck.deal()   
    return hand


def print_hand(hand, title):
    """Displays a hand of cards."""
    print(f"\n{title}:")
    for i, card in enumerate(hand, 1):
        print(f"{i}: {card}")


def main():
    deck = Deck()
    deck.shuffle()

    hand = deal_poker_hand(deck)
    print_hand(hand, "Initial Hand")

    answer = input(
        "\nEnter card numbers to replace (example: 1 3 5), or press Enter to keep all cards: "
    ).strip()

    if answer:
        try:
            selections = list(map(int, answer.split()))
            selections = [n for n in selections if 1 <= n <= 5]
            hand = replace_cards(hand, deck, selections)
        except ValueError:
            print("Invalid input. No cards replaced.")

    print_hand(hand, "Final Hand After Draw")
    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
