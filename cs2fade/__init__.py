__author__ = "Lukas Mahler"
__version__ = "0.0.0"
__date__ = "04.11.2025"
__email__ = "m@hler.eu"
__status__ = "Development"


from cs2fade.AcidFadeCalculator import AcidFadeCalculator as AcidFade
from cs2fade.AmberFadeCalculator import AmberFadeCalculator as AmberFade
from cs2fade.FadeCalculator import FadeCalculator as Fade
from cs2fade.Interfaces import FadeInfo, get

__all__ = [
    'Fade',
    'AcidFade',
    'AmberFade',
    'FadeInfo',
    'get',
]
