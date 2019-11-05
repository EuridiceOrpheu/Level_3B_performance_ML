# Example of calculating classification sensivity
# True positive rate


def sensivity(actual, predicted):
    TP = 0
    FN = 0
    for i in range(len(actual)):
        if (actual[i]):
            if actual[i] == predicted[i]:
                TP += 1
            else:
                FN += 1
    return TP / float(TP+FN)

# Test accuracy
actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,0,0,0,1,0,1,1,1]
accuracy = sensivity(actual, predicted)
print(accuracy)
from sklearn import metrics
print(metrics.recall_score(actual, predicted))
