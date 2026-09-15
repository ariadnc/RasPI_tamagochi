def ask_meaning(word):
    print("\nWhat does this mean?")
    print(f"\n🇨🇳  {word['character']}\n")

    answer = input("Your answer: ")

    if answer.lower().strip() == word["meaning"].lower():
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Not quite! The answer is: {word['meaning']}")
        return False
