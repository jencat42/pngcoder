import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pngcoder",
    version="1.0",
    author="JenCat",
    author_email="jencat@ex.ua",
    description="Encode (obfuscate) any file to PNG and vise versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jencat42/pngcoder",
    packages=["src"],
    classifiers=[
        "Obfuscation",
        "Encoder"
    ],
    python_requires='>=3.7',
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': ['pngcoder=src.pngcoder'],
    }
)