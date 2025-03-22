import numpy as np
import matplotlib.pyplot as plt

# Opis: Program symuluje grę w "Kamień, Papier, Nożyce" pomiędzy graczem a komputerem,
#       aktualizując macierz przejść na podstawie wyników i uczenia się w czasie rzeczywistym.

# Inicjalizacja stanu gotówki gracza
cash: int = 0
cash_history: list[int] = []

states_computer = ["Paper", "Rock", "Scissors"]
transition_matrix_computer = {
    "Paper": {"Paper": 2/3, "Rock": 1/3, "Scissors": 0/3},
    "Rock": {"Paper": 0/3, "Rock": 2/3, "Scissors": 1/3},
    "Scissors": {"Paper": 2/3, "Rock": 0/3, "Scissors": 1/3}
}

# obliczanie wektoru stacjonarnego
matrix_size = len(states_computer)
matrix = np.zeros((matrix_size, matrix_size))
for i in range(matrix_size):
    for j in range(matrix_size):
        matrix[i, j] = transition_matrix_computer[states_computer[i]][states_computer[j]]
eigenvalues, eigenvectors = np.linalg.eig(matrix.T)
stationary_index = np.argmin(np.abs(eigenvalues - 1.0))
stationary_vector = np.real(eigenvectors[:, stationary_index])
stationary_vector /= stationary_vector.sum()

def choose_move_computer(computer_previous_move: str) -> str:
    next_move: str = np.random.choice(states_computer, p=[transition_matrix_computer[computer_previous_move][x] for x in states_computer])
    return next_move

def choose_move_player() -> str:
    next_move: str = np.random.choice(states_computer, p=stationary_vector)
    return next_move

##### GRACZ #####
# Definicja ruchów gracza:
#   wersja 1: na podstawie wektora stacjonarnego transition_matrix_computer,
#   wersja 2: w trakcie gry(iteracji) nauczenie gracza taktyki w postaci jego macierzy przejść
#             (inicjujemy macierz przejść gracza wypełnioną np. 1/3, a w trakcie gry po każdej rundzie aktualizujemy ją). 
# Należy napisać kod dla obu wersji (w osobnych plikach, albo w jednym pliku z możliwością zmiany taktyki jakimś parametrem)

# Obliczanie wektora stacjonarnego macierzy przejść transition_matrix_computer (wersja 1 taktyki gracza)
'''do uzupelnienia'''

# Funkcja aktualizująca macierz przejść gracza (wersja 2 taktyki gracza)
'''do uzupelnienia'''
# Funkcja wybierająca ruch gracza na podstawie macierzy przejść tj. na podstawie swojego poprzedniego wyboru (wersja 2 taktyki gracza)
'''do uzupelnienia'''
if __name__ == '__main__':
    # Główna pętla gry
    computer_previous_move = np.random.choice(states_computer)
    for _ in range(10_000):
        computer_current_move = choose_move_computer(computer_previous_move)
        player_current_move = choose_move_player()
        if computer_current_move == "Paper":
            if player_current_move == "Scissors":
                cash += 1
            elif player_current_move == "Rock":
                cash -= 1
        elif computer_current_move == "Scissors":
            if player_current_move == "Rock":
                cash += 1
            elif player_current_move == "Paper":
                cash -= 1
        elif computer_current_move == "Rock":
            if player_current_move == "Paper":
                cash += 1
            elif player_current_move == "Scissors":
                cash -= 1
        cash_history.append(cash)
        computer_previous_move = computer_current_move




    # Wykres zmiany stanu gotówki w każdej kolejnej grze
    plt.plot(range(10_000), cash_history)
    plt.xlabel('Numer Gry')
    plt.ylabel('Stan Gotówki')
    plt.title('Zmiana Stanu Gotówki w Grze "Kamień, Papier, Nożyce V1"')
    plt.show()