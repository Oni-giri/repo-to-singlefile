from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="repo-to-text",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gitpython>=3.1.0",
        "requests>=2.31.0",
        "typing-extensions>=4.5.0",
        "tiktoken>=0.5.1,<0.6.0",
    ],
    entry_points={
        'console_scripts': [
            'repo-to-text=repo_converter.cli:main',
        ],
    },
    author="Yakitori",
    author_email="mers_etanche.0n@icloud.com",
    description="A tool to convert code repositories into text format for LLM context",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Oni-giri/repo-to-text",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)