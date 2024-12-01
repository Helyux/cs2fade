__author__ = "Lukas Mahler"
__version__ = "1.1.6"
__date__ = "06.10.2024"
__email__ = "m@hler.eu"
__status__ = "Production"


from cs2fade.BaseCalculator import BaseCalculator


class AcidFadeCalculator(BaseCalculator):

    def __init__(self):

        super().__init__()

        self.weapons = [
            'SSG 08',
        ]

        self.reversed_weapons = [
            'SSG 08',
        ]

        self.trade_up_weapons = [
            'SSG 08',
        ]

        self.configs = {
            'default': {
                'pattern_offset_x_start': -2.4,
                'pattern_offset_x_end': -2.1,
                'pattern_offset_y_start': 0.0,
                'pattern_offset_y_end': 0.0,
                'pattern_rotate_start': -55,
                'pattern_rotate_end': -65,
            }
        }


if __name__ == '__main__':
    exit(1)
