import argparse
import os
import subprocess

from configs import config


def build_visual_novel(source_dir, output_dir, platforms, resolutions, languages):
    """
    Build a visual novel for the specified platforms, resolutions, and languages.

    Args:
        source_dir (str): The directory containing the source files of the visual novel.
        output_dir (str): The directory where the built files will be saved.
        platforms (list): A list of platforms to build for (e.g., ['linux', 'windows']).
        resolutions (list): A list of resolutions to build for (e.g., ['hd', 'fullhd', '4k']).
        languages (list): A list of languages to include in the built visual novel.

    Returns:
        None
    """
    print(f"Building for platforms: {platforms}")
    print(f"With resolutions: {resolutions}")
    print(f"And languages: {languages}")

    # Make sure the story is cohesive
    # before building
    try:
        subprocess.run(["python", "main.py", "--check-cohesion"], check=True)
    except subprocess.CalledProcessError:
        print("Story is not cohesive. Aborting build.")
        return

    # Run tests before building
    try:
        subprocess.run(["python", "-m", "pytest", "tests"], check=True)
    except subprocess.CalledProcessError:
        print("Tests didn't passed. Aborting build.")
        return

    # Make sure the code is formatted before building
    # Run isort before anything else
    subprocess.run(["isort", "."], check=True)
    # Run black then
    subprocess.run(["black", "."], check=True)

    for platform in platforms:
        for resolution in resolutions:
            config.resolution = (
                resolution if resolution in config.available_resolutions else "hd"
            )
            dist_path = os.path.join(
                output_dir, f"dist_{platform.lower()}_{resolution.lower()}"
            )
            work_path = os.path.join(
                output_dir, f"build_{platform.lower()}_{resolution.lower()}"
            )
            os.makedirs(dist_path, exist_ok=True)
            os.makedirs(work_path, exist_ok=True)
            match platform.lower():
                case "linux":
                    # Linux build command
                    pyinstaller_args = [
                        "pyinstaller",
                        "--name=%s" % f"{config.caption}_Linux",
                        "--onefile",
                        "--windowed",
                        "--distpath=%s" % dist_path,
                        "--workpath=%s" % work_path,
                        source_dir,
                    ]
                    subprocess.run(pyinstaller_args, check=True)
                case "windows":
                    # Windows build command using Wine
                    pyinstaller_args = [
                        "wine",
                        "pyinstaller",
                        "--name=%s" % f"{config.caption}_Windows",
                        "--onefile",
                        "--windowed",
                        "--distpath=%s" % dist_path,
                        "--workpath=%s" % work_path,
                        source_dir,
                    ]
                    subprocess.run(pyinstaller_args, check=True)
                case _:
                    print(
                        f"Platform {platform} is not supported for direct building from this script."
                    )


def main():
    parser = argparse.ArgumentParser(description="Your Visual Novel Game Engine CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    build_parser = subparsers.add_parser("build", help="Build the visual novel project")
    build_parser.add_argument(
        "--platforms",
        help="Comma-separated list of platforms (windows,linux)",
        required=True,
    )
    build_parser.add_argument(
        "--resolutions",
        help="Comma-separated list of resolutions (hd,fullhd,4k)",
        required=True,
    )
    build_parser.add_argument(
        "--languages", help="Comma-separated list of languages (en,pt)", required=True
    )
    build_parser.add_argument(
        "source_dir", help="Source directory of your visual novel"
    )
    build_parser.add_argument("output_dir", help="Output directory for the project")

    args = parser.parse_args()

    try:
        languages = [
            config.available_languages[lang] for lang in args.languages.split(",")
        ]
        config.languages = languages
    except KeyError:
        print(
            f"Invalid language code. Available languages: {', '.join(config.available_languages.keys())}"
        )
        return

    if args.command == "build":
        platforms = args.platforms.split(",")
        resolutions = args.resolutions.split(",")
        build_visual_novel(
            args.source_dir, args.output_dir, platforms, resolutions, languages
        )
    else:
        print("Use --help to see available commands")


if __name__ == "__main__":
    main()
