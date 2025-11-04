__author__ = "Lukas Mahler"
__version__ = "0.0.0"
__date__ = "04.11.2025"
__email__ = "m@hler.eu"
__status__ = "Development"


from dataclasses import dataclass
from typing import Optional

from cs2fade.AcidFadeCalculator import AcidFadeCalculator as AcidFade
from cs2fade.AmberFadeCalculator import AmberFadeCalculator as AmberFade
from cs2fade.FadeCalculator import FadeCalculator as Fade


@dataclass(frozen=True)
class FadeInfo:
    weapon: str
    seed: int
    percentage: float
    ranking: int
    finish: str


_CALCULATORS = {
    'fade': Fade,
    'amber': AmberFade,
    'acid': AcidFade,
}

_SUPPORTED_WEAPONS = {
    finish: calculator.supported_weapons() for finish, calculator in _CALCULATORS.items()
}


def _resolve_finish_for_weapon(weapon: str, finish: Optional[str] = None) -> str:
    """Map a weapon name to the finish that supports it."""
    if finish is not None:
        if finish not in _CALCULATORS:
            raise ValueError(f"Unknown finish [{finish}].")
        if weapon not in _SUPPORTED_WEAPONS.get(finish, []):
            raise ValueError(f"Weapon [{weapon}] is not supported by the finish [{finish}].")
        return finish

    matching_finishes = [
        finish_name
        for finish_name, weapons in _SUPPORTED_WEAPONS.items()
        if weapon in weapons
    ]

    if not matching_finishes:
        raise ValueError(f"Weapon [{weapon}] is not supported by any fade calculator.")

    # Prefer base fade over other fade types
    if 'fade' in matching_finishes:
        return 'fade'

    if len(matching_finishes) == 1:
        return matching_finishes[0]

    matches = ', '.join(matching_finishes)
    raise ValueError(
        f"Weapon [{weapon}] is ambiguous across finishes: [{matches}]. "
        f"This weapon can therefore not be resolved automatically."
    )


def get(weapon: str, seed: int, finish: Optional[str] = None) -> FadeInfo:
    """
    Return fade information for the given weapon and seed.

    When the finish is omitted, the helper prefers the base fade whenever it
    is available for the weapon. Providing a finish overrides this inference
    and validates the chosen combination.
    """
    resolved_finish = _resolve_finish_for_weapon(weapon, finish)
    calculator = _CALCULATORS[resolved_finish]
    result = calculator.get_percentage(weapon, seed)
    return FadeInfo(
        weapon=weapon,
        seed=result.seed,
        percentage=result.percentage,
        ranking=result.ranking,
        finish=resolved_finish,
    )

if __name__ == '__main__':
    exit(1)
