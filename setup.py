from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mprc-fft",
    version="1.0.0",
    author="Muhammad Arshad",
    author_email="arshad@quantum.research",
    description="MPRC Spectral Transform: A Signal-Adapted Geometric Projection on Z₂₅₆",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mprc-fft",
    project_urls={
        "Documentation": "https://github.com/yourusername/mprc-fft#readme",
        "Paper": "https://github.com/yourusername/mprc-fft/blob/main/docs/mprc_fft_paper.pdf",
        "Source Code": "https://github.com/yourusername/mprc-fft",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19.0",
    ],
    extras_require={
        "dev": ["pytest>=6.0", "numpy>=1.19.0"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: Creative Commons :: CC BY-NC 4.0 (Non-Commercial, Educational Use Only)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords=[
        "spectral-transform",
        "fft",
        "ring-geometry",
        "modular-arithmetic",
        "signal-processing",
        "mathematics",
        "quantum-computing",
    ],
    zip_safe=False,
)
