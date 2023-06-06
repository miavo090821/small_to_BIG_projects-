import random
import pygame
import sqlite3
import socket

# Initialize Pygame and Pygame Mixer
pygame.mixer.init()
pygame.init()

# Set window dimensions
window_width = 800
window_height = 600

# Define color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Hangman Game")

# Set the position and size of the hangman's head
head_radius = 50
head_x = 450
head_y = 250

# Define the hangman graphics
hangman_graphics = [
    [(100, 500), (700, 500)],  # Base
    [(100, 500), (100, 100)],  # Vertical pole
    [(100, 100), (400, 100)],  # Horizontal pole
    [(400, 100), (400, 150)],  # Rope
    [(450, 300, 50)],  # Head
    [(400, 250), (400, 400)],  # Body
    [(400, 275), (350, 325)],  # Left arm
    [(400, 275), (450, 325)],  # Right arm
    [(400, 400), (350, 450)],  # Left leg
    [(400, 400), (450, 450)]  # Right leg
]


class SoundManager:
    def __init__(self):
        # Initialize sound effects
        self.congrats_sound = pygame.mixer.Sound('congrats.wav')
        self.correct_sound = pygame.mixer.Sound('correct.wav')
        self.incorrect_sound = pygame.mixer.Sound('incorrect.wav')


class DatabaseManager:
    def __init__(self, db_file):
        self.db_file = db_file

    def load_words(self):
        # Connect to the database and retrieve words and suggestions
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT word, suggestion FROM words")
        rows = cursor.fetchall()
        words = [row[0] for row in rows]
        suggestions = [row[1] for row in rows]
        cursor.close()
        connection.close()
        return words, suggestions


class NetworkManager:
    
    def get_ip_address():
        try:
            # Create a temporary socket to retrieve the IP address
            temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            temp_socket.connect(("8.8.8.8", 80))
            ip_address = temp_socket.getsockname()[0]
            temp_socket.close()
            return ip_address
        except socket.error:
            return "Cannot retrieve IP address"


class User:
    def __init__(self, username, password, nickname):
        self.username = username
        self.password = password
        self.nickname = nickname
        self.score = 0
        self.ip_address = NetworkManager.get_ip_address()


class GameManager:
    def __init__(self):
        self.users = []
        self.high_scores = []
        self.sound_manager = SoundManager()
        self.db_manager = DatabaseManager('word_dict.db')

    def register(self):
        # Register a new user
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        nickname = input("Enter a nickname: ")
        user = User(username, password, nickname)
        self.users.append(user)

    def login(self):
        # Log in with existing user credentials
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for user in self.users:
            if user.username == username and user.password == password:
                print("Login successful!")
                return user
        print("Invalid username or password.")
        return None

    def display_high_scores(self):
        # Display the high scores
        print("High Scores:")
        for score in self.high_scores:
            print(f"{score.nickname}: {score.score}")

    def update_high_scores(self, user):
        # Update the high scores list
        self.high_scores.append(user)
        self.high_scores.sort(key=lambda x: x.score, reverse=True)

    def save_high_scores(self):
        # Save the high scores to a file
        with open('high_scores.txt', 'w') as file:
            for score in self.high_scores:
                file.write(f"{score.nickname},{score.score}\n")

    def load_high_scores(self):
        try:
            # Load the high scores from a file
            with open('high_scores.txt', 'r') as file:
                for line in file:
                    nickname, score = line.strip().split(',')
                    user = User("", "", nickname)
                    user.score = int(score)
                    self.high_scores.append(user)
        except FileNotFoundError:
            return

    def initialize_game(self):
        # Initialize the game by selecting a random word from the database
        words, suggestions = self.db_manager.load_words()
        word_index = random.randint(0, len(words) - 1)
        word = words[word_index]
        suggestion = suggestions[word_index]
        guessed_letters = set()
        max_guesses = 9
        return word, guessed_letters, max_guesses, suggestion

    def draw_hangman(self, stage, player_index):
        # Draw the hangman graphics based on the current stage of the game
        player_x = 50 + player_index * 200
        player_y = 50

        for i in range(stage + 1):
            graphic = hangman_graphics[i]
            if len(graphic) == 2:
                line_start = (player_x + graphic[0][0], player_y + graphic[0][1])
                line_end = (player_x + graphic[1][0], player_y + graphic[1][1])
                pygame.draw.line(window, WHITE, line_start, line_end, 10)
            else:
                circle_center = (head_x, head_y)
                pygame.draw.circle(window, WHITE, circle_center, head_radius)

    def run_hangman_game(self, player_name, player_index):
        # Run a game of hangman
        congrats_sound, correct_sound, incorrect_sound = (
            self.sound_manager.congrats_sound,
            self.sound_manager.correct_sound,
            self.sound_manager.incorrect_sound
        )
        word, guessed_letters, max_guesses, suggestion = self.initialize_game()
        score = 9
        incorrect_guesses = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            window.fill(BLACK)

            print("Suggestion:", suggestion)

            guess = input(f"{player_name}, guess a letter: ").lower()
            guessed_letters.add(guess)

            all_letters_guessed = True
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
                    all_letters_guessed = False
            print()

            if all_letters_guessed:
                print("\nCONGRATS, You guessed the word correctly!")
                pygame.mixer.Sound.play(congrats_sound)
                print("Score:", score)
                break

            if guess in guessed_letters and guess in word:
                print("\nCorrect letter!")
                pygame.mixer.Sound.play(correct_sound)
                continue
            else:
                print("\nIncorrect!")
                pygame.mixer.Sound.play(incorrect_sound)
                score -= 1
                incorrect_guesses += 1
                self.draw_hangman(incorrect_guesses, player_index)

            if len(guessed_letters) >= max_guesses:
                print("Oops, the word was", word, "Try a new word, okay?")
                break

            print("Score:", score)
            if score == 0:
                print("You lost")
                self.draw_hangman(9, player_index)
                break

            pygame.display.update()

        user = User("", "", player_name)
        user.score = score
        self.update_high_scores(user)
        self.save_high_scores()

    def start_game(self):
        self.load_high_scores()
        while True:
            choice = input(
                "Do you want to register (R), login (L), view high scores (H), or search for IP addresses (I)? "
            ).lower()

            if choice == "r":
                self.register()
            elif choice == "l":
                user = self.login()
                if user is None:
                    continue
                else:
                    break
            elif choice == "h":
                self.display_high_scores()
                continue
            elif choice == "i":
                print("IP addresses of other players:")
                for i, user in enumerate(self.users):
                    if user.ip_address != NetworkManager.get_ip_address():
                        print(f"Player {i + 1} ({user.nickname}): {user.ip_address}")
                continue
            else:
                print("Invalid choice. Please try again.")

        for i, user in enumerate(self.users):
            print(f"\nPlayer {i + 1} ({user.nickname})")
            self.run_hangman_game(user.nickname, i)

        while True:
            choice = input("Do you want to play again (P), search for IP addresses (I), or quit (Q)? ").lower()
            if choice == "q":
                break
            elif choice == "i":
                print("IP addresses of other players:")
                for i, user in enumerate(self.users):
                    if user.ip_address != NetworkManager.get_ip_address():
                        print(f"Player {i + 1} ({user.nickname}): {user.ip_address}")
                continue

        pygame.quit()

game_manager = GameManager()
game_manager.start_game()
