# tests/test_read_settings.py

import unittest
from read_settings import ReadSettings

class TestReadSettings(unittest.TestCase):
    def test_load_settings(self):
        settings = ReadSettings()
        settings.load_settings()
        self.assertTrue(isinstance(settings.settings, dict))

    def test_save_settings(self):
        settings = ReadSettings()
        settings.settings["reservoir_size"] = 2000
        settings.save_settings()
        self.assertTrue(settings.settings["reservoir_size"], 2000)

if __name__ == "__main__":
    unittest.main()
