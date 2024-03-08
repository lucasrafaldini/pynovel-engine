from typing import TYPE_CHECKING
import pygame
from builders.popup import PopupBuilder
from managers.save_manager import CantSaveGame, SaveAndLoadManager

if TYPE_CHECKING:
    from engine import Story

class ScreenHandler:
    """
    A class that handles different screens in a game.

    Attributes:
        None

    Methods:
        clear_screen(screen, bg_color) -> None:
            Clear the screen with the background color.

        handle_about_screen(story, event):
            Handle the about screen based on the given event.

        handle_help_screen(story, event):
            Handle the help screen based on the given event.

        handle_game_dialogue_screen(story, event):
            Handle the game dialogue screen based on the given event.

        handle_game_choice_screen(story, event):
            Handle the game choice screen based on the given event.
    """

    def clear_screen(screen: pygame.Surface, bg_color: tuple[int, int, int]) -> None:
        """
        Clear the screen with the background color.
        """
        screen.fill(bg_color)

    def handle_about_screen(story: 'Story', event: pygame.event.Event) -> None:
        """
        Handles events for the about screen.

        Args:
            story (Story): The story object.
            event (pygame.event.Event): The event object.

        Returns:
            None
        """
        match event.type:
            case pygame.QUIT:
                story.running = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        story.current_game_state = story.possible_game_states.main_menu
                        story.active_item_index = 0

    def handle_help_screen(story: 'Story', event: pygame.event.Event) -> None:
        """
        Handles events for the help screen.

        Args:
            story (Story): The story object.
            event (pygame.event.Event): The event object.

        Returns:
            None
        """
        match event.type:
            case pygame.QUIT:
                story.running = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        story.current_game_state = story.possible_game_states.main_menu
                        story.active_item_index = 0

    def handle_game_dialogue_screen(story: 'Story', event: pygame.event.Event) -> None:
        """
        Handles events for the game dialogue screen.

        Args:
            story (Story): The story object.
            event (pygame.event.Event): The event object.

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
                    case pygame.K_s:
                        try:
                            SaveAndLoadManager.save_game(story.current_scene)
                            story.popup_info = PopupBuilder.init_popup(story.screen, mode="save_success")
                        except CantSaveGame as exc:
                            print(exc)
                            story.popup_info = PopupBuilder.init_popup(story.screen, mode="save_error") 
                    case pygame.K_RETURN:
                        story.current_game_state = "in_choice"

    def handle_game_choice_screen(story: 'Story', event: pygame.event.Event) -> None:
        """
        Handle the game choice screen based on the given event.

        Args:
            story (Story): The story object.
            event (pygame.event.Event): The event object.

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
                    case pygame.K_s:
                        try:
                            SaveAndLoadManager.save_game(story.current_scene)
                            story.popup_info = PopupBuilder.init_popup(story.screen, mode="save_success")
                        except CantSaveGame as exc:
                            print(exc)
                            story.popup_info = PopupBuilder.init_popup(story.screen, mode="save_error")
                    case pygame.K_UP:
                        story.active_item_index = (story.active_item_index - 1) % len(
                            story.choices[story.selected_language][story.current_scene]
                        )
                    case pygame.K_DOWN:
                        story.active_item_index = (story.active_item_index + 1) % len(
                            story.choices[story.selected_language][story.current_scene]
                        )
                    case pygame.K_RETURN:
                        if (
                            story.choices[story.selected_language][story.current_scene][
                                story.active_item_index
                            ][1]
                            == "end_scene"
                        ):
                            story.running = False
                        story.current_game_state = story.choices[
                            story.selected_language
                        ][story.current_scene][story.active_item_index][1]
                        story.possible_game_states.game_state = story.choices[
                            story.selected_language
                        ][story.current_scene][story.active_item_index][1]
                        story.current_scene = story.choices[story.selected_language][
                            story.current_scene
                        ][story.active_item_index][1]
