# Madlib made by HAKkun

def Madlib_Process(): #choosing madlibs
    Madlibs_Function = ["Genshin Impact","Harry Potter","Jobless Reincarnation","Manchester United"]
    if Categories == "1" :
        Madlibs_Function = Madlibs_Function[0]
    elif Categories == "2":
        Madlibs_Function = Madlibs_Function[1]
    elif Categories == "3":
        Madlibs_Function = Madlibs_Function[2]
    elif Categories == "4":
        Madlibs_Function = Madlibs_Function[3]
    print(f"Madlibs {Madlibs_Function}")
    Current_Categories = Madlib_Question()
    Madlib_Input()
    if Categories == "1" :
        print(Current_Categories.Genshin_Impact())
    elif Categories == "2":
        print(Current_Categories.Harry_Potter())
    elif Categories == "3":
        print(Current_Categories.Jobless_Reincarnation())
    elif Categories == "4":
        print(Current_Categories.Manchester_United())

print("Choose the number")
print("1. Game \n2. Movies \n3. Anime \n4. Sports")
Categories = input("Number: ")
if Categories == "1" :
    Madlib_Process()
elif Categories == "2":
    Madlib_Process()
elif Categories == "3":
    Madlib_Process()
elif Categories == "4":
    Madlib_Process()
else:
    print("please input the correct number")

