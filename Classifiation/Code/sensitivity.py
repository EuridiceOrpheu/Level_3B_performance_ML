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

# Test sensivity
actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,0,0,0,1,0,1,1,1]
sensivity = sensivity(actual, predicted)
print(sensivity)

