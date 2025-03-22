import numpy as np
import matplotlib.pyplot as plt

# Opis: Program symuluje grę w "Kamień, Papier, Nożyce" pomiędzy graczem a komputerem,
#       aktualizując macierz przejść na podstawie wyników i uczenia się w czasie rzeczywistym.

# Inicjalizacja stanu gotówki gracza
cash: int = 0
cash_history: list[int] = []

lear_rate: int = 5

states = ["Paper", "Rock", "Scissors"]
transition_matrix_computer = {
    "Paper": {"Paper": 2 / 3, "Rock": 1 / 3, "Scissors": 0 / 3},
    "Rock": {"Paper": 0 / 3, "Rock": 2 / 3, "Scissors": 1 / 3},
    "Scissors": {"Paper": 2 / 3, "Rock": 0 / 3, "Scissors": 1 / 3}
}

# default values for player matrix
transition_matrix_player = {
    "Paper": {"Paper": 1 / 3, "Rock": 1 / 3, "Scissors": 1 / 3},
    "Rock": {"Paper": 1 / 3, "Rock": 1 / 3, "Scissors": 1 / 3},
    "Scissors": {"Paper": 1 / 3, "Rock": 1 / 3, "Scissors": 1 / 3},
}


def computer_move(previous_move: str) -> str:
    next_move: str = np.random.choice(states,
                                      p=[transition_matrix_computer[previous_move][x] for x in states])
    return next_move

def player_move(previous_move: str) -> str:
    next_move: str = np.random.choice(states,
                                      p=[transition_matrix_player[previous_move][x] for x in states])
    return next_move

def adjust_player_transition_matrix(previous_move: str, current_move: str, learn_rate: int) -> None:
    transition_matrix_player[previous_move][current_move] += learn_rate
    suma = sum(transition_matrix_player[previous_move][x] for x in states)
    # normalization
    for s in states:
        transition_matrix_player[previous_move][s] /= suma

if __name__ == '__main__':
    previous_computer_move = np.random.choice(states)
    previous_player_move = np.random.choice(states)

    for _ in range(10_000):
        computer_current_move = computer_move(previous_computer_move)
        player_current_move = player_move(previous_player_move)

        if computer_current_move == "Paper":
            if player_current_move == "Scissors":
                cash += 1
                adjust_player_transition_matrix(previous_player_move, player_current_move, lear_rate)
            elif player_current_move == "Rock":
                cash -= 1
        elif computer_current_move == "Scissors":
            if player_current_move == "Rock":
                cash += 1
                adjust_player_transition_matrix(previous_player_move, player_current_move, lear_rate)
            elif player_current_move == "Paper":
                cash -= 1
        elif computer_current_move == "Rock":
            if player_current_move == "Paper":
                cash += 1
                adjust_player_transition_matrix(previous_player_move, player_current_move, lear_rate)
            elif player_current_move == "Scissors":
                cash -= 1
        cash_history.append(cash)

        # swap previous and current states
        previous_computer_move = computer_current_move
        previous_player_move = player_current_move

    # Wykres zmiany stanu gotówki w każdej kolejnej grze
    plt.plot(range(10_000), cash_history)
    plt.xlabel('Numer Gry')
    plt.ylabel('Stan Gotówki')
    plt.title('Zmiana Stanu Gotówki w Grze "Kamień, Papier, Nożyce V2"')
    plt.show()
