__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "04.11.2025"
__email__ = "m@hler.eu"
__status__ = "Production"


import cs2fade
from cs2fade import AcidFade, AmberFade, Fade, FadeInfo

if __name__ == "__main__":

    # Easy interface to query all fade finishes
    info: FadeInfo = cs2fade.get("M4A1-S", 374)
    print(f"[{info.weapon}] with seed {info.seed}: {info.percentage}% [{info.finish}] (Rank {info.ranking})")
    # -> [M4A1-S] with seed 374: 100.0% [fade] (Rank 1)


    ### Lower level API

    # Get a list of supported weapons
    print("Supported weapons for fade:", Fade.supported_weapons())
    # -> ['AWP', 'Bayonet', 'Bowie Knife', 'Butterfly Knife', 'Classic Knife', 'Falchion Knife', 'Flip Knife', ...]

    print("Supported weapons for acid fade:", AcidFade.supported_weapons())
    # -> ['SSG 08']

    print("Supported weapons for amber fade:", AmberFade.supported_weapons())
    # -> ['AUG', 'Galil AR', 'MAC-10', 'P2000', 'R8 Revolver', 'Sawed-Off']


    # Get the fade percentages for a specific weapon and seed
    fade = Fade.get_percentage(weapon := "M4A1-S", 374)
    print(f"Base fade percentage for [{weapon}] "
          f"with seed: {fade.seed} is {fade.percentage}% / ranked: {fade.ranking}")
    # -> Base fade percentage for [M4A1-S] with seed: 374 is 100.0% / ranked: 1

    # Get the acid fade percentages for a specific weapon and seed
    fade = AcidFade.get_percentage(weapon := "SSG 08", 576)
    print(f"Acid fade percentage for [{weapon}] "
          f"with seed: {fade.seed} is {fade.percentage}% / ranked: {fade.ranking}")
    # -> Acid fade percentage for [SSG 08] with seed: 576 is 100.0% / ranked: 1

    # Get the amber fade percentages for a specific weapon and seed
    fade = AmberFade.get_percentage(weapon := "R8 Revolver", 412)
    print(f"Amber fade percentage for [{weapon}] "
          f"with seed: {fade.seed} is {fade.percentage}% / ranked: {fade.ranking}")
    # -> Amber fade percentage for [R8 Revolver] with seed: 412 is 80.0% / ranked: 1
