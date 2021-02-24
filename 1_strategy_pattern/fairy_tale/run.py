from fairy_tale_figure import Queen
from weapon_behaviour import AxeBehaviour

if __name__ == '__main__':
    queen = Queen()
    queen.fight()
    queen.set_weapon_behaviour(AxeBehaviour)
    queen.fight()
