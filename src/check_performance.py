import sys

threshold = 0.95  #Intentionally setting a higher accuracy rate than the model's actual accuracy rate
with open("artifacts/accuracy.txt", "r") as f:
    accuracy = float(f.read().strip())

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
