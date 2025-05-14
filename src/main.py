from Game21 import Game21
from Player import Player

players = [
    Player("Ваня", "random"),
    Player("Петя", "LLM"),
    Player("Игорь", "LLM"),
    Player("Вася", "LLM"),
    Player("Лёша", "player"),
]

game21 = Game21(players)

game21.run()
