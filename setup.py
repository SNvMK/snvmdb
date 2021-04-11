import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="snvmdb",
    version="1.1.0",
    author="SNVMK",
    author_email="sidzahroman@gmail.com",
    description="Simple database tool",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snvmk/snvmdb",
    project_urls={
        "Bug Tracker": "https://github.com/snvmk/snvmdb/issues",
        "Documentation": "https://github.com/SNvMK/snvmdb/wiki",
        "Discussions": "https://github.com/SNvMK/snvmdb/discussions"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.5",
    extras_require={
        'speedup': ['ujson']
    }
)
