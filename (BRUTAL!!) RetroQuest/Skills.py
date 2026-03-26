class skill:
    def __init__(self, name, description, damage, heal, cost):
          self.basename = name
          self.level=1
          self.description=description
          self.damage=damage
          self.cost=cost
          self.heal=heal
    def nome_modificado(self):
        return f"{self.basename} Lv {self.level}"
    def level_up(self):
        self.level+=1
        print(f"{self.basename} leveled up to Lv {self.level}!")

    def use(self, player, target):
            if not player.mana_use(self.cost):
                return False
            damage = self.damage
            if self.damage != 0:
                    target.toma(self.damage, player)
                    print(f"{player.name} used {self.basename} and caused {damage} damage to {target.name}!")
            if self.heal != 0:
                    player.heal(self.heal)
            return True