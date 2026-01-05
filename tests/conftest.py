"""Pytest configuration and fixtures"""

from pathlib import Path

import pytest


@pytest.fixture
def project_root():
    """Path to project root directory"""
    return Path(__file__).parent.parent
