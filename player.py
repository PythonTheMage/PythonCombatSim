# Player attributes (and inventory?)
# * = maybe

class player:
    # Attributes
    Attack = 0      # Base attack power before modifiers from equipment
    pDefence = 0    # Defence against physical attacks
    mDefence = 0    # Defence against magic attacks
    Agility = 0     # Accuracy and evasion
    Luck = 0        # Crit rate and evasion*

    # Sub-Attributes (Governed by main attributes and equipment)
    Accuracy = 0    # Chance of landing attacks
    Evasion = 0     # Chance of dodging attacks

    pass