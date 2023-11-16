import os
from setuptools import setup


def read_me(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    name="Pyqt5-Leaflet",
    version="0.0.1",
    author="Francesco Gerratana",
    author_email="nextechnics@gmail.com",
    description="Use Pyqt5 and Leaflet to embed maps Openstreetmap",
    license="GPL v3",
    keywords="example documentation tutorial",
    url="https://gerfra.github.io/",
    long_description=read_me('README.md'),
    classifiers=[
        "Development Status :: 1",
        "Topic :: Utilities",
        "License :: GPL v3",
    ],
    install_requires=[
        'PyQt5 == 5.15.9',
        'PyQt5 - Qt5 == 5.15.2',
        'PyQt5 - sip == 12.12.1',
        'PyQtWebEngine == 5.15.6',
        'PyQtWebEngine - Qt5 == 5.15.2',
    ],
    python_requires='>=3.11'
)
