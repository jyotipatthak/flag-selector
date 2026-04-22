def per_flag_accuracy(Y_test, Y_pred, flags):
    print("\nPer-Flag Accuracy:")
    for i, flag in enumerate(flags):
        acc = (Y_pred[:, i] == Y_test.iloc[:, i]).mean()
        print(f"{flag}: {acc:.3f}")