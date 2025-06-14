import subprocess
import sys


def test_train_and_save_model():
    result = subprocess.run(
        [sys.executable, "src/train.py"],
        capture_output=True
    )
    assert result.returncode == 0, (
        f"Training script failed: {result.stderr.decode()}"
    )


def test_evaluate_and_accuracy():
    result = subprocess.run(
        [sys.executable, "src/evaluate.py"],
        capture_output=True
    )
    assert result.returncode == 0, (
        f"Evaluation script failed: {result.stderr.decode()}"
    )
