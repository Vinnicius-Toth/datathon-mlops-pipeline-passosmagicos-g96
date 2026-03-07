from sklearn.metrics import (
    classification_report,
    recall_score,
    roc_auc_score,
    confusion_matrix
)


def evaluate_model(y_test, y_pred, y_prob):

    metrics = {
        "recall_class_1": recall_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_prob),
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
    }

    print("\n=== Classification Report ===\n")
    print(classification_report(y_test, y_pred))

    print("\n=== Metrics ===")
    print(metrics)

    return metrics