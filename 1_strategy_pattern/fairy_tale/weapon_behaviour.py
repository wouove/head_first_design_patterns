class WeaponBehaviour:
    def use_weapon(self):
        raise NotImplementedError("use_weapon() not implemented")


class KnifeBehaviour(WeaponBehaviour):
    def use_weapon(self):
        print("Cutting with a knife")


class BowAndArrowBehaviour(WeaponBehaviour):
    def use_weapon(self):
        print("Shooting with bow and arrow")


class AxeBehaviour(WeaponBehaviour):
    def use_weapon(self):
        print("Chopping with an axe")


class SwordBehaviour(WeaponBehaviour):
    def use_weapon(self):
        print("Swinging a sword")
