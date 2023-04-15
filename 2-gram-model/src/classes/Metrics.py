class Metrics():
    def __init__(self, y_pred, y_true):
        self.y_pred = y_pred
        self.y_true = y_true
    
    def accuracy(self):
        hits = 0
        total = len(self.y_pred)
        for index in range(len(self.y_pred)):
            prediciton = self.y_pred[index]
            true = self.y_true[index]
            if prediciton == true:
                hits += 1
        return hits/total