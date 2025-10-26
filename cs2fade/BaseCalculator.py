__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "26.10.2025"
__email__ = "m@hler.eu"
__status__ = "Production"


from cs2fade.RandomNumberGenerator import RandomNumberGenerator


class FadePercentage:
    def __init__(self, seed, percentage, ranking):
        self.seed = seed
        self.percentage = percentage
        self.ranking = ranking


class WeaponFadePercentage:
    def __init__(self, weapon, percentages):
        self.weapon = weapon
        self.percentages = percentages


class BaseCalculator:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.initialized = True
            self.weapons = []
            self.reversed_weapons = []
            self.trade_up_weapons = []
            self.configs = {}
            self.min_percentage = 80

    @classmethod
    def supported_weapons(cls):
        instance = cls()
        return instance.weapons

    @classmethod
    def get_percentage(cls, weapon, seed):
        """Class-level method to get the fade percentage for a weapon and seed."""
        instance = cls()  # Get the singleton instance
        percentages = instance.get_fade_percentages(weapon)
        return percentages[seed]

    @classmethod
    def get_all_percentages(cls):
        """Class-level method to get all fade percentages."""
        instance = cls()  # Get the singleton instance
        return [
            WeaponFadePercentage(weapon, instance.get_fade_percentages(weapon))
            for weapon in instance.weapons
        ]

    @classmethod
    def get_fade_percentages(cls, weapon):
        """Class-level method to get fade percentages for a specific weapon."""
        instance = cls()  # Get the singleton instance
        if weapon not in instance.weapons:
            raise ValueError(f'The weapon "{weapon}" is currently not supported.')

        config = instance.configs.get(weapon, instance.configs['default'])
        raw_results = []
        max_seed = 1000 if weapon in instance.trade_up_weapons else 999

        for i in range(max_seed + 1):
            random_number_generator = RandomNumberGenerator()
            random_number_generator.set_seed(i)

            x_offset = random_number_generator.random_float(
                config['pattern_offset_x_start'], config['pattern_offset_x_end']
            )
            random_number_generator.random_float(
                config['pattern_offset_y_start'], config['pattern_offset_y_end']
            )
            rotation = random_number_generator.random_float(
                config['pattern_rotate_start'], config['pattern_rotate_end']
            )

            uses_rotation = config['pattern_rotate_start'] != config['pattern_rotate_end']
            uses_x_offset = config['pattern_offset_x_start'] != config['pattern_offset_x_end']

            if uses_rotation and uses_x_offset:
                raw_result = rotation * x_offset
            elif uses_rotation:
                raw_result = rotation
            else:
                raw_result = x_offset

            raw_results.append(raw_result)

        is_reversed = weapon in instance.reversed_weapons

        if is_reversed:
            best_result = min(raw_results)
            worst_result = max(raw_results)
        else:
            best_result = max(raw_results)
            worst_result = min(raw_results)

        result_range = worst_result - best_result
        percentage_results = [
            (worst_result - raw_result) / result_range
            for raw_result in raw_results
        ]
        sorted_percentage_results = sorted(percentage_results)

        return [
            FadePercentage(
                i,
                instance.min_percentage + (percentage_result * (100 - instance.min_percentage)),
                min(
                    sorted_percentage_results.index(percentage_result) + 1,
                    len(sorted_percentage_results) - sorted_percentage_results.index(percentage_result)
                )
            )
            for i, percentage_result in enumerate(percentage_results)
        ]


if __name__ == '__main__':
    exit(1)
