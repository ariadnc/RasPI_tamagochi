def ask_meaning(word):
    print("\nWhat does this mean?")
    print(f"\n🇨🇳  {word['Chinese']}\n")

    answer = input("Your answer: ")

    if answer.lower().strip() == word["English"].lower():
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Not quite! The answer is: {word['English']}")
        return False
