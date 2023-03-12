import setuptools

setuptools.setup(
    name="enigma_hiratsuca_maluli",
    version="0.0.1",
    authors="Hiratsuca, Maluli",
    description="A package to encrypt and decrypt messages using the Enigma Machine and Linear Algebra",
    url="https://github.com/LuccaHiratsuca/Enigma",
    packages=['enigma_hiratsuca_maluli'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['numpy']
)