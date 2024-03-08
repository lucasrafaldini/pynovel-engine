from unittest import TestCase, mock
import pygame

from builders.screen import ScreenBuilder
from engine import Story


class TestScreenBuilder(TestCase):
    def setUp(self):
        self.story = Story(no_translation=True)
        self.story.selected_language = "English"
        self.story.current_scene = "start"
        self.story.add_scene("start", "Text", "Char")
        self.story.add_choice("start", "choice1", "start")
        self.story.add_choice("start", "choice2", "end_scene")
        self.screen_builder = ScreenBuilder(self.story)


    def test_build_about_screen(self):
        # Just assert no raises happen
        self.assertEqual(self.screen_builder.build_about_screen(), None)

    def test_build_help_screen(self):
        # Just assert no raises happen
        self.assertEqual(self.screen_builder.build_help_screen(), None)

    def test_build_dialogue_screen(self):
        self.screen_builder.story.scenes = self.story.scenes[self.story.selected_language] 
        
        # Just assert no raises happen
        self.assertEqual(self.screen_builder.build_dialogue_screen(), None)

    def test_build_choice_screen(self):
        # Just assert no raises happen
        self.assertEqual(self.screen_builder.build_choice_screen(), None)

       