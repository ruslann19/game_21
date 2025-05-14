import json
from random import getrandbits

from Card import Card, CardValue

from .consts import PlayerState
from .OpenRouterChat import OpenRouterChat

MAX_SCORE = 21


class Player:
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type
        self.cards = []
        self.state = PlayerState.ACTIVE

        self._score = 0
        self._aces = 0
        self._aces_as_1 = 0

        with open("OPENROUTER_API_KEY.txt", "r") as f:
            API_KEY = f.readline()

        system_prompt = """
            Мы играем в 21. Я буду говорить тебе какие у тебя карты, а ты будешь решать, брать ли ещё карты.

            2–10 — номинал карты (например, 7 = 7 очков).
            Валет (В), Дама (Д), Король (К) — по 10 очков .
            Туз (Т) — 1 или 11 очков , как удобнее тебе.

            Отвечай в формате JSON, следующим образом:
            {
                "message": "<Твои рассуждения на счёт того, нужно ли ещё брать карту>",
                "take": "<true/false (с маленькой буквы) - брать или не брать карту>"
            }

            Такой формат нужен, чтобы распарсить его через json.loads.
        """

        self.chat = OpenRouterChat(
            api_key=API_KEY,
            model="meta-llama/llama-3-8b-instruct",
            system_prompt=system_prompt,
        )

    def __str__(self) -> str:
        cards = ""
        for card in self.cards:
            cards += str(card)

        result = f"name: {self.name}\n" + f"cards: {cards}\n" + f"score: {self.score()}"
        return result

    def score(self) -> int:
        return self._score

    def is_active(self) -> bool:
        return self.state == PlayerState.ACTIVE

    def decide(self) -> bool:
        match self.type:
            case "random":
                decision = self._decide_random()
            case "LLM":
                decision = self._decide_llm()
            case "player":
                decision = self._decide_player()

        print("decision:", decision)
        print()

        if not decision:
            self.state = PlayerState.STOPPED

        return decision

    def _decide_random(self):
        print(f"{self.name}: Я рандомный чел")
        decision = bool(getrandbits(1))
        return decision

    def _decide_llm(self):
        cards = ""
        for card in self.cards:
            cards += str(card)

        response = self.chat.ask(f"У тебя есть: {cards}")
        response_json = json.loads(response)

        message = response_json["message"]
        print(f"{self.name}: {message}")

        decision = response_json["take"] == "true"

        return decision

    def _decide_player(self):
        cards = ""
        for card in self.cards:
            cards += str(card)

        print(f"У Вас есть: {cards}")

        correct_input = False
        while not correct_input:
            print("Брать ещё карту?")
            print("1 - да")
            print("0 - нет")
            player_input = input("Ваше решение: ")

            match player_input:
                case "1":
                    decision = True
                    correct_input = True

                case "0":
                    decision = False
                    correct_input = True

                case _:
                    print("Некорректный ввод")

        return decision

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

        if card.value == CardValue.ACE:
            self._aces += 1

        self._score += card.score()

        if self._score > MAX_SCORE:
            if self._aces > self._aces_as_1:
                self._score -= 10
                self._aces_as_1 += 1
            else:
                self.state = PlayerState.FAILED
