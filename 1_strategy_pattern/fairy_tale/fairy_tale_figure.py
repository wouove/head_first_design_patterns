from weapon_behaviour import KnifeBehaviour, BowAndArrowBehaviour, AxeBehaviour


class Character:
    def __init__(self, weapon_behaviour):
        self.weapon_behaviour = weapon_behaviour

    def set_weapon_behaviour(self, weapon_behaviour):
        self.weapon_behaviour = weapon_behaviour

    def fight(self):
        self.weapon_behaviour.use_weapon(self)


class Queen(Character):
    def __init__(self):
        super().__init__(KnifeBehaviour)


class King(Character):
    def __init__(self):
        super().__init__(SwordBehaviour)


class Troll(Character):
    def __init__(self):
        super().__init__(AxeBehaviour)


class Knight(Character):
    def __init__(self):
        super().__init__(BowAndArrowBehaviour)
