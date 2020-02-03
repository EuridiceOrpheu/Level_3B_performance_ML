#TN/(TN+FP)
0==0 / 0==1
def specifity(actual, predicted):
    TN = 0
    FN = 0
    for i in range(len(actual)):
        if (actual[i]!=1):
            if actual[i] == predicted[i]:
                TN += 1
            else:
                FP += 1
    return TN / float(TN+FP)


actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,0,0,0,1,0,1,1,1]
specifity = specifity(actual, predicted)
print(specifity)