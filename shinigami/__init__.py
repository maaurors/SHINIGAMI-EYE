"""
SHINIGAMI-EYE (神死眼)
All-Seeing Cybersecurity Framework

A next-generation offensive security framework for network reconnaissance,
vulnerability assessment, and security intelligence gathering.

Author: Created with Antigravity AI
Version: 1.0.0
License: Educational Use Only
"""

__version__ = "1.0.0"
__author__ = "SHINIGAMI-EYE Team"
__license__ = "Educational Use Only"

from shinigami.utils import logger, ascii_art
from shinigami import modules

__all__ = [
    'logger',
    'ascii_art',
    'modules'
]
