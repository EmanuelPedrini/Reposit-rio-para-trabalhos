from Itens import item
#weapons
rustysword=item("Rusty sword", "Weapon", 0)
iron_sword = item("Iron Sword", "Weapon", 3)
butchers_cleaver = item("Butcher's Cleaver", "Weapon", 5)

#lista com todas as weapons
todasaarmas=[rustysword, iron_sword, butchers_cleaver]

#armors
torn_clothes = item("Torn Clothes", "Armor", 1)
leather_armor = item("Leather Armor", "Armor", 3)
chainmail = item("Chainmail", "Armor", 5)

#lista com todas as armaduras
todasasarmors=[torn_clothes, leather_armor, chainmail]

#acsessories
old_ring = item("Old Ring", "Accessory", 1)
mana_pendant = item("Mana Pendant", "Accessory", 2)
lucky_charm = item("Lucky Charm", "Accessory", 3)

#lista com todos
todososacesssorios=[old_ring, mana_pendant, lucky_charm]

#lista com todos os equipamentos
todososequipamentos = todasaarmas + todososacesssorios + todasasarmors