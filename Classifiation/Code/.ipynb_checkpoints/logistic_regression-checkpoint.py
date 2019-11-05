#quick model fit
import numpy as np
import warnings
import pandas
warnings.filterwarnings("ignore")#not recomended but i have included this for my own convenience.
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = pandas.DataFrame(data = data.data,columns=data.feature_names)
y = data.target
#train test split
from sklearn import model_selection
np.random.seed(2) #to enable you replicate the same thing i am doing here.
X_train, X_test, y_train, y_test = model_selection.train_test_split(X,y,test_size=0.30)
# I will use logistic reg
from sklearn.linear_model import LogisticRegression
reg = LogisticRegression()
reg.fit(X_train,y_train)
preds = reg.predict(X_test)
predsprob = reg.predict_proba(X_test)

#Confusion matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,preds,labels=[1,0]))
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(confusion_matrix(y_test,preds),annot=True,lw =2,cbar=False)
plt.ylabel("True Values")
plt.xlabel("Predicted Values")
plt.title("CONFUSSION MATRIX VISUALIZATION")
plt.show()