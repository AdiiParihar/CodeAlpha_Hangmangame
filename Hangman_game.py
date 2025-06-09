import random
def play_game():
    print("🎮 Welcome to Naruto Character Guessing Game!\n")
    while True:
        L = ['naruto', 'sasuke', 'sakura', 'kakashi', 'itachi', 'minato']
        word = random.choice(L).lower()
        to_guess = ["_"] * len(word)
        chances = 6
        guessed_letters = []
        while True:
            print("\nWord to guess:", " ".join(to_guess))
            print("Guessed letters:", ", ".join(guessed_letters))
            s = input("Enter your guess: ").lower()
            if not s.isalpha() or len(s) != 1:
                print("❗ Please enter a single alphabetic character.")
                continue
            if s in guessed_letters:
                print("You already guessed that letter!")
                continue
            guessed_letters.append(s)
            if s in word:
                for i in range(len(word)):
                    if word[i] == s:
                        to_guess[i] = s
                if "".join(to_guess) == word:
                    print("\n✅ You won! The word was:", word)
                    break
                print("Correct guess!")
            else:
                print("Wrong guess!")
                chances -= 1
                if chances == 0:
                    print("\nYou lost! The word was:", word)
                    break
                print(f"You have {chances} guesses left.")
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! See you next time")
            break
if __name__ == "__main__":
    play_game()