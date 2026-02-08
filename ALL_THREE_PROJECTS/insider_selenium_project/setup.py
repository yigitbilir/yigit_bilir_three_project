from setuptools import setup, find_packages

setup(
    name="insider-selenium-tests",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'selenium==4.27.1',
        'pytest==8.3.4',
        'pytest-html==4.1.1',
        'webdriver-manager==4.0.2',
        'Pillow==11.0.0',
    ],
    python_requires='>=3.10',
)
