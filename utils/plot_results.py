import matplotlib.pyplot as plt

def plot_flag_accuracy(acc_list, flags):
    plt.barh(flags, acc_list)
    plt.xlabel("Accuracy")
    plt.title("Per-Flag Accuracy")
    plt.tight_layout()
    plt.savefig("flag_selector_results.png")
    plt.show()