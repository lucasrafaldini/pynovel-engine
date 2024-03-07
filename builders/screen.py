from typing import TYPE_CHECKING

import pygame
from configs import Config, config
from resources.buttons import ChoicesButton, DialogueButton
from resources.texts import TextManagerInstance


if TYPE_CHECKING:
    from engine import Story

class ScreenBuilder:
    def __init__(self, story: 'Story', config: Config=config):
        """
        Initializes a new instance of the Screens class.

        Args:
            story (Story): The story object.
            config (Config, optional): The configuration object. Defaults to config.

        Attributes:
            screen (pygame.Surface): The screen surface to draw on.
            language (str): The language to use for text rendering.
            config (Config): The configuration object.
            text_font (pygame.font.Font): The font for small text.
            dialogue_font (pygame.font.Font): The font for medium text present in dialogue screens.
        """
        self.story = story
        self.screen = self.story.screen
        self.language = self.story.selected_language
        self.config = config
        self.text_font = pygame.font.Font(None, self.config.sizes["small"])
        self.dialogue_font = pygame.font.Font(None, self.config.sizes["medium"])

    def build_about_screen(self) -> None:
        """
        Builds the about screen.

        This method fills the screen with a black color and displays the title and about text on the screen.

        Args:
            None

        Returns:
            None
        """
        self.screen.fill(self.config.colors["black"])

        title_text = TextManagerInstance.static_texts["about"][self.language][0]
        title_font = pygame.font.Font(None, self.config.sizes["large"])
        title_surface = title_font.render(
            title_text, True, self.config.colors["active_pink"]
        )
        title_rect = title_surface.get_rect(
            center=(self.config.width // 2, self.config.height // 4)
        )
        self.screen.blit(title_surface, title_rect)

        about_text = TextManagerInstance.static_texts["about"][self.language][1]
        about_lines = about_text.split("\n")

        for i, line in enumerate(about_lines):
            line_surface = self.text_font.render(
                line, True, self.config.colors["regular_pink"]
            )
            line_rect = line_surface.get_rect(
                center=(
                    self.config.width // 2.1,
                    title_rect.bottom + 20 + i * self.text_font.get_linesize(),
                )
            )
            self.screen.blit(line_surface, line_rect)

    def build_help_screen(self) -> None:
        """
        Builds the help screen with the title and about text.

        This method fills the screen with a black color and then renders the title and about text on the screen.

        Args:
            None

        Returns:
            None
        """
        self.screen.fill(self.config.colors["black"])

        title_text = TextManagerInstance.static_texts["help"][self.language][0]
        title_font = pygame.font.Font(None, self.config.sizes["large"])
        title_surface = title_font.render(
            title_text, True, self.config.colors["active_pink"]
        )
        title_rect = title_surface.get_rect(
            center=(self.config.width // 2, self.config.height // 4)
        )
        self.screen.blit(title_surface, title_rect)

        about_text = TextManagerInstance.static_texts["help"][self.language][1]
        about_lines = about_text.split("\n")

        for i, line in enumerate(about_lines):
            line_surface = self.text_font.render(
                line, True, self.config.colors["regular_pink"]
            )
            line_rect = line_surface.get_rect(
                center=(
                    self.config.width // 2.1,
                    title_rect.bottom + 20 + i * self.text_font.get_linesize(),
                )
            )
            self.screen.blit(line_surface, line_rect)

    def build_dialogue_screen(self) -> None:
        """
        Builds a dialogue screen with a character image, dialogue text, character name, and dialogue buttons.

        Args:
            current_scene (str): The current scene to display on the screen.
        Returns:
            None
        """
        current_scene = self.story.scenes[self.story.current_scene]
        character_image, dialogue, character_name = current_scene["image"], current_scene["description"], current_scene["character_name"]

        self.screen.fill(self.config.colors["white"])

        if character_image:
            character = pygame.image.load(character_image)
            character_rect = character.get_rect(
                center=(self.config.width // 2, (self.config.height // 5) * 2)
            )
            self.screen.blit(character, character_rect)

        # Dialogue box
        dialogue_box_rect = pygame.Rect(
            0,
            self.config.height - self.config.sizes["dialogue_box_height"],
            self.config.width,
            self.config.sizes["dialogue_box_height"],
        )
        pygame.draw.rect(
            self.screen, self.config.colors["dialogue_box"], dialogue_box_rect
        )

        # Character name
        name_text_surface = self.dialogue_font.render(
            character_name, True, self.config.colors["black"]
        )
        name_text_rect = name_text_surface.get_rect(
            bottomleft=(
                self.config.padding,
                dialogue_box_rect.top - self.config.padding,
            )
        )
        self.screen.blit(name_text_surface, name_text_rect)

        # Dialogue text
        dialogue_lines = dialogue.split("\n")
        for i, line in enumerate(dialogue_lines):
            line_surface = self.dialogue_font.render(
                line, True, self.config.colors["white"]
            )
            line_rect = line_surface.get_rect(
                topleft=(
                    self.config.padding,
                    dialogue_box_rect.top
                    + self.config.padding
                    + i * self.dialogue_font.get_linesize(),
                )
            )
            self.screen.blit(line_surface, line_rect)

        button_font = pygame.font.Font(None, self.config.sizes["ui"])
        dialogue_buttons = [
            DialogueButton(
                self.screen,
                self.config.colors["dialogue_box"],
                self.config.width // 3,
                self.config.height - 50,
                100,
                30,
                f'{TextManagerInstance.static_texts["dialogue"][self.language][0]} (ESC)',
                self.config.colors["white"],
                button_font,
            ),
            DialogueButton(
                self.screen,
                self.config.colors["dialogue_box"],
                (self.config.width // 3) * 2,
                self.config.height - 50,
                100,
                30,
                f'{TextManagerInstance.static_texts["dialogue"][self.language][1]} (S)',
                self.config.colors["white"],
                button_font,
            ),
        ]

        # Draw buttons
        for button in dialogue_buttons:
            button.draw()

    def build_choice_screen(self) -> None:
        """
        Builds a choice screen with buttons for each choice.

        Args:
            choices (list): A list of choices to be displayed on the screen.
            active_item_index (int, optional): The index of the active choice. Defaults to 0.

        Returns:
            tuple: A tuple containing the choice buttons and the active item index.
        """
        self.screen.fill(self.config.colors["white"])
        choices_list = [item[0] for item in self.story.choices[self.story.selected_language][self.story.current_scene]]
        for i, choice in enumerate(choices_list):
            button = ChoicesButton(
                self.screen,
                choice,
                self.config.width // 2 - 200,
                self.config.height // 2 + i * 50,
                400,
                40,
                self.text_font,
                self.config.colors["black"],
                (
                    self.config.colors["active_pink"]
                    if self.story.active_item_index == i
                    else self.config.colors["white"]
                ),
            )
            self.story.choices_items.append(button)

        for button in self.story.choices_items:
            button.draw()
