"""
Setup script for Music RAG AI
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="music-rag-ai",
    version="1.0.0",
    author="Music RAG AI Team",
    author_email="contact@music-rag-ai.com",
    description="AI-powered music recommendation system using RAG with cultural intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/psr0049/music-rag-ai",
    project_urls={
        "Bug Tracker": "https://github.com/psr0049/music-rag-ai/issues",
        "Documentation": "https://github.com/psr0049/music-rag-ai#readme",
        "Source Code": "https://github.com/psr0049/music-rag-ai",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "music-rag-ai=src.apps.streamlit_app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)