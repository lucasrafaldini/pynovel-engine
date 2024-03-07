from setuptools import find_packages, setup


def setup_pynovel_engine():
    """
    Set up the visual novel engine package.

    This function sets up the necessary information for packaging and distributing
    the visual novel engine package. It includes the package name, version, description,
    author information, package dependencies, and entry points for console scripts.

    Returns:
        None
    """
    setup(
        name="pynovel_engine",
        version="0.1",
        description="A visual novel engine",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        author="Lucas Rafaldini",
        author_email="lucas.rafaldini@gmail.com",
        packages=find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3.11",
            "Operating System :: OS Independent",
        ],
        install_requires=["pygame", "pyinstaller", "pytest"],
        entry_points={
            "console_scripts": [
                "pynovel_engine = main:main",
                "pynovel_engine_cli = cli:main",
            ]
        },
    )


setup_pynovel_engine()
