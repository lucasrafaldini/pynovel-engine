from googletrans import Translator

from configs import config

translator = Translator()


class TextManager:
    """
    A class that manages static texts for a game.
    The default language is English, but the class can be extended to support multiple languages.
    To do so, simply add languages on config.py and all translations will be generated automatically using the Google Translate API.

    Attributes:
        static_texts (dict): A dictionary containing static texts for different parts of the game.
            The structure of the dictionary is as follows:
            {
                "menu_items": {
                    "English": ["Start", "Load", "About", "Help", "Quit"]
                },
                "about": {
                    "English": ("About This Game", "Welcome to the heart of storytelling...")
                },
                "help": {
                    "English": ("How to Play", "Use the arrow keys to navigate the menus and press Enter to select an option.")
                },
                "dialogue": {
                    "English": ("Exit now", "Save"),
                },
                ...
            }
    """

    def __init__(self, no_translation=False):
        self.static_texts = {
            "menu_items": {"English": ["Start", "Load", "About", "Help", "Quit"]},
            "about": {
                "English": (
                    "About This Game",
                    """
                            Welcome to the heart of storytelling where imagination meets interactivity. 
                            This Novel Game Engine is the product of cutting-edge Python programming, 
                            harnessing the power of Pygame to deliver an unparalleled interactive experience.

                            With this engine, creators can weave intricate narratives, branch stories in complex ways, 
                            and bring characters to life, offering players a unique journey with each decision they make.
                            
                            Key Features:

                            - Dynamic Storytelling: Create stories with multiple paths and endings based on user choices.
                            
                            - Character Interaction: Develop deep characters and dynamic dialogues that respond to player actions.
                            
                            - Save and Resume: Players can save their progress and return to their story at any time, ensuring the adventure never misses a beat.
                            
                            - Multilingual Support: Stories crafted in one language bloom into a bouquet of languages with our built-in translation toolkit.
                            
                            - Simplified Deployment: Packaging and distributing your stories is a breeze with our built-in build system, whether you're targeting desktop or mobile platforms.
                            
                            Thank you for exploring this narrative adventure, and I look forward to the possibility of contributing to [Company Name]'s success.
                        """,
                )
            },
            "help": {
                "English": (
                    "How to Play",
                    "Use the arrow keys to navigate the menus and press Enter to select an option.",
                )
            },
            "dialogue": {
                "English": ("Exit now", "Save"),
            },
        }
        if not no_translation:
            for language in config.languages:
                self.static_texts["menu_items"][language] = [
                    translator.translate(
                        item,
                        src="en",
                        dest=list(config.available_languages.keys())[
                            list(config.available_languages.values()).index(language)
                        ],
                    ).text
                    for item in self.static_texts["menu_items"]["English"]
                ]

                self.static_texts["about"][language] = (
                    translator.translate(
                        self.static_texts["about"]["English"][0],
                        src="en",
                        dest=list(config.available_languages.keys())[
                            list(config.available_languages.values()).index(language)
                        ],
                    ).text,
                    translator.translate(
                        self.static_texts["about"]["English"][1],
                        src="en",
                        dest=list(config.available_languages.keys())[
                            list(config.available_languages.values()).index(language)
                        ],
                    ).text,
                )

                self.static_texts["help"][language] = (
                    translator.translate(
                        self.static_texts["help"]["English"][0],
                        src="en",
                        dest=list(config.available_languages.keys())[
                            list(config.available_languages.values()).index(language)
                        ],
                    ).text,
                    translator.translate(
                        self.static_texts["help"]["English"][1],
                        src="en",
                        dest=list(config.available_languages.keys())[
                            list(config.available_languages.values()).index(language)
                        ],
                    ).text,
                )

                self.static_texts["dialogue"][language] = (
                    translator.translate(
                        self.static_texts["dialogue"]["English"][0],
                        src="en",
                        dest=list(config.available_languages.keys())[
                            list(config.available_languages.values()).index(language)
                        ],
                    ).text,
                    translator.translate(
                        self.static_texts["dialogue"]["English"][1],
                        src="en",
                        dest=list(config.available_languages.keys())[
                            list(config.available_languages.values()).index(language)
                        ],
                    ).text,
                )


TextManagerInstance = TextManager()