class Madlib_Question:
    Name = ""
    Name2 = ""
    Name3 = ""
    Spell = ""
    Spell2 = ""
    SignatureMove = ""
    SignatureMove2 = ""
    Adjective = ""
    Adjective2 = ""
    Noun = ""
    Noun2 = ""
    Location = ""
    Location2 = ""

    if Categories == "1":
        def Genshin_Impact(self):
            madlib = f" {self.Name} set off on an adventure in the land of {self.Location}, known for its {self.Adjective} landscapes and hidden treasures. Accompanied by their trusty companion, {self.Name2}, they sought to uncover the secrets of a mysterious {self.Noun}. The duo soon discovered that this artifact held the key to unlocking the ancient {self.Spell}, a power that could change the fate of Teyvat.\n  Their journey led them through {self.Location2}, where they encountered allies and enemies alike. Along the way, they met a guardian wielding a legendary {self.Noun2}, who taught them the secrets of the {self.Spell2}. Together, they faced numerous challenges, including a {self.Adjective2} monster that threatened the peace of the land.\n  In a climactic battle, {self.Name} used their newfound abilities to confront the {self.Adjective2} foe, who had been causing chaos across {self.Location}. With the power of the {self.Noun} and the strength of their allies, they unleashed the {self.Spell}, defeating the enemy and restoring harmony. The adventures of {self.Name} and {self.Name2} became legends, inspiring future heroes in the land of Teyvat."
            
            return madlib
    
    def Jobless_Reincarnation(self):
        madlib = f" {self.Name} found themselves in a {self.Adjective} world after reincarnating, where magic and {self.Noun} were part of everyday life. Determined to make the most of their second chance, they set off on a journey through {self.Location}. Early in their travels, they encountered {self.Name2}, a wise and skilled mentor who saw great potential in {self.Name}. Under their guidance, {self.Name} learned the secrets of powerful {self.Spell}, a skill that promised to change their destiny.\n As they honed their abilities, {self.Name} and {self.Name2} ventured into {self.Location2}, a land known for its {self.Adjective2} terrains and formidable creatures. Here, they discovered a legendary {self.Noun2}, an artifact said to grant immense power to its bearer. However, their path was fraught with danger, as they soon faced off against a {self.Adjective} monster that had been terrorizing the region. In a fierce battle, {self.Name} used their {self.Spell} to subdue the beast, showcasing the true extent of their newfound strength.\n    The journey wasn't without its trials. As they continued their quest, {self.Name} encountered a {self.Adjective2} foe who wielded the dark arts of {self.Spell2}, challenging everything they had learned. The epic duel between {self.Name} and this formidable adversary tested their resolve and skill to the utmost. With the help of {self.Name2} and the power of the {self.Noun2}, they were able to overcome this dire threat. By the end of their journey, {self.Name} had not only grown in power but also in wisdom, forging unbreakable bonds and leaving a lasting legacy in the world they now called home."
        
        return madlib
    
    def Harry_Potter(self):
        madlib = f"{self.Name} entered the magical world of Hogwarts, where the {self.Adjective} castle stood tall amidst the enchanting landscape. Eager to explore, they quickly befriended {self.Name2}, who introduced them to the wonders of {self.Noun}. Together, they delved into the secrets of the school, discovering hidden corridors and ancient spells. Their curiosity led them to the discovery of the {self.Spell}, a powerful enchantment said to be lost for centuries.\n As their friendship deepened, {self.Name} and {self.Name2} found themselves drawn into the mysteries of {self.Location}, a forbidden part of the school grounds. Here, they encountered a legendary {self.Noun2}, an object of immense power that could alter the course of their destiny. Their journey through {self.Location2}, filled with {self.Adjective2} creatures and perilous challenges, tested their courage and wit. During their adventure, they faced a {self.Adjective} creature that guarded the {self.Noun2}. Using their newly learned {self.Spell}, {self.Name} managed to overcome the beast and secure the artifact.\n  The climax of their tale came when {self.Name} faced off against a {self.Adjective2} foe, a dark wizard who had mastered the {self.Spell2}. The duel between them was fierce, showcasing the true power and determination of both sides. With the support of {self.Name2} and the wisdom gained from their journey, {self.Name} unleashed the full potential of the {self.Spell}, ultimately defeating their adversary. The triumph solidified their place in the annals of Hogwarts' history, leaving behind a legacy of bravery and friendship that would inspire future generations of witches and wizards."
        
        return madlib
    
    def Manchester_United(self):
        madlib = f"{self.Name} arrived at Old Trafford, eager to make their mark in the legendary {self.Adjective} stadium. Under the watchful eye of {self.Name3}, they quickly became friends with {self.Name2}, a seasoned player who taught them the intricacies of {self.Noun}. Together, they explored the rich history of Manchester United, discovering the secrets behind the club’s success, including the famed {self.SignatureMove}, a skill perfected by legends.\n    Their journey took them to {self.Location}, where they trained rigorously to master their techniques and improve their teamwork. Amidst the {self.Adjective2} fields, they encountered a legendary {self.Noun2}, an object that symbolized the club's storied past and future ambitions. Their training sessions were intense, filled with {self.Adjective2} drills and tactical challenges, preparing them for the trials ahead.\n    The ultimate test came during a crucial match against a formidable rival, a team known for their {self.SignatureMove2}. In the heat of the game, {self.Name} showcased their {self.SignatureMove}, dazzling the crowd with their skill and determination. The match reached its climax when {self.Name} faced off against a {self.Adjective2} defender, renowned for their defensive prowess. With a burst of inspiration and the support of {self.Name2}, {self.Name} executed a perfect {self.SignatureMove}, scoring the winning goal and securing victory for Manchester United. The triumph solidified their place in the club's history, celebrated by fans and teammates alike, leaving a legacy of excellence and teamwork at Old Trafford."
        
        return madlib
    
def Madlib_Input():

    Madlib_Question.Name = input("Give a name: ")
    Madlib_Question.Name2 = input("Give a second name: ")
    if Categories == "4":
        Madlib_Question.Name3 = input("Give a third name: ")
        Madlib_Question.SignatureMove = input("Give a signature move: ")
        Madlib_Question.SignatureMove2 = input("Give another signature move: ")
    elif Categories == "1" or "2" or "3":
        Madlib_Question.Spell = input("Give your spell chant: ")
        Madlib_Question.Spell2 = input("Give another spell chant: ")
    Madlib_Question.Adjective = input("Give an adjective: ")
    Madlib_Question.Adjective2 = input("Give another adjective: ")
    Madlib_Question.Noun = input("Give a noun: ")
    Madlib_Question.Noun2 = input("Give another noun: ")
    Madlib_Question.Location = input("Give a location: ")
    Madlib_Question.Location2 = input("Give another location: ")

    return Madlib_Question


    





