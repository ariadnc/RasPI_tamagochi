from vocab import load_vocabulary, get_random_word
from quiz import ask_meaning


def start_game(tamagotchi):

    vocabulary = load_vocabulary()

    print("\n🐣 Welcome to your Chinese Tamagotchi!")
    print("Let's learn some Chinese!\n")

    while tamagotchi.is_alive():

        word = get_random_word(vocabulary)

        print("\n-------------------------")
        print(f"HSK {word['HSKLevel']}")
        print("-------------------------")

        question_type = input(
            "\nChoose a question:\n"
            "1 - Meaning\n"
            "q - Quit\n\n"
            "Your choice: "
        )

        if question_type == "q":
            break

        elif question_type == "1":
            correct = ask_meaning(word)

        else:
            print("Please choose 1 or q.")
            continue

        if correct:
            tamagotchi.correct_answer()
        else:
            tamagotchi.wrong_answer()

    print("\n🐣 Game over!")
    print(f"⭐ Final XP: {tamagotchi.xp}")
