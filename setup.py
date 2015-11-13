from setuptools import setup
import codecs


with codecs.open('README.rst', 'r', 'utf-8') as readme:
    long_description = readme.read()


setup(
    name='nvimex',
    packages=['nvimex'],
    version='0.1',
    description='Run neovim commands from your shell.',
    long_description=long_description,
    license='MIT',
    author='Andreas Karlsson',
    author_email='andreas.karlsson87+pip-nvimex@gmail.com',
    url='https://github.com/akarl818/nvimex',
    keywords=['neovim'],
    install_requires=[
        'neovim==0.0.38',
        'docopt==0.6.2'
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
    ],
    entry_points={
        'console_scripts': ['nvimex = nvimex.nvimex:main']
    }
)
