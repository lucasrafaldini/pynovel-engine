# Your Visual Novel Engine

Your Visual Novel Engine is a Python-powered game engine designed to create interactive visual novels with ease. Utilizing the robust libraries of Python and Pygame, this engine provides a platform for creators to bring their stories to life with intricate narratives and complex branching storylines.

## Features

- **Dynamic Storytelling**: Facilitate the creation of stories with multiple paths and endings influenced by user choices.
- **Character Interaction**: Develop characters and dialogues that dynamically respond to player actions.
- **Save and Resume**: Allow players to save their progress and return to their adventure at any point.
- **Multilingual Support**: Craft stories in one language and expand to a bouquet of languages with a built-in translation toolkit.
- **Simplified Deployment**: Package and distribute stories effortlessly with a built-in build system for desktop and mobile platforms.

## Installation

To install the Visual Novel Engine, you can use the following command:

```bash
pip install visual_novel_engine
pip install visual_novel_engine_cli
```

## Usage
Running the Engine

To start the visual novel engine, use the following command:

```bash

visual_novel_engine_cli
```

## Building a Visual Novel

To build your visual novel project into an executable, navigate to your project directory and run:

```bash

visual_novel_engine_cli --build ./main.py .
```
    ./main.py is the path to the Python script that serves as the entry point for your visual novel.
    The second argument . is the directory where the built executable will be placed. You can replace this with any output directory you prefer.

## Additional Commands

To get help on the CLI usage, run:

```bash

visual_novel_engine_cli --help
```


## Development

If you wish to contribute or customize the engine, clone the repository and install the package in editable mode:

```bash

git clone https://github.com/lucasrafaldini/visual_novel_engine.git
cd visual_novel_engine
pip install -e .
```

