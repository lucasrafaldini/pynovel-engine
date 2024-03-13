import json
import os
import sys
from datetime import datetime

from errors.saveandload import CantSaveGame, NoGameSaved


class SaveAndLoadManager:

    def save_game(state: str, save_directory="saved_games") -> None:
        # Lets create the folder inside the dist folder
        # so the user can save the game in the same folder as the executable
        # and the game will be able to find the saved games
        save_directory = os.path.join(os.path.dirname(sys.executable), save_directory)

        # Create the save directory if it doesn't exist
        os.makedirs(save_directory, exist_ok=True)

        # Create a save file with state and datetime
        filename = f'save_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json'
        filepath = os.path.join(save_directory, filename)
        try:
            with open(filepath, "w") as save_file:
                save_dict = {
                    "state": state,
                    # I could store the language just for troubleshooting reasons
                    # because saving and loading the language unable the user to load their saved game
                    # with the game started in another language and it limits the user experience
                    # 'language': config.selected_language,
                }
                json.dump(save_dict, save_file)
        except CantSaveGame as exc:
            print(exc)
            raise CantSaveGame

    def load_game(save_directory="saved_games") -> str:
        save_directory = os.path.join(os.path.dirname(sys.executable), save_directory)
        if not os.path.exists(save_directory):
            print("Save directory does not exist.")
            raise NoGameSaved

        # Get the list of save files
        save_files = [
            f
            for f in os.listdir(save_directory)
            if f.startswith("save_") and f.endswith(".json")
        ]
        if not save_files:
            print("No saved games to load.")
            raise NoGameSaved

        # Reading the content of the save files makes this load function
        # grow in processing time (O(n)) so we will get the latest save based
        # on the last modification time of the file
        latest_save_file = max(
            save_files, key=lambda f: os.path.getmtime(os.path.join(save_directory, f))
        )
        latest_save_path = os.path.join(save_directory, latest_save_file)

        with open(latest_save_path, "r") as save_file:
            save_dict = json.load(save_file)
            return save_dict["state"]
