try:
    from sklearn.metrics import (
        # _regression:
        mean_squared_error,
        # _ranking:
        roc_auc_score,
        # _classification:
        accuracy_score,
        f1_score,
        precision_score,
        recall_score,
        log_loss,
    )
except ImportError:
    print("sklearn not available")
