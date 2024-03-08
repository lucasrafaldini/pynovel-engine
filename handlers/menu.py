from typing import TYPE_CHECKING

import pygame

from builders.popup import PopupBuilder
from managers.save_manager import NoGameSaved, SaveAndLoadManager
from resources.texts import TextManagerInstance

if TYPE_CHECKING:
    from engine import Story


class MenuHandler:

    def handle_main_menu(
        story: "Story",
        event: pygame.event.Event,
    ) -> None:
        """
        Handles the main menu events and updates the game state, active item index, and running status.

        Args:
            story (Story): The story object.
            event (pygame.event.Event): The event to handle.

        Returns:
            None
        """
        match event.type:
            case pygame.QUIT:
                story.running = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        story.running = False
                    case pygame.K_UP:
                        story.active_item_index = (story.active_item_index - 1) % len(
                            story.menu_items
                        )
                    case pygame.K_DOWN:
                        story.active_item_index = (story.active_item_index + 1) % len(
                            story.menu_items
                        )
                    case pygame.K_RETURN:
                        if (
                            story.menu_items[story.selected_language][
                                story.active_item_index
                            ]
                            == TextManagerInstance.static_texts["menu_items"][
                                story.selected_language
                            ][-1]
                        ):
                            story.running = False
                        elif (
                            story.menu_items[story.selected_language][
                                story.active_item_index
                            ]
                            == TextManagerInstance.static_texts["menu_items"][
                                story.selected_language
                            ][2]
                        ):
                            story.current_game_state = story.possible_game_states.about
                        elif (
                            story.menu_items[story.selected_language][
                                story.active_item_index
                            ]
                            == TextManagerInstance.static_texts["menu_items"][
                                story.selected_language
                            ][3]
                        ):
                            story.current_game_state = story.possible_game_states.help
                        elif (
                            story.menu_items[story.selected_language][
                                story.active_item_index
                            ]
                            == TextManagerInstance.static_texts["menu_items"][
                                story.selected_language
                            ][0]
                        ):
                            story.current_game_state = story.possible_game_states.game

                        elif (
                            story.menu_items[story.selected_language][
                                story.active_item_index
                            ]
                            == TextManagerInstance.static_texts["menu_items"][
                                story.selected_language
                            ][1]
                        ):
                            print(
                                f"Selected: {story.menu_items[story.selected_language][story.active_item_index]}"
                            )
                            try:
                                last_saved_state: str = SaveAndLoadManager.load_game()
                                story.popup_info = PopupBuilder.init_popup(
                                    story.screen, mode="load_success"
                                )
                                # Wait a little bit before redirecting user to the state from the game
                                # the user previously saved
                                pygame.time.wait(2000)
                                story.current_game_state = (
                                    story.possible_game_states.game
                                )
                                story.current_scene = last_saved_state
                            except NoGameSaved as exc:
                                print(exc.message)
                                story.popup_info = PopupBuilder.init_popup(
                                    story.screen, mode="load_failed"
                                )

    def handle_language_menu(
        story: "Story",
        event: pygame.event.Event,
    ):
        """
        Handles the language menu events.

        Args:
            story (Story): The story object.
            event (pygame.event.Event): The event to handle.

        Returns:
            tuple: A tuple containing the updated current game state, active item index, and running flag.
        """
        match event.type:
            case pygame.QUIT:
                story.running = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        story.running = False
                    case pygame.K_UP:
                        story.active_item_index = (story.active_item_index - 1) % len(
                            story.languages
                        )
                    case pygame.K_DOWN:
                        story.active_item_index = (story.active_item_index + 1) % len(
                            story.languages
                        )
                    case pygame.K_RETURN:
                        story.current_game_state = story.possible_game_states.main_menu
                        story.selected_language = story.languages[
                            story.active_item_index
                        ]
                        story.active_item_index = 0
