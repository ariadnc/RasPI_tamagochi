def ask_meaning(word):
    print("\nWhat does this mean?")
    print(f"\n🇨🇳  {word['Chinese']}\n")

    answer = input("Your answer: ")

    if answer.lower().strip() in word["English"].lower():
        print(f"✅ Correct! The answer is: {word['English']}")
        return True
    else:
        print(f"❌ Not quite! The answer is: {word['English']}")
        return False

