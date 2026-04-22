from data.dataset import generate_dataset, FLAGS
from features.feature_engineering import create_features
from models.train_model import train
from evaluation.evaluate import evaluate
from utils.metrics import per_flag_accuracy

def main():
    df = generate_dataset()

    X, Y, feature_cols = create_features(df)

    model, scaler, X_test, Y_test = train(X, Y)

    Y_pred = model.predict(X_test)

    evaluate(Y_test, Y_pred)
    per_flag_accuracy(Y_test, Y_pred, FLAGS)

if __name__ == "__main__":
    main()