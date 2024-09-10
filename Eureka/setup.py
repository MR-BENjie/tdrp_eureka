from setuptools import setup, find_packages

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    "charset-normalizer",

    "openai",

    'ray>=1.1.0',
    'tensorboard>=1.14.0',
    'tensorboardX>=1.6',
    'setproctitle',
    'psutil',
    'pyyaml',


    "termcolor",
    "hydra-core>=1.1",
    "pyvirtualdisplay",
]

# Installation operation
setup(
    name="eureka",
    author="Jason Ma",
    version="1.0",
    description="Eureka",
    keywords=["llm", "rl"],
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=INSTALL_REQUIRES,
    packages=find_packages("."),
)

