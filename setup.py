"""
SHINIGAMI-EYE Setup Script
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

setup(
    name="shinigami-eye",
    version="2.0.0",
    author="Mauro",
    author_email="maauro.rs@gmail.com",
    description="All-Seeing Cybersecurity Framework for Network Reconnaissance and Security Intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maaurors/SHINIGAMI-EYE",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "dnspython>=2.4.2",
        "pyOpenSSL>=23.3.0",
        "jinja2>=3.1.2",
    ],
    entry_points={
        "console_scripts": [
            "shinigami-eye=shinigami.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
