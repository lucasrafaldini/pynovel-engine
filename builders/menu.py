from typing import TYPE_CHECKING, Dict, List

import pygame

from configs import Config, config

if TYPE_CHECKING:
    from engine import Story


class MenuBuilder:
    def __init__(self, story: "Story", config=config):
        """
        Initializes a Menu object.

        Args:
            story (Story): The story object.
            config (Config, optional): The configuration object for the menu. Defaults to config.

        Attributes:
            story (Story): The story object.
            screen (pygame.Surface): The screen surface to draw the menu on.
            config (Config): The configuration object for the menu.
            active_item_index (int): The index of the active menu item.
            width (int): The width of the menu.
            height (int): The height of the menu.
            colors (dict): A dictionary of color values for the menu.
            bg_color (tuple): The background color of the menu.
            font_color (tuple): The font color of the menu.
            active_item_color (tuple): The color of the active menu item.
            menu_font_size (int): The font size of the menu items.
            menu_items (list): A list of menu items.
            language_menu_font (pygame.font.Font): The font for the language menu items.
            main_menu_font (pygame.font.Font): The font for the main menu items.
        """
        self.story: Story = story
        self.screen: pygame.Surface = self.story.screen
        self.config: Config = config
        self.active_item_index: int = self.story.active_item_index
        self.width: int = self.config.width
        self.height: int = self.config.height
        self.colors: Dict[str, tuple[int, int, int]] = self.config.colors
        self.bg_color: tuple[int, int, int] = self.colors["black"]
        self.font_color: tuple[int, int, int] = self.colors["regular_pink"]
        self.active_item_color: tuple[int, int, int] = self.colors["active_pink"]
        self.menu_font_size: int = self.config.sizes["medium"]
        self.menu_items: List[str] = self.story.menu_items
        self.language_menu_font: pygame.font.Font = pygame.font.Font(
            None, self.menu_font_size
        )
        self.main_menu_font: pygame.font.Font = pygame.font.Font(
            None, self.menu_font_size
        )

    def build_language_menu(self) -> None:
        """
        Builds and displays the language menu on the screen.

        Returns:
            None
        """
        self.screen.fill(self.bg_color)
        for index, language in enumerate(self.story.languages):
            label = self.language_menu_font.render(language, True, self.font_color)
            x = self.width // 2
            y = (
                (self.height // 2)
                - (len(self.story.languages) * self.menu_font_size // 2)
                + (index * self.menu_font_size)
            )
            label_rect = label.get_rect(center=(x, y))

            if index == self.active_item_index:
                label = self.language_menu_font.render(
                    language, True, self.active_item_color
                )

            self.screen.blit(label, label_rect.topleft)

    def build_main_menu(self) -> None:
        """
        Builds the main menu based on the specified language.

        Returns:
            None

        """
        menu_items = self.menu_items[self.story.selected_language]
        max_label_width = max(
            [self.main_menu_font.size(item)[0] for item in menu_items]
        )
        menu_bg_width = max_label_width * 3
        menu_bg_height = self.height

        menu_bg_rect = pygame.Rect(0, 0, menu_bg_width, menu_bg_height)
        pygame.draw.rect(self.screen, self.colors["white"], menu_bg_rect)

        for index, item in enumerate(menu_items):
            label = self.main_menu_font.render(item, True, self.font_color)
            x = 10
            y = (
                (self.height // 2)
                - (len(menu_items) * self.menu_font_size // 2)
                + (index * self.menu_font_size)
            )
            label_rect = label.get_rect(x=x, centery=y)

            if index == self.active_item_index:
                label = self.main_menu_font.render(
                    item, True, self.active_item_color
                )  # Change text color for active item

            self.screen.blit(label, label_rect.topleft)
