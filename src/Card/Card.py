from .consts import SCORE


class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        result = f"({self.value.value} {self.suit.value})"
        return result

    def score(self) -> int:
        return SCORE[self.value]
