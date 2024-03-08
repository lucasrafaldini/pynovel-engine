import sys
from typing import List

import pygame
from googletrans import Translator

from builders.menu import MenuBuilder
from builders.popup import PopupBuilder
from builders.screen import ScreenBuilder
from configs import Config, config
from errors.story import StoryCohesionError
from handlers.menu import MenuHandler
from handlers.screen import ScreenHandler
from resources.buttons import ChoicesButton
from resources.texts import TextManagerInstance

translator = Translator()


class States:
    def __init__(self):
        self.language_menu = 1
        self.main_menu = 2
        self.game = 3
        self.about = 4
        self.help = 5
        self.quit = 6
        self.game_state = "start"


class Story:
    def __init__(
        self, states: States = States(), config: Config = config, no_translation=False
    ) -> None:
        """
        Initialize the Story class.

        Args:
            states (States, optional): The states of the game. Defaults to States().
            config (dict, optional): The configuration of the game. Defaults to config inside configs.py file.
        """
        self.config: Config = config
        self.caption: str = self.config.caption
        self.width: int = self.config.width
        self.height: int = self.config.height
        self.menu_items: List[str] = TextManagerInstance.static_texts["menu_items"]
        self.menu_font_size: int = self.config.sizes["medium"]
        self.languages: List[str] = self.config.languages
        self.selected_language: str = None
        self.colors: dict = self.config.colors
        self.active_item_color: tuple = self.colors["active_pink"]
        self.bg_color: tuple = self.colors["black"]
        self.font_color: tuple = self.colors["regular_pink"]
        self.possible_game_states = states
        self.current_game_state: int = self.possible_game_states.language_menu
        self.scenes: dict = {}
        self.current_scene: str = "start"
        self.choices_items: List[ChoicesButton] = []
        self.choices: dict = {}
        self.current_choice: str = None
        self.active_item_index: int = 0
        self.running: bool = True
        self.game_icon = pygame.image.load(self.config.game_icon)
        pygame.display.set_icon(self.game_icon)
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title=self.caption, icontitle=self.caption)
        self.menu_font = pygame.font.Font(None, self.menu_font_size)
        self.popup_info = None
        self.no_translation = no_translation

    def run(self) -> None:
        # Check if the story has been defined and if it has a ending
        self.check_story()

        # Main game loop
        while self.running:
            self.screen_manager()
            self.pre_game_event_handler()
            if self.popup_info:
                # If popup duration has passed, stop showing the popup
                if not PopupBuilder.draw_popup(self.screen, self.popup_info):
                    self.popup_info = None
            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def check_story(self) -> None:
        """
        Checks if the story has been defined and if it has a ending.

        If the story has not been defined, if the choices weren't defined, if every scene doesn't have at least 2 choices or if the story
        doesn't have an ending, it raises a StoryCohesionError.

        Returns:
            None
        """
        has_start = False
        has_end = False
        has_multiple_choices = True
        for lang in list(self.choices.values()):
            for scene in list(lang.values()):
                if len(scene) < 2:
                    has_multiple_choices = False
                for choice in scene:
                    if choice[1] == "end_scene":
                        has_end = True
                    if choice[1] == "start":
                        has_start = True

        if not all([self.scenes, self.choices, has_end, has_start, has_multiple_choices]):
            raise StoryCohesionError
        print("Story is cohesive")

    def add_scene(
        self,
        scene_name: str,
        description: str,
        character_name: str = "",
        image: str = "boilerplate.png",
    ) -> None:
        image = f"{self.config.image_path}{image}"
        if not self.no_translation:
            for language in self.languages:
                if language not in self.scenes:
                    self.scenes[language] = {}
                self.scenes[language][scene_name] = {
                    "description": translator.translate(
                        description,
                        src="en",
                        dest=list(config.available_languages.keys())[
                            list(config.available_languages.values()).index(language)
                        ],
                    ).text,
                    "image": image,
                    "character_name": character_name,
                }
        else:
            if "English" not in self.scenes:
                self.scenes["English"] = {}
            self.scenes["English"][scene_name] = {
                "description": description,
                "image": image,
                "character_name": character_name,
            }

    def add_choice(self, scene: str, choice: str, next_scene: str) -> None:
        """
        Adds a choice to the specified scene in multiple languages.

        Args:
            scene (str): The scene to add the choice to.
            choice (str): The choice text.
            next_scene (str): The next scene to transition to after selecting the choice.

        Returns:
            None
        """
        if not self.no_translation:
            for language in self.languages:
                if language not in self.choices:
                    self.choices[language] = {}
                if scene in self.choices[language]:
                    self.choices[language][scene].append(
                        (
                            translator.translate(
                                choice,
                                src="en",
                                dest=list(config.available_languages.keys())[
                                    list(config.available_languages.values()).index(
                                        language
                                    )
                                ],
                            ).text,
                            next_scene,
                        )
                    )
                else:
                    if "English" not in self.choices:
                        self.choices[language] = {}
                    self.choices[language][scene] = [
                        (
                            translator.translate(
                                choice,
                                src="en",
                                dest=list(config.available_languages.keys())[
                                    list(config.available_languages.values()).index(
                                        language
                                    )
                                ],
                            ).text,
                            next_scene,
                        )
                    ]
        else:
            if "English" not in self.choices:
                self.choices["English"] = {}
            if scene in self.choices["English"]:
                self.choices["English"][scene].append((choice, next_scene))
            else:
                self.choices["English"][scene] = [(choice, next_scene)]

    def screen_manager(self) -> None:
        """
        Manages the screen based on the current game state.

        This method clears the screen, determines the current game state, and builds the appropriate menu or screen
        based on the game state. It also handles the flow of the game by calling the `StoryFlow` class to run the flow
        of the game based on the current game state.

        Returns:
            None
        """
        ScreenHandler.clear_screen(self.screen, self.bg_color)

        match self.current_game_state:
            case self.possible_game_states.language_menu:
                MenuBuilder(self).build_language_menu()
            case self.possible_game_states.main_menu:
                MenuBuilder(self).build_main_menu()
            case self.possible_game_states.about:
                ScreenBuilder(self).build_about_screen()
            case self.possible_game_states.help:
                ScreenBuilder(self).build_help_screen()
            case _:
                StoryFlow(self).run_flow()

    def pre_game_event_handler(self) -> None:
        """
        Handles pre-game events based on the current game state.

        This method processes events from the Pygame event queue and performs
        different actions based on the current game state. It calls different
        handler methods depending on the game state to handle specific events.

        Returns:
            None
        """
        for event in pygame.event.get():
            match self.current_game_state:
                case self.possible_game_states.language_menu:
                    MenuHandler.handle_language_menu(self, event)
                case self.possible_game_states.main_menu:
                    MenuHandler.handle_main_menu(self, event)
                case self.possible_game_states.about:
                    ScreenHandler.handle_about_screen(self, event)
                case self.possible_game_states.help:
                    ScreenHandler.handle_help_screen(self, event)
                case _:
                    self.game_event_handler(event)

    def game_event_handler(self, event: pygame.event.Event) -> None:
        """
        Handles game events based on the current game state.

        Args:
            event: The event to be handled.

        Returns:
            None
        """
        match self.current_game_state:
            case "in_choice":
                ScreenHandler.handle_game_choice_screen(self, event)
            case _:
                ScreenHandler.handle_game_dialogue_screen(self, event)


