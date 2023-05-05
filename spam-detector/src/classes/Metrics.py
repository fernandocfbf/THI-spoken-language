import random
random.seed(42) 

class Metrics():

    def train_test_split(self, df):
        rows = df.index.tolist()
        random.shuffle(rows)
        df = df.iloc[rows]
        train_proportion = 0.8
        train_size = int(train_proportion * len(df))
        train_df = df[:train_size]
        test_df = df[train_size:]
        return train_df, test_df
    
    def accuracy(self, y_pred, y_true):
        hits = 0
        total = len(y_pred)
        for index in range(len(y_pred)):
            prediciton = y_pred[index]
            true = y_true[index]
            if prediciton == true:
                hits += 1
        return hits/total
    
    def confusion_matrix(self, y_true, y_pred):
        tp = fp = tn = fn = 0
        for pred, true in zip(y_pred, y_true):
            if pred == "spam" and true == "spam":
                tp += 1
            elif pred == "spam" and true == "ham":
                fp += 1
            elif pred == "ham" and true == "ham":
                tn += 1
            elif pred == "ham" and true == "spam":
                fn += 1
        return (tp, fp, tn, fn)


    def f1_score(self, y_true, y_pred):
        tp, fp, tn, fn = self.confusion_matrix(y_true, y_pred)
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2 * (precision * recall) / (precision + recall)
        return f1


    def recall(self, y_true, y_pred):
        tp, fp, tn, fn = self.confusion_matrix(y_true, y_pred)
        recall = tp / (tp + fn)
        return recall
