__author__ = "Lukas Mahler"
__version__ = "1.0.0"
__date__ = "04.11.2025"
__email__ = "m@hler.eu"
__status__ = "Production"


import unittest

import cs2fade
from cs2fade import AcidFade, AmberFade, Fade, FadeInfo
from cs2fade.BaseCalculator import FadePercentage


class TestFadeCalculators(unittest.TestCase):

    def test_supported_weapons(self):
        # Test supported weapons for each calculator
        self.assertEqual(
            Fade.supported_weapons(),
            ['AWP', 'Bayonet', 'Bowie Knife', 'Butterfly Knife', 'Classic Knife', 'Falchion Knife',
             'Flip Knife', 'Glock-18', 'Gut Knife', 'Huntsman Knife', 'Karambit', 'Kukri Knife',
             'M4A1-S', 'M9 Bayonet', 'MAC-10', 'MP7', 'Navaja Knife', 'Nomad Knife', 'Paracord Knife',
             'R8 Revolver', 'Shadow Daggers', 'Skeleton Knife', 'Stiletto Knife', 'Survival Knife',
             'Talon Knife', 'UMP-45', 'Ursus Knife']
        )
        self.assertEqual(
            AcidFade.supported_weapons(),
            ['SSG 08']
        )
        self.assertEqual(
            AmberFade.supported_weapons(),
            ['AUG', 'Galil AR', 'MAC-10', 'P2000', 'R8 Revolver', 'Sawed-Off']
        )

    def test_fade_percentages(self):

        # Test high-end Fade percent
        fade = Fade.get_percentage("M4A1-S", 374)
        self.assertIsInstance(fade, FadePercentage)
        self.assertEqual(fade.seed, 374)
        self.assertAlmostEqual(fade.percentage, 100.00, places=2)
        self.assertEqual(fade.ranking, 1)

        # Test tradeup pattern 1000
        fade = Fade.get_percentage("Bowie Knife", 1000)
        self.assertIsInstance(fade, FadePercentage)
        self.assertEqual(fade.seed, 1000)
        self.assertAlmostEqual(fade.percentage, 81.4169, places=2)
        self.assertEqual(fade.ranking, 74)

        # Test low-end Fade percent
        fade = Fade.get_percentage("M9 Bayonet", 541)
        self.assertIsInstance(fade, FadePercentage)
        self.assertEqual(fade.seed, 541)
        self.assertAlmostEqual(fade.percentage, 80.2498, places=2)
        self.assertEqual(fade.ranking, 10)

        # Test random Fade percent
        fade = Fade.get_percentage("M9 Bayonet", 839)
        self.assertIsInstance(fade, FadePercentage)
        self.assertEqual(fade.seed, 839)
        self.assertAlmostEqual(fade.percentage, 87.4310, places=2)
        self.assertEqual(fade.ranking, 378)

        # Test fade percentage for AcidFade
        fade = AcidFade.get_percentage("SSG 08", 576)
        self.assertIsInstance(fade, FadePercentage)
        self.assertEqual(fade.seed, 576)
        self.assertAlmostEqual(fade.percentage, 100.00, places=2)
        self.assertEqual(fade.ranking, 1)

        # Test fade percentage for AmberFade
        fade = AmberFade.get_percentage("AUG", 763)
        self.assertIsInstance(fade, FadePercentage)
        self.assertEqual(fade.seed, 763)
        self.assertAlmostEqual(fade.percentage, 100.00, places=2)
        self.assertEqual(fade.ranking, 1)

    def test_module_level_get_defaults(self):
        result = cs2fade.get("M4A1-S", 374)
        self.assertIsInstance(result, FadeInfo)
        self.assertEqual(result.weapon, "M4A1-S")
        self.assertEqual(result.seed, 374)
        self.assertEqual(result.finish, "fade")
        self.assertAlmostEqual(result.percentage, 100.00, places=2)
        self.assertEqual(result.ranking, 1)

    def test_module_level_get_invalid_weapon(self):
        with self.assertRaises(ValueError):
            cs2fade.get("Imaginary Knife", 42)

    def test_module_level_get_infers_unique_finish(self):
        result = cs2fade.get("AUG", 763)
        self.assertEqual(result.finish, "amber")
        self.assertAlmostEqual(result.percentage, 100.00, places=2)
        self.assertEqual(result.ranking, 1)


if __name__ == '__main__':
    unittest.main()
