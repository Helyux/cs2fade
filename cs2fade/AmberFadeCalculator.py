__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "12.07.2023"
__email__ = "m@hler.eu"
__status__ = "Production"


from cs2fade.BaseCalculator import BaseCalculator


class AmberFadeCalculator(BaseCalculator):

    def __init__(self):

        super().__init__()

        self.weapons = [
            'AUG',
            'Galil AR',
            'MAC-10',
            'P2000',
            'R8 Revolver',
            'Sawed-Off',
        ]

        self.reversed_weapons = []

        self.trade_up_weapons = [
            'AUG',
            'Galil AR',
            'MAC-10',
            'P2000',
            'R8 Revolver',
            'Sawed-Off',
        ]

        self.configs = {
            'default': {
                'pattern_offset_x_start': -0.7,
                'pattern_offset_x_end': -0.7,
                'pattern_offset_y_start': -0.7,
                'pattern_offset_y_end': -0.7,
                'pattern_rotate_start': -55,
                'pattern_rotate_end': -65,
            }
        }


if __name__ == '__main__':
    exit(1)
