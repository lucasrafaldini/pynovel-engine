import pygame


class DialogueButton:
    def __init__(
        self,
        screen: pygame.Surface,
        color: tuple,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        text_color: tuple,
        font: pygame.font.Font,
    ) -> None:
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.font = font

    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)


class ChoicesButton:
    """
    Represents a button with customizable text, position, size, and appearance.

    Args:
        screen (pygame.Surface): The surface on which the button will be drawn.
        text (str): The text to be displayed on the button.
        x (int): The x-coordinate of the top-left corner of the button.
        y (int): The y-coordinate of the top-left corner of the button.
        width (int): The width of the button.
        height (int): The height of the button.
        font (pygame.font.Font): The font used for the button text.
        bg_color (tuple): The background color of the button in RGB format.
        text_color (tuple): The color of the button text in RGB format.
    """

    def __init__(
        self,
        screen: pygame.Surface,
        text: str,
        x: int,
        y: int,
        width: int,
        height: int,
        font: pygame.font.Font,
        bg_color: tuple,
        text_color: tuple,
    ) -> None:
        self.screen = screen
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color

    def draw(self) -> None:
        """
        Draws the button on the screen.
        """
        # Draw the button rectangle
        pygame.draw.rect(self.screen, self.bg_color, self.rect)
        # Draw the button text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)
