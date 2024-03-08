from unittest import TestCase, mock
from unittest.mock import MagicMock

from resources.buttons import ChoicesButton, DialogueButton


class TestButtons(TestCase):

    def setUp(self):
        self.screen = MagicMock()
        self.font = MagicMock()
        self.config = {
            "bg_color": (255, 255, 255),
            "text_color": (0, 0, 0),
        }
        self.color = (255, 255, 255)
        self.bg_color = (255, 255, 255)
        self.x = 0
        self.y = 0
        self.width = 100
        self.height = 100
        self.text = "Test"

    @mock.patch("pygame.draw.rect")
    def test_dialogue_button(self, mock_draw_rect):
        mock_draw_rect.return_value = MagicMock()

        button = DialogueButton(
            self.screen,
            self.color,
            self.x,
            self.y,
            self.width,
            self.height,
            self.text,
            self.bg_color,
            self.font,
        )
        button.draw()
        self.screen.blit.assert_called_once()

    @mock.patch("pygame.draw.rect")
    def test_choices_button(self, mock_draw_rect):
        mock_draw_rect.return_value = MagicMock()

        button = ChoicesButton(
            self.screen,
            self.color,
            self.x,
            self.y,
            self.width,
            self.height,
            self.font,
            self.text,
            self.bg_color,
        )
        button.draw()
        self.screen.blit.assert_called_once()
