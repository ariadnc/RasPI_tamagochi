class Tamagotchi:

    def __init__(self):
        self.xp = 0
        self.health = 3

    def correct_answer(self):
        self.xp += 10
        print("🐣 Tamagotchi: YAY!")
        print(f"⭐ XP: {self.xp}")

    def wrong_answer(self):
        self.health -= 1
        print("🐣 Tamagotchi: Oh no...")
        print(f"❤️ Health: {self.health}")

    def is_alive(self):
        return self.health > 0
