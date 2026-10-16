from sklearn.metrics import precision_score, recall_score, f1_score

# Sample held-out test data (1 = Scam, 0 = Safe)
# y_true: The actual true labels of your test messages
y_true = [1, 1, 1, 0, 0, 1, 0, 1, 0, 0] 

# y_pred: What your scam detection rule predicted (1 = Scam, 0 = Safe)
y_pred = [1, 1, 0, 0, 0, 1, 1, 1, 0, 0] 

# Calculate evaluation metrics
precision = precision_score(y_true, y_pred, zero_division=0)
recall = recall_score(y_true, y_pred, zero_division=0)
f1 = f1_score(y_true, y_pred, zero_division=0)

# Print the results nicely for your report
print("=== ScamShield-AI Evaluation Report ===")
print(f"Precision: {precision:.2f}")
print(f"Recall:    {recall:.2f}")
print(f"F1 Score:  {f1:.2f}")
