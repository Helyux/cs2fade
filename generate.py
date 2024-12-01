__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "02.12.2024"
__email__ = "m@hler.eu"
__status__ = "Production"


import json
import os

from cs2fade import AcidFade, AmberFade, Fade


def main():
    """
    Generate static .json files, this is different from the original TypeScript repository.
    I like this .json format more for accessing the seeds later.
    e.g. ['AWP']['42']['percentage'], where 42 is the seed.
    """

    # Ensure the output directory exists
    output_dir = os.path.normpath("./generated")
    os.makedirs(output_dir, exist_ok=True)

    # Build a new dict using format [WEAPON][SEED] = seed, percentage, ranking
    for calc_cls, name in [(Fade, 'fade'), (AmberFade, 'fade_amber'), (AcidFade, 'fade_acid')]:
        rebuild = {}
        for obj in calc_cls.get_all_percentages():
            weapon_name = obj.weapon
            rebuild[weapon_name] = {}
            for subobj in obj.percentages:
                rebuild[weapon_name][subobj.seed] = {
                    'seed': subobj.seed,
                    'percentage': subobj.percentage,
                    'ranking': subobj.ranking
                }

        # Dump the new dicts to a JSON file using 4 indents under ./generated
        output_path = os.path.normpath(os.path.join(output_dir, f"{name}.json"))
        with open(output_path, 'w') as jf:
            json.dump(rebuild, jf, indent=4)

        print(f"Generated JSON for {name:10s}: {output_path}")


if __name__ == '__main__':
    main()
