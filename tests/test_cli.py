import os
import subprocess
from unittest import TestCase

from pytest import MonkeyPatch

from cli import build_visual_novel
from configs import config


class TestCli(TestCase):

    def setUp(self):
        self.source_dir = "tests/test_data"
        self.output_dir = "tests/test_data"
        self.platforms = ["linux", "windows"]
        self.resolutions = ["hd", "fullhd", "4k"]
        self.languages = ["en", "es"]

    def test_build_visual_novel(self):

        with MonkeyPatch().context() as m:
            m.setattr(subprocess, "run", lambda *args, **kwargs: None)
            m.setattr(os, "makedirs", lambda *args, **kwargs: None)
            m.setattr(config, "resolution", "hd")

            # assert it doesn't raise an error and return None
            self.assertEqual(
                build_visual_novel(
                    self.source_dir,
                    self.output_dir,
                    self.platforms,
                    self.resolutions,
                    self.languages,
                ),
                None,
            )
