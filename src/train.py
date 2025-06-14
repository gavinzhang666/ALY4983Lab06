import os
import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

def main():
    X, y = load_iris(return_X_y=True)
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, "artifacts/model.pkl")

if __name__ == "__main__":
    main()
