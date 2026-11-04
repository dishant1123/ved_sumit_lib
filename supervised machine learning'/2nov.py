import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score,classification_report,roc_curve,roc_auc_score
from sklearn.svm import SVC 
import seaborn as sns
import matplotlib.pyplot as plt

# read csv : 

df= pd.read_csv("supervised machine learning'/Social_Network_Ads.csv")
print(df.head())

# missing values :
print(df.isnull().sum())

#gender  : 
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# feature selection : 
X=df[['Age','EstimatedSalary','Gender']]
y=df['Purchased']

# split data :
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42)

# scale data :
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

# model : 
model =SVC(
    kernel='linear',
    random_state=42
)

# fit model :
model.fit(X_train_scaled,y_train) 

# predict :
y_predict = model.predict(X_test_scaled)
print("Predicted Values : ",y_predict)

# accuracy score :
accuracy = accuracy_score(y_test,y_predict)
print("Model Accuracy : ",accuracy)

# classification report :
classification_rep = classification_report(y_test,y_predict)
print("Classification Report : \n",classification_rep)

#confusion matrix using  seaborn  ----> sns.heatmap 

confusion_matrix = pd.crosstab(y_test,
                               y_predict,
                               rownames=['Actual'],
                               colnames=['Predicted'])
print("Confusion Matrix : \n",confusion_matrix)

confusion_matrix_plot = sns.heatmap(confusion_matrix,
                                    annot=True,
                                    fmt='d',
                                    cmap='Blues')
plt.show()

# apply below  code  when  you use the logistic regression  : 
"""
# roc curve :
curve =roc_curve(y_predict,y_test) 
print(curve)

plt.plot()

# Probability of positive class
y_prob = model.predict_proba(X_test)[:, 1]

# ROC values
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# AUC Score
auc_score = roc_auc_score(y_test, y_prob)

# Plot ROC Curve
plt.figure(figsize=(6,4)) 
plt.plot(fpr,tpr,label =f"AUC = {auc_score:.3f}",
         color='blue')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid(True)

plt.show()"""


"""
confusion  matrix :

actual 0  predicted 0   -----> True Negative (TN)
actual 1  predicted 1   -----> True positive (TP)

actual 0  predicted 1   -----> False positive (FP)
actual 1  predicted 0   -----> False negative (FN)
"""

# new dataset predict :
new_data = pd.DataFrame({
    'Age':[39,49,29],
    'EstimatedSalary':[39000, 49000,29000],
    'Gender':[0,0,0]
})

# scale new data :
new_data_scaled = scaler.transform(new_data)

# predict new data :
new_prediction = model.predict(new_data_scaled)
print("New Data Prediction : ",new_prediction)


# over fiting check  : train score and test score