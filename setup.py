import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roblox-api-wrapper",
    version="0.0.1",
    author="TerrificTable55",
    author_email="terrifictable@terrifictable.xyz",
    description="A Wrapper for the Roblox API", # Why am i doing this?
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TerrificTable/roblox_api_wrapper", # TODO
    project_urls={
        "Bug Tracker": "https://github.com/TerrificTable/roblox_api_wrapper/issues", # TODO
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={ "": "wrapper" },
    packages=setuptools.find_packages(where="wrapper"),
    python_requires=">=3.9",
)
