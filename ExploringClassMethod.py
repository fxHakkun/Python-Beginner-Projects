#Play with Class

# Python program to
# demonstrate init with
# inheritance

class Player:
    def __init__(self, name, base_skill, passive, second_skill, ultimate, hp):
        self.name = name
        self.base_skill = base_skill
        self.passive = passive
        self.second_skill = second_skill
        self.ultimate = ultimate
        self.hp = hp

    def is_using(self):
        if bool(self.base_skill) == True:
            print(f"{self.name} is using {self.base_skill}")
        if bool(self.second_skill) == True:
            print(f"{self.name} is using {self.second_skill}")
        if bool(self.ultimate) == True:
            print(f"{self.name} is using {self.ultimate}")
        if bool(self.passive) == True:
            print(f"{self.name}'s {self.passive} is activated !")

    def take_dmg(self):
        for item in range(bool()):
            if bool(self.base_skill or self.second_skill) == True:
                print(f"HP : {self.hp - 100}")


Roger = Player("Roger", "Claw", None, "Sprint", "Wolf Form", 1000)
Roger.is_using()
Roger.take_dmg()