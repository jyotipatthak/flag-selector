from sklearn.metrics import hamming_loss, f1_score

def evaluate(Y_test, Y_pred):
    print("\nEvaluation Results:")
    print(f"Hamming Loss : {hamming_loss(Y_test, Y_pred):.4f}")
    print(f"F1 Score     : {f1_score(Y_test, Y_pred, average='micro'):.4f}")