from setuptools import setup, find_packages

setup(
    name="arcade-ytx",
    version="0.3",
    packages=find_packages(),
    description="😎 Bring back retro arcade vibes with this Python game pack! All addictive gameplay built with love(and the rich library).",
    author={"name": "Aryan Kalra", "email": "aryan.kalra363@gmail.com"},
    url="https://github.com/A-ryan-Kalra/arcade-ytx/tree/feat/all-game",
    dependencies=[
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "Pygments==2.19.2",
        "rich==14.0.0",
    ],
    entry_points={
        "console_scripts": ["arcade-ytx=arcade_ytx.main:run_game"],
    },
)
