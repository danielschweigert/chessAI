from setuptools import setup, find_packages
import os


with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    requires = f.read().strip().split('\n')

setup(
    name="chessAI",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requires,
    package_data={},

    authors=["Daniel Schweigert"],
    description="ML approaches for chess",
    url="",

    entry_points={
        "console_scripts": [
            "chess = chessAI.main:main"
        ]
    }
)
