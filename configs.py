import os
import sys
from typing import Dict, List


class Config:
    """
    Configuration class for the game engine.

    Attributes:
        available_resolutions (list): A list of available resolutions.
        resolution (str): The default resolution of the game.
        image_path (str): The path to the images folder.
        game_icon (str): The path to the game icon.
        colors (dict): A dictionary mapping color names to RGB values.
        sizes (dict): A dictionary mapping size names to corresponding values.
        padding (int): The padding value (for the dialogue box).
        width (int): The width of the game window.
        height (int): The height of the game window.
        caption (str): The caption of the game window.
        available_languages (dict): A dictionary mapping language codes to language names. This can be modified to add or remove languages.
        languages (list): A list of available language names to be shown on the language menu.
        popup_settings (dict): A dictionary containing settings for different popup messages.
    """

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def __init__(self):
        self.available_resolutions: List[str] = ["hd", "fullhd", "4k"]

        # You can change the default resolution of the game here
        self.resolution: str = "hd"
        self.image_path: str = self.resource_path(
            f"resources/images/{self.resolution}/"
        )
        self.game_icon: str = f"{self.image_path}icon"

        # You can change the colors of the game here
        self.colors: Dict[str, tuple[int, int, int]] = {
            "white": (255, 255, 255),
            "green": (0, 255, 0),
            "red": (255, 0, 0),
            "black": (0, 0, 0),
            "regular_pink": (255, 105, 108),
            "active_pink": (255, 20, 147),
            "dialogue_box": (0, 0, 0, 128),
        }

        # You can change the sizes of the game here
        self.sizes: Dict[str, int] = {
            "small": 20,
            "medium": 40,
            "large": 60,
            "dialogue_box_height": 220,
            "ui": 30,
        }

        # You can change the padding value for the dialogue box here
        self.padding: int = 20

        # You can change the width and height of the game window here
        self.width: int = 1365
        self.height: int = 768

        # You can change the caption of the game window here
        self.caption: str = "PyNovel-Engine"

        # You can add or remove languages here
        self.available_languages: Dict[str, str] = {
            "en": "English",
            "pt": "Portuguese",
            "es": "Spanish",
            # "fr": "French",
            # "de": "Deustch",
        }
        self.languages: List[str] = [lang for lang in self.available_languages.values()]

        # You can change the popup settings here
        self.popup_settings: Dict[str, Dict[str, any]] = {
            "save_success": {
                "message": "Game saved successfully!",
                "position": (self.width // 2, self.height // 4),
                "duration": 3,
                "text_color": self.colors["green"],
                "bg_color": self.colors["black"],
                "font_size": 60,
                "alpha": 128,
            },
            "save_failed": {
                "message": "Failed to save game!",
                "position": (self.width // 2, self.height // 4),
                "duration": 3,
                "text_color": self.colors["red"],
                "bg_color": self.colors["black"],
                "font_size": 60,
                "alpha": 128,
            },
            "load_success": {
                "message": "Game loaded successfully!",
                "position": (self.width // 2, self.height // 4),
                "duration": 3,
                "text_color": self.colors["green"],
                "bg_color": self.colors["black"],
                "font_size": 60,
                "alpha": 128,
            },
            "load_failed": {
                "message": "Failed to load game!",
                "position": (self.width // 2, self.height // 4),
                "duration": 3,
                "text_color": self.colors["red"],
                "bg_color": (0, 0, 0),
                "font_size": 60,
                "alpha": 128,
            },
        }


config = Config()
