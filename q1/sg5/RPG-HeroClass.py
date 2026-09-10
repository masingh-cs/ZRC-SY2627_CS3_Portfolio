class Hero:
    def __init__(self, name, hp):
        # Store name and hp as instance attributes
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        # Subtract damage from hp
        self.hp -= amount


# ------------------------------------------------------------
# Step 3 — Instantiate two heroes and try them out.
# ------------------------------------------------------------
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(arthur.hp)     # Expected: 90
print(morgana.hp)    # Expected: 100
