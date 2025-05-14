from enum import Enum

CardSuit = Enum(
    "CardSuit",
    [
        ("CROSSES", "CROSSES"),
        ("SPADES", "SPADES"),
        ("HEARTS", "HEARTS"),
        ("DIAMONDS", "DIAMONDS"),
    ],
)

CardValue = Enum(
    "CardValue",
    [
        ("TWO", "2"),
        ("THREE", "3"),
        ("FOUR", "4"),
        ("FIVE", "5"),
        ("SIX", "6"),
        ("SEVEN", "7"),
        ("EIGHT", "8"),
        ("NINE", "9"),
        ("TEN", "10"),
        ("JACK", "JACK"),
        ("QUEEN", "QUEEN"),
        ("KING", "KING"),
        ("ACE", "ACE"),
    ],
)

SCORE = {
    CardValue.TWO: 2,
    CardValue.THREE: 3,
    CardValue.FOUR: 4,
    CardValue.FIVE: 5,
    CardValue.SIX: 6,
    CardValue.SEVEN: 7,
    CardValue.EIGHT: 8,
    CardValue.NINE: 9,
    CardValue.TEN: 10,
    CardValue.JACK: 10,
    CardValue.QUEEN: 10,
    CardValue.KING: 10,
    CardValue.ACE: 11,
}
