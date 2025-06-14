import sys

threshold = 0.999
with open("artifacts/accuracy.txt", "r") as f:
    accuracy = float(f.read().strip())

accuracy = 0.50


if accuracy < threshold:
    sys.exit(
        f"ERROR: Model accuracy {accuracy:.2f} below "
        f"threshold {threshold:.2f}"
    )
else:
    print(
        f"Model accuracy {accuracy:.2f} meets "
        f"threshold {threshold:.2f}"
    )
