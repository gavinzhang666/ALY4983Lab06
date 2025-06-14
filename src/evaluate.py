import joblib
from sklearn.datasets import load_iris


def main():
    model = joblib.load("artifacts/model.pkl")
    X, y = load_iris(return_X_y=True)
    accuracy = model.score(X, y)
    print(f"Accuracy: {accuracy:.4f}")
    with open("artifacts/accuracy.txt", "w") as f:
        f.write(str(accuracy))


if __name__ == "__main__":
    main()
