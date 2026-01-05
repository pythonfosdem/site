"""Test that Lektor builds successfully"""

import subprocess


def test_lektor_build_succeeds(tmp_path):
    """Ensure the site builds without errors"""
    output_dir = tmp_path / "build-output"

    result = subprocess.run(
        [".venv/bin/lektor", "build", "--output-path", str(output_dir)],
        capture_output=True,
        text=True,
        timeout=60,
    )

    assert result.returncode == 0, (
        f"Lektor build failed with exit code {result.returncode}\n"
        f"STDOUT: {result.stdout}\n"
        f"STDERR: {result.stderr}"
    )

    # Verify output directory was created
    assert output_dir.exists(), "Build output directory not created"

    # Verify index.html was generated
    index_file = output_dir / "index.html"
    assert index_file.exists(), "index.html not generated"


def test_build_output_contains_expected_files(tmp_path):
    """Verify key files are in build output"""
    output_dir = tmp_path / "build-output"

    subprocess.run(
        [".venv/bin/lektor", "build", "--output-path", str(output_dir)],
        capture_output=True,
        timeout=60,
    )

    # Check for key pages
    expected_files = [
        "index.html",
        "talks/index.html",
        "speakers/index.html",
        "call-for-proposals/index.html",
        "code-of-conduct/index.html",
    ]

    for file_path in expected_files:
        full_path = output_dir / file_path
        assert full_path.exists(), f"Expected file not found: {file_path}"
