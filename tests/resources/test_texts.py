

from unittest import TestCase
from unittest.mock import MagicMock
from configs import config

from resources.texts import TextManager


class TestTexts(TestCase):

    def setUp(self):
        self.config = config
        self.text_manager = TextManager(no_translation=True)

    def test_text_manager(self):
        self.assertEqual(len(self.text_manager.static_texts.keys()),  4)
        self.assertEqual(len(self.text_manager.static_texts["menu_items"]["English"]),  5)

    # def test_text_manager_translation(self):
    #     for item in self.text_manager.static_texts.keys():
    #         self.assertEqual(list(self.text_manager.static_texts[item].keys()),  list(self.config.available_languages.values()))