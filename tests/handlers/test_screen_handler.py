import os
import shutil
from unittest import TestCase, mock
import pygame
from engine import Story

from handlers.screen import ScreenHandler


class TestScreenHandler(TestCase):

    def setUp(self):
        self.screen_handler = ScreenHandler
        self.story = Story(no_translation=True)
        self.story.add_scene("start", "Test text", "Test character")
        self.story.add_choice("start", "choice1", "start")
        self.story.add_choice("start", "choice2", "end_scene")

    def tearDown(self) -> None:
        if os.path.exists('saved_games'):
            shutil.rmtree('saved_games')
        return super().tearDown()


    def test_clear_screen(self):
        screen = mock.Mock(spec=pygame.Surface)
        bg_color = (255, 255, 255)

        self.screen_handler.clear_screen(screen, bg_color)

        screen.fill.assert_called_once_with(bg_color)

    def test_handle_about_screen_quit_event(self):
        event = pygame.event.Event(pygame.QUIT)

        self.screen_handler.handle_about_screen(self.story, event)

        self.assertFalse(self.story.running)

    def test_handle_about_screen_escape_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)

        self.screen_handler.handle_about_screen(self.story, event)

        self.assertEqual(self.story.current_game_state, self.story.possible_game_states.main_menu)
        self.assertEqual(self.story.active_item_index, 0)

    def test_handle_help_screen_quit_event(self):
        event = pygame.event.Event(pygame.QUIT)

        self.screen_handler.handle_help_screen(self.story, event)

        self.assertFalse(self.story.running)
    
    def test_handle_help_screen_escape_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)

        self.screen_handler.handle_help_screen(self.story, event)

        self.assertEqual(self.story.current_game_state, self.story.possible_game_states.main_menu)
        self.assertEqual(self.story.active_item_index, 0)

    def test_handle_game_dialogue_screen_quit_event(self):
        event = pygame.event.Event(pygame.QUIT)

        self.screen_handler.handle_game_dialogue_screen(self.story, event)

        self.assertFalse(self.story.running)

    def test_handle_game_dialogue_screen_escape_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)

        self.screen_handler.handle_game_dialogue_screen(self.story, event)

        self.assertFalse(self.story.running)

    def test_handle_game_dialogue_screen_return_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)

        self.screen_handler.handle_game_dialogue_screen(self.story, event)

        self.assertTrue(self.story.running)
        self.assertEqual(self.story.current_game_state, "in_choice")

    def test_handle_game_dialogue_screen_s_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_s)

        self.screen_handler.handle_game_dialogue_screen(self.story, event)

        self.assertTrue(self.story.running)
        self.assertTrue(os.path.exists('saved_games'))

    def test_handle_game_choice_screen_quit_event(self):
        event = pygame.event.Event(pygame.QUIT)

        self.screen_handler.handle_game_choice_screen(self.story, event)

        self.assertFalse(self.story.running)

    def test_handle_game_choice_screen_escape_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)

        self.screen_handler.handle_game_choice_screen(self.story, event)

        self.assertFalse(self.story.running)

    def test_handle_game_choice_screen_return_key(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        self.story.selected_language = "English"

        self.screen_handler.handle_game_choice_screen(self.story, event)

        self.assertTrue(self.story.running)
        self.assertNotEqual(self.story.current_game_state, "in_choice")

    
    

    