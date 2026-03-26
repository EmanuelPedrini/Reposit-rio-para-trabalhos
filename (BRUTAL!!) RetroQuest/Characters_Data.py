from Character import character
from Skill_Data import healing, fireball

Knight = character("Knight","she","her",5, 2, 5, 0, 3, 3, 10, 0, 0, [healing], [], 0 )
Mage = character("Mage","he", "his", 3, 3, 3, 1, 5, 5, 10, 0, 0, [fireball], [], 5)
Vampire= character("Vampire", "she", "her", 4, 2, 6, -1, 2, 2, 10, 20, 0, [], [], 0 )
Penintent= character("Penitent", "he", "his", 2, 1, 8, -3, 1, 1, 9, 0, 5, [], [], 0)

allcharacters=[Knight, Mage, Vampire, Penintent]