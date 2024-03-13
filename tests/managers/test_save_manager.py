import os
import shutil
import sys
from unittest import TestCase

from managers.save_manager import SaveAndLoadManager


class TestSaveManager(TestCase):

    def setUp(self):
        self.save_manager = SaveAndLoadManager

    def tearDown(self) -> None:
        if os.path.exists(
            os.path.join(os.path.dirname(sys.executable), "saved_games_test")
        ):
            shutil.rmtree(
                os.path.join(os.path.dirname(sys.executable), "saved_games_test")
            )
        return super().tearDown()

    def test_save_game(self):
        self.save_manager.save_game("state", "saved_games_test")

        self.assertTrue(
            os.path.exists(
                os.path.join(os.path.dirname(sys.executable), "saved_games_test")
            )
        )
        self.assertTrue(
            os.listdir(
                os.path.join(os.path.dirname(sys.executable), "saved_games_test")
            )
        )
        self.assertTrue(
            os.listdir(
                os.path.join(os.path.dirname(sys.executable), "saved_games_test")
            )[0].startswith("save_")
        )
        self.assertTrue(
            os.listdir(
                os.path.join(os.path.dirname(sys.executable), "saved_games_test")
            )[0].endswith(".json")
        )

    def test_load_game(self):
        self.save_manager.save_game("state", "saved_games_test")
        state = self.save_manager.load_game(
            os.path.join(os.path.dirname(sys.executable), "saved_games_test")
        )

        self.assertEqual(state, "state")
