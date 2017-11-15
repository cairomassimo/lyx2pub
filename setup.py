from setuptools import setup

setup(
    name="lyx2pub",
    version="0.0.1",
    py_modules=["lyx2pub"],
    zip_safe=False,
    install_requires=[
        "docopt",
    ],
    entry_points={
        "console_scripts": [
            "lyx2pub=lyx2pub:main",
        ]
    }
)
