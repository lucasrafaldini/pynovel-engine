from unittest import TestCase

import pygame
from engine import Story

from handlers.menu import MenuHandler


class TestMenuHandler(TestCase):

    def setUp(self):
        self.screen_handler = MenuHandler
        self.selected_language = "English"
        self.story = Story(no_translation=True)
        self.story.selected_language = self.selected_language
        self.story.add_scene("start", "Test text", "Test character")
        self.story.add_choice("scene1", "choice1", "scene2")
        self.story.add_choice("scene1", "choice1", "end_scene")

    def test_handle_main_menu_quit_event(self):
        event = pygame.event.Event(pygame.QUIT)

        self.screen_handler.handle_main_menu(self.story, event)

        self.assertFalse(self.story.running)

    def test_handle_main_menu_escape_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)

        self.screen_handler.handle_main_menu(self.story, event)

        self.assertFalse(self.story.running)
    
    def test_handle_main_menu_up_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)

        self.screen_handler.handle_main_menu(self.story, event)

        self.assertEqual(self.story.active_item_index, len(self.story.menu_items) - 1)
    
    def test_handle_main_menu_down_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)

        self.screen_handler.handle_main_menu(self.story, event)

        self.assertEqual(self.story.active_item_index, 1)

    def test_handle_main_menu_return_key_quit(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        
        self.story.active_item_index = self.story.menu_items[self.selected_language].index("Quit")

        self.screen_handler.handle_main_menu(self.story, event)

        self.assertFalse(self.story.running)

    def test_handle_main_menu_return_key_about(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        self.story.active_item_index = self.story.menu_items[self.selected_language].index("About")

        self.screen_handler.handle_main_menu(self.story, event)

        self.assertEqual(self.story.current_game_state, self.story.possible_game_states.about)

    def test_handle_main_menu_return_key_help(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        self.story.active_item_index = self.story.menu_items[self.selected_language].index("Help")

        self.screen_handler.handle_main_menu(self.story, event)

        self.assertEqual(self.story.current_game_state, self.story.possible_game_states.help)

    def test_handle_main_menu_return_key_game(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        self.story.active_item_index = self.story.menu_items[self.selected_language].index("Start")

        self.screen_handler.handle_main_menu(self.story, event)

        self.assertEqual(self.story.current_game_state, self.story.possible_game_states.game)

    def test_handle_language_menu_quit_event(self):
        event = pygame.event.Event(pygame.QUIT)

        self.screen_handler.handle_language_menu(self.story, event)

        self.assertFalse(self.story.running)
    
    def test_handle_language_menu_escape_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)

        self.screen_handler.handle_language_menu(self.story, event)

        self.assertFalse(self.story.running)

    def test_handle_language_menu_up_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)

        self.screen_handler.handle_language_menu(self.story, event)

        self.assertEqual(self.story.active_item_index, len(self.story.languages) - 1)

    def test_handle_language_menu_down_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)

        self.screen_handler.handle_language_menu(self.story, event)

        self.assertEqual(self.story.active_item_index, 1)


    def test_handle_language_menu_return_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)

        self.screen_handler.handle_language_menu(self.story, event)

        self.assertEqual(self.story.selected_language, self.story.languages[self.story.active_item_index])
