from unittest import TestCase
from unittest import mock
from unittest.mock import MagicMock
from engine import Story, States
from errors.story import StoryCohesionError
from configs import config
from unittest import mock

class StoryTest(TestCase):

    def setUp(self):
        self.story = Story()
        self.screen_handler = MagicMock()
        self.menu_builder = MagicMock()
        self.states = States()
        self.config = config

    def test_check_story(self):

        self.story.add_scene("scene1", "This is the first scene")
        self.story.add_choice("scene1", "choice1", "end_scene")
        self.story.add_choice("scene1", "choice2", "scene1")

        self.assertEqual(self.story.check_story(), None)

    def test_check_story_exception_just_one_choice(self):

        self.story.add_scene("scene1", "This is the first scene")
        self.story.add_choice("scene1", "choice1", "end_scene")

        self.assertRaises(StoryCohesionError, self.story.check_story)

    def test_check_story_exception_no_end(self):

        self.story.add_scene("scene1", "This is the first scene")
        self.story.add_choice("scene1", "choice1", "scene1")
        self.story.add_choice("scene1", "choice2", "scene1")

        self.assertRaises(StoryCohesionError, self.story.check_story)

    def test_add_scene(self):
        expected_scene = ("scene1", "This is the first scene")

        self.story.add_scene(expected_scene[0], expected_scene[1])

        languages = self.config.languages
        
        self.assertEqual(list(self.story.scenes.keys()), languages)
        for language in languages:
            self.assertEqual(list(self.story.scenes[language].keys())[0], expected_scene[0])

    @mock.patch('builders.menu.MenuBuilder.build_language_menu')
    def test_screen_manager_language_menu_flow(self, mock_build_language_menu):
        self.story.current_game_state = self.states.language_menu
        self.story.screen_manager()

        mock_build_language_menu.assert_any_call()

    @mock.patch('builders.menu.MenuBuilder.build_main_menu')
    def test_screen_manager_main_menu_flow(self, mock_build_main_menu):
        self.story.current_game_state = self.states.main_menu
        self.story.screen_manager()

        mock_build_main_menu.assert_any_call()

    @mock.patch('builders.screen.ScreenBuilder.build_about_screen')
    def test_screen_manager_language_menu_flow(self, mock_build_about_screen):
        self.story.current_game_state = self.states.about
        self.story.screen_manager()

        mock_build_about_screen.assert_any_call()

    @mock.patch('builders.screen.ScreenBuilder.build_help_screen')
    def test_screen_manager_language_menu_flow(self, mock_build_help_screen):
        self.story.current_game_state = self.states.help
        self.story.screen_manager()

        mock_build_help_screen.assert_any_call()

    # @mock.patch('engine.StoryFlow.run_flow')
    # def test_screen_manager_language_menu_flow(self, mock_story_flow):
    #     self.story.current_game_state = self.states.game
    #     self.story.screen_manager()

    #     mock_story_flow.assert_any_call()
