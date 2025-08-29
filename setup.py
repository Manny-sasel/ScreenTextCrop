"""
Setup script for Live Screen Text Extractor
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="live-screen-text-extractor",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Extract text from any part of your screen using OCR with a floating control panel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/live-screen-text-extractor",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
        "Topic :: Text Processing :: General",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.10',
            'black>=21.0',
            'flake8>=3.8',
        ],
        'enhanced': [
            'scikit-image>=0.18.0',
            'matplotlib>=3.3.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'screen-text-extractor=screen_text_extractor:main',
        ],
    },
    keywords="ocr text-extraction screen-capture tesseract gui desktop-application",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/live-screen-text-extractor/issues",
        "Source": "https://github.com/yourusername/live-screen-text-extractor",
        "Documentation": "https://github.com/yourusername/live-screen-text-extractor/blob/main/README.md",
    },
)