class StoryFlow:
    """
    Represents the flow of a story in a game.

    Attributes:
        possible_game_states (list): A list of possible game states.
        current_game_state (str): The current game state.
        scenes (dict): A dictionary containing the scenes of the story.
        current_scene (str): The current scene.
        choices (dict): A dictionary containing the choices available in each scene.
        current_choice (str): The current choice.
        choices_items (list): A list of choices buttons.
        screen: The screen object used for displaying the game.
        selected_language (str): The selected language for the game.
        active_item_index (int, optional): The index of the active item in the choices screens. Defaults to 0.
    """

    def __init__(self, story: Story) -> None:
        self.possible_game_states = story.possible_game_states
        self.current_game_state = story.current_game_state
        self.scenes = story.scenes[story.selected_language]
        self.current_scene = story.current_scene
        self.choices = story.choices
        self.current_choice = story.current_choice
        self.choices_items: List[ChoicesButton] = []
        self.screen = story.screen
        self.selected_language = story.selected_language
        self.active_item_index = story.active_item_index

    def run_flow(self) -> None:
        """
        Runs the flow of the story.

        Returns:
            None
        """
        match self.current_game_state:
            case "in_choice":
                ScreenBuilder(self).build_choice_screen()
            case _:
                ScreenBuilder(self).build_dialogue_screen()
