from setuptools import setup, find_packages

setup(
    name="pyappms",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gitpython",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "pyappms=pyappms.cli:main",  # cli.py içindeki main fonksiyonunu çalıştırır
        ],
    },
    python_requires='>=3.7',
)
