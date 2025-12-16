import unittest
from datavisualizer.config.config import AppConfig

class ConfigTests(unittest.TestCase):

    def test_initializedAppConfig_hasDefaultValues(self):
        # Arrange/Act/Assert
        self.assertEqual(AppConfig.SECRET_KEY,
                         '7d4asdasda4fffa1afa27d4asd41f27567d441f2b6176a')
        self.assertTrue(AppConfig.DEBUG)
        self.assertTrue(AppConfig.CSRF_ENABLED)
