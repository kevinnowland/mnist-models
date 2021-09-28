from setuptools import setup

# make the README into the long description
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mnist_models",
    version="0.0.1",
    description="play with models and mnist data",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/kevinnowland/mnist-models",
    author="Kevin Nowland",
    license="MIT",
    packages=["mnist_models"],
    package_dir={"mnist_models": "mnist_models"},
    package_data={"mnist_models": ["pretrained_models/*pkl"]},
    install_requires=[
        'mnist>=0.2.2',
        'numpy>=1.21',
        'scikit-learn>=0.24',
    ],
    zip_safe=False
)
