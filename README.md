# PyNovel Engine

PyNovel Engine is a Python-powered game engine designed to create interactive visual novels with ease. Utilizing the robust libraries of Python and Pygame, this engine provides a platform for creators to bring their stories to life with intricate narratives and complex branching storylines.

## Features

- **Dynamic Storytelling**: Facilitate the creation of stories with multiple paths and endings influenced by user choices.
- **Character Interaction**: Develop characters and dialogues that dynamically respond to player actions.
- **Save and Resume**: Allow players to save their progress and return to their adventure at any point.
- **Multilingual Support**: Craft stories in one language and expand to a bouquet of languages with a built-in translation toolkit.
- **Simplified Deployment**: Package and distribute stories effortlessly with a built-in build system for desktop and mobile platforms.

## Installation

To install the PyNovel Engine, you can use the following command:

```bash
pip install pynovel_engine
pip install pynovel_engine_cli
```

## Usage
Running the Engine

To start the visual novel engine, use the following command:

```bash

pynovel_engine_cli
```

## Building a Visual Novel

To build your visual novel project into an executable, navigate to your project directory and run:

```bash
pynovel_engine_cli build --platforms=windows,linux --resolutions=hd,fullhd,4k --languages=en,pt,fr,es,de ./main.py .
```
- build: Command to build the visual novel project.
- --platforms: The platforms for which the visual novel will be built. You can specify multiple platforms separated by commas. The available platforms are windows and linux.
-  --resolutions: The resolutions for which the visual novel will be built. You can specify multiple resolutions separated by commas. The available resolutions are hd, fullhd, and 4k.
-  --languages: The languages in which the visual novel will be built. You can specify multiple languages separated by commas. The available languages are en, pt, fr, es, and de, but you can add more languages at the config file.
- ./main.py: The entry point of the visual novel project.
- .: The directory where you want to save the built visual novel.

## Additional Commands

To get help on the CLI usage, run:

```bash
pynovel_engine_cli --help
```


## Development

If you wish to contribute or customize the engine, clone the repository and install the package in editable mode:

```bash
git clone https://github.com/lucasrafaldini/pynovel_engine.git
cd pynovel_engine
pip install -r requirements.txt
pip install -e .
```

## Testing

If you want to test if your story is cohesive and has no errors, define your history in main.py and use the following command:

```bash
pynovel_engine --check-cohesion
```

There are unit tests for each of the components of the game, but you need to take some cautions.
Because of incompatibilities between the googletrans library and the latest httpx library, the tests raise some warnings (but those are expected).

We can't update the httpx lib to remove those warning because the googletrans library is not compatible with the latest version of httpx.

To run the tests, you can use the following command:

```bash
python3 -m pytest tests --disable-warnings
```

## Expected errors

For errors/warnings on tests, please read the Testing section.

Some build/execution errors are expected in some cases, such as:

```bash
httpcore._exceptions.ConnectTimeout: _ssl.c:989: The handshake operation timed out
```

This error occurs when the engine is translating its text. All translation operations have retries programmed, but in some cases, the connection may be too slow or unstable. In this case, the engine will continue to try to connect until it succeeds. If the error persists, it is recommended to check the internet connection and try again.

## Future Enhancements

- [ ] **Add validation for Story to have only one start scene**: Add validation to ensure that the story has just one start scene, preventing creators from creating visual novels with multiple starting points.
- [ ] **Customizable Text Speed**: Allow players to adjust the speed at which text is displayed on the screen, catering to different reading speeds and preferences.
- [ ] **Change Tooltip Text on Game Icon (currently "Python")**: Change the tooltip text that appears when hovering over the game icon in the taskbar to reflect the name of the visual novel being played.
- [ ] **Add custom loggers (replace prints)**: Add custom loggers to the engine to allow creators to log custom messages and errors.
- [ ] **Encode The Save File**: Encrypt the save file to prevent players from modifying it and cheating the game.
- [ ] **Troubleshooting Mode**: Implement a troubleshooting mode that provides detailed error messages and logs to help creators identify and fix issues in their visual novels.
- [ ] **Translate Popup Texts**: Add support for translating popup texts, such as tooltips and context menus, to make the visual novel accessible to a wider audience.
- [ ] **Load Game Menu**: Implement a menu that allows players to load multiple previously saved game states.
- [ ] **Multiple Game Load**: Enhance the engine to support saving and loading multiple game states, allowing players to have multiple save slots and switch between them.
- [ ] **Customizable UI**: Provide a way for creators to customize the visual novel's user interface, including the ability to add custom backgrounds, buttons, and other UI elements.
- [ ] **Audio Support**: Integrate audio playback capabilities to add background music and sound effects to the visual novel.
- [ ] **Mobile Deployment**: Extend the build system to support packaging visual novels for mobile platforms, such as Android and iOS.

