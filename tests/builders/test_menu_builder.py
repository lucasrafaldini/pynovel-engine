from unittest import TestCase, mock

import pygame

from builders.menu import MenuBuilder
from engine import Story


class TestMenuBuilder(TestCase):
    def setUp(self):
        self.story = Story(no_translation=True)
        self.story.selected_language = "English"
        self.story.add_scene("start", "Text", "Char")
        self.story.add_choice("start", "choice1", "start")
        self.story.add_choice("start", "choice2", "end_scene")
        self.menu_builder = MenuBuilder(self.story)

    def test_build_main_menu(self):

        # Just assert no raises happen
        self.assertEqual(self.menu_builder.build_main_menu(), None)
