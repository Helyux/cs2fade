__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "02.12.2024"
__email__ = "m@hler.eu"
__status__ = "Production"


from cs2fade import AcidFade, AmberFade, Fade

if __name__ == "__main__":

    # Get list of supported weapons
    print("Supported weapons for fade:      ", Fade.supported_weapons())
    print("Supported weapons for acid fade: ", AcidFade.supported_weapons())
    print("Supported weapons for amber fade:", AmberFade.supported_weapons())

    # Get the fade percentages for a specific weapon and seed
    fade = Fade.get_percentage(weapon := "M4A1-S", 374)
    print(f"Base fade percentage for  [{weapon:>6s}] "
          f"with seed: {fade.seed:4d} is {fade.percentage:6.2f}% / ranked: {fade.ranking:3d}")

    # Get the acid fade percentages for a specific weapon and seed
    fade = AcidFade.get_percentage(weapon := "SSG 08", 576)
    print(f"Acid fade percentage for  [{weapon:>6s}] "
          f"with seed: {fade.seed:4d} is {fade.percentage:6.2f}% / ranked: {fade.ranking:3d}")

    # Get the amber fade percentages for a specific weapon and seed
    fade = AmberFade.get_percentage(weapon := "AUG", 763)
    print(f"Amber fade percentage for [{weapon:>6s}] "
          f"with seed: {fade.seed:4d} is {fade.percentage:6.2f}% / ranked: {fade.ranking:3d}")
