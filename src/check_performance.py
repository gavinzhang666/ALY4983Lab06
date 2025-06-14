import sys

threshold = 0.80
with open("artifacts/accuracy.txt", "r") as f:
    accuracy = float(f.read().strip())
if accuracy < threshold:
    sys.exit(f"ERROR: Model accuracy {accuracy:.2f} below threshold {threshold:.2f}")
else:
    print(f"Model accuracy {accuracy:.2f} meets threshold {threshold:.2f}")
