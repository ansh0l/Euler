from collections import counter

suites = {
    'C' : "Club",
    'D' : "Diamond",
    'H' : "Heart",
    'S' : "Spade",
    }

values = {
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 11, 
    'Q' : 12,
    'K' : 13,
    'A' : 14,
    }

class InvalidCard(Exception):
    pass

class Card(object):

    def __init__(self, card='AC'):
        if type(card) != str or not (1 < len(card) < 4):
            raise InvalidCard
        if len(card) == 2:
            self.value = values[card[0]]
            self.suite = suites[card[1]]
        else #len(card) == 3 #Example 10C, 10S
            self.value = values[card[:2]]
            self.suite = suites[card[2]]

    def __unicode__(self):
        return "suite: %s value:%s" % (self.suite, self.value)


class InvalidHand(Exception):
    pass

class Hand(object):

    def __init__(self, cards = []):
        if type(cards) != list or len(cards) != 5 or \
                not all(type(c) == Card for c in cards):
            raise InvalidHand
        self.cards = cards

    def values(self):
        return sorted([c.value for c in self.cards])

    def suites(self):
        return [c.suite for c in self.cards]

    def get_rank(self):
        values = self.values()
        counter_values = Counter(self.values())
        counter_suites = Counter(self.suites())

        if len(counter_suites.keys()) == 1 and set(values) == set(range(10, 15)):
            self.rank = 1
            self.combination = "Royal Flush"
        elif len(counter_suites.keys()) and \
                set(values) == set(range(values[0], values[0] + 5)):
            self.rank = 2
            self.combination = "Straight Flush"
        elif len(counter_values.keys()) == 2:
            if counter_values.values()[0] in [1, 4]:
                self.rank = 3
                self.combination = "Four Of A Kind"
            else:
                self.rank = 4
                self.combination = "Full House"
        elif len(counter_suites.keys()) == 1 :
            self.rank = 5
            self.combination = "Flush"
        elif set(values) == set(range(values[0], values[0] + 5)):
            self.rank = 6
            self.combination = "Straight"
        elif len(counter_values.keys()) == 3:
            if 3 in counter_values.values():
                self.rank = 7
                self.combination = "Three Of A Kind"
            else:
                self.rank = 8
                self.combination = "Double Pair"
        elif len(counter_values.keys()) == 4:
            self.rank = 9
            self.combination = "Pair"
        else:
            self.rank = 10
            self.combination = "High Card"


class InvalidGame(Exception):
    pass

class Game(object):

    def __init__(self, hands = []):
        if type(hands) != list or len(hands) != 2 or \
                not all(type(h) == Hand for h in hands):
            raise InvalidGame
        self.hands = hands

    def compare_hands(hands = self.hands)
        if hand[0].rank != hand[1].rank:
            return 0 if hand[0].rank > hand[1].rank else 1

def construct_game(string):


def main():
    with open("poker.txt", "r") as f:
        game = construct_game(f.readline())

if __name__ == "__main__":
    main()
