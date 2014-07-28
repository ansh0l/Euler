class InvalidCard(Exception):
    pass

class InvalidHand(Exception):
    pass

class Card(object):

    def __init__(self, card='AC'):
        if type(card) != str or len(card) != 2:
            raise InvalidCard
        self.value = card[0]
        self.suite = card[1]

    def __unicode__(self):
        return "suite: %s value:%s" % (self.suite, self.value)

class Hand(object):

    def __init__(self, cards = []):
        if type(cards) != list or len(cards) != 5 or \
                not all(type(c) == Card for c in cards):
            raise InvalidHand
        self.cards = cards

def main():
    pass

if __name__ == "__main__":
    main()

