class PSHS_Galaxy:
    def __init__(self):
        self.name = "PSHS Galaxy"
        self.mood = "Void"

    def quote(self):
        return "[Nothingness]"

class Nationality(PSHS_Galaxy):
    def __init__(self):
        super().__init__()
        self.name = "Nationality"
        self.mood = "Patriotic"
        self.country = "Unknown"

    def quote(self):
        return "patriotic"

class Alien(PSHS_Galaxy):
    def __init__(self):
        super().__init__()
        self.name = "Alien"
        self.mood = "Curious"
        self.planet = "Unknown"

    def quote(self):
        return "[Alien langueage]"

class Filipino(Nationality):
    def __init__(self):
        super().__init__()
        self.name = "Filipino"
        self.country = "Philippines"
        self.language = "Filipino"
        self.favorite_food = "Milo and Rice"

    def quote(self):
        return "Rene ang bituwin ng Mindanao"

class Indonesian(Nationality):
    def __init__(self):
        super().__init__()
        self.name = "Indonesian"
        self.country = "Indonesia"
        self.language = "Bahasa Indonesia"
        self.favorite_food = "Beef Rendang"

    def quote(self):
        return "Sedikit-sedikit, lama-lama menjadi bukit."

class Spaniard(Nationality):
    def __init__(self):
        super().__init__()
        self.name = "Spaniard"
        self.country = "Spain"
        self.language = "Spanish"
        self.favorite_food = "Tortilla Española"

    def quote(self):
        return "Caminante, no hay camino, se hace camino al andar."

class Marvel(Alien):
    def __init__(self):
        super().__init__()
        self.name = "Marvel"
        self.planet = "Earth"
        self.hero = "Ant man"

    def quote(self):
        return "My days of breaking into places and stealing shit are over!"

class Avengers(Alien):
    def __init__(self):
        super().__init__()
        self.name = "Avengers"
        self.planet = "Earth"
        self.team_size = 6

    def quote(self):
        return "Avengers Assemble!"

everyone = [PSHS_Galaxy(), Nationality(), Alien(), Filipino(),
            Indonesian(), Spaniard(), Marvel(), Avengers()]

for obj in everyone:
    print(f"{obj.name} ({obj.mood}): {obj.quote()}")

print()
for nat in [Filipino(), Indonesian(), Spaniard()]:
    print(nat.country, "|", nat.language, "|", nat.favorite_food)
