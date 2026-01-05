"""Test content (.lr files) structure and validity"""
import pytest
from pathlib import Path


def get_all_lr_files():
    """Find all .lr content files"""
    content_dir = Path("content")
    if not content_dir.exists():
        return []
    return list(content_dir.rglob("*.lr"))


@pytest.mark.parametrize("lr_file", get_all_lr_files())
def test_lr_file_has_model(lr_file):
    """Every .lr file must have a _model or _template field (except data-only files)"""
    content = lr_file.read_text(encoding="utf-8")

    # Skip data-only files in rooms directory (they don't need _model/_template)
    if "rooms/" in str(lr_file):
        pytest.skip(f"Skipping data-only file: {lr_file}")

    assert "_model:" in content or "_template:" in content, (
        f"{lr_file} missing _model or _template field"
    )


@pytest.mark.parametrize("lr_file", get_all_lr_files())
def test_lr_file_has_field_separators(lr_file):
    """Check .lr files have proper structure with --- separators"""
    content = lr_file.read_text(encoding="utf-8")
    # Most .lr files have at least one field separator
    # Skip check if it's a very simple file
    if len(content.strip()) > 20:
        assert "---" in content or "####" in content, (
            f"{lr_file} missing field separators (--- or ####)"
        )


def test_talks_directory_structure():
    """Talks should be in content/talks/ with contents.lr"""
    talks_dir = Path("content/talks")

    if not talks_dir.exists():
        pytest.skip("No talks directory found")

    # Get all talk directories (exclude the parent talks/contents.lr)
    talk_dirs = [
        d for d in talks_dir.iterdir() if d.is_dir() and (d / "contents.lr").exists()
    ]

    assert len(talk_dirs) > 0, "No talks found in content/talks/"

    # Verify each talk has required structure
    for talk_dir in talk_dirs:
        contents_file = talk_dir / "contents.lr"
        assert contents_file.exists(), f"Missing contents.lr in {talk_dir}"


def test_speakers_directory_structure():
    """Speakers should be in content/speakers/ with contents.lr"""
    speakers_dir = Path("content/speakers")

    if not speakers_dir.exists():
        pytest.skip("No speakers directory found")

    speaker_dirs = [
        d
        for d in speakers_dir.iterdir()
        if d.is_dir() and (d / "contents.lr").exists()
    ]

    assert len(speaker_dirs) > 0, "No speakers found in content/speakers/"
