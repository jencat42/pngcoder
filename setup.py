import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    license='MIT',
    name="pngcoder",
    version="1.2",
    author="JenCat",
    author_email="jencat@ex.ua",
    description="Encode (obfuscate) any file to PNG or WAV and vise versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jencat42/pngcoder",
    packages=["src"],
    keywords='obfuscate obfuscator encode encoder png wav binary',
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'pngcoder=src.pngcoder:main',
            'wavcoder=src.wavcoder:main'
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Any',
        'Topic :: Obfuscator :: Encoder',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)