"""Pytest configuration and fixtures"""
import pytest
from pathlib import Path


@pytest.fixture
def project_root():
    """Path to project root directory"""
    return Path(__file__).parent.parent
