from typing import List

from Dealer import Dealer
from Player import Player

INITIAL_CARDS_COUNT = 2
MAX_SCORE = 21


class Game21:
    def __init__(self, players: List[Player]) -> None:
        self.players = players
        self.players_count = len(self.players)
        self.active_players_count = self.players_count
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]

        self.dealer = Dealer()

        for player in self.players:
            for _ in range(INITIAL_CARDS_COUNT):
                card = self.dealer.get_card()
                player.add_card(card)

    def handle_next_player(self) -> None:
        if not self.current_player.is_active():
            self.active_players_count -= 1
            return

        take_card = self.current_player.decide()

        if take_card:
            card = self.dealer.get_card()
            self.current_player.add_card(card)

    def set_next_active_player(self) -> None:
        if self.active_players_count == 0:
            self.current_player = None
            return

        index = (self.current_player_index + 1) % self.players_count
        player = self.players[index]
        while not player.is_active():
            if index == self.current_player_index:
                break

            index = (index + 1) % self.players_count
            player = self.players[index]

        self.current_player_index = index
        self.current_player = player

    def run(self) -> None:
        while self._check_active_players():
            self.handle_next_player()
            self.set_next_active_player()

        self._show_results()

    def _check_active_players(self) -> bool:
        return self.active_players_count > 0

    def _show_results(self) -> None:
        print("------ RESULTS ------")
        best_score = 0
        for player in self.players:
            score = player.score()
            if score <= MAX_SCORE and score > best_score:
                best_score = score
            print(player)
            print()

        print("------ BEST RESULT ------")
        for player in self.players:
            if player.score() == best_score:
                print(player)
                print()
