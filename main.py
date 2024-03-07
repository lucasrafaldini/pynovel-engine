import argparse
from engine import Story

"""
Here you can define the storyline of your game.
The Story class is a wrapper for the game engine and it allows you to define the scenes and choices of your game.

The Story class has the following methods:
    - add_scene: Adds a new scene to the game.
    - add_choice: Adds a new choice to a scene.
    - run: Starts the game.

The add_scene method has the following parameters:
    - scene_name (str): The name of the scene.
    - character_name (str): The name of the character that will be displayed in the scene.
    - description (str): The description of the scene.
    - image (str): The name of the image that will be displayed in the scene.

The add_choice method has the following parameters:
    - scene (str): The name of the scene where the choice will be added.
    - description (str): The description of the choice.
    - next_scene (str): The name of the scene that the choice leads to.

The run method has no parameters and it starts the game.

Example (with just one scene):
    story = Story()
    story.add_scene(scene_name="start", character_name="Doggo", description="You wake up in a mysterious room.", image="doggo.png")
    story.add_choice("start", "Go through the door", "door_scene")
    story.add_choice("start", "Look out the window", "door_scene")

"""


story = Story()

# Defina o início da história
story.add_scene(
    scene_name="start", description="You wake up in a mysterious room.", character_name="Doggo", image="doggo.png"
)
# Then, add choices
story.add_choice("start", "Go through the door", "door_scene")
story.add_choice("start", "Look out the window", "door_scene")

# Cena 2
story.add_scene(scene_name="door_scene", description="You find a hallway.", character_name="Doggo", image="doggo.png")
# Escolhas para a cena 2
story.add_choice("door_scene", "Go to the right", "window_scene")
story.add_choice("door_scene", "Go to the left", "start")

# Cena 3
story.add_scene(
    scene_name="window_scene", description="You see a garden below.", character_name="Doggo", image="doggo.png"
)
# Escolhas para a cena 3
story.add_choice("window_scene", "Get out of here", "end_scene")
story.add_choice("window_scene", "Go back", "door_scene")


if __name__ == "__main__":
    # If it has the parameter check_cohesion=True, it will check if the story is cohesive.
    # If it is not, it will raise a StoryCohesionError.
    argparser = argparse.ArgumentParser(description="PyNovel Game Engine CLI")
    argparser.add_argument("--check-cohesion", action="store_true", help="Check if the story is cohesive")
    args = argparser.parse_args()
    if args.check_cohesion:
        story.check_story()
    else:
        story.run()
