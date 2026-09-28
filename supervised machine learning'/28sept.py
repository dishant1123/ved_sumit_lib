"""
classfication  : not spam vs spam ,  0 or  1 , male or female , survived or not survived
predict : category

ex : 

study_hrs    marks   result 
1             10      fail
2             34      fail
4             65      pass 
6             78      pass
8             90      pass

probability :
pass -----> 75%  -----> pass 
fail  -----> 25%  -----> fail  ------> 0 
0.5 >   ------> class 1 
< 0.5   ------> class 0 

limit/ decision boundary :

1. > 0.5   -----> class 1
2. < 0.5   -----> class 0

model : 

1. logistic regression
2. KNN : k nearest neighbor
3. SVM : support vector machine
4. decision tree
5. random forest
6. XGBoost

evaluation metrics :
1. accuracy
2. precision
3. recall
4. f1 score

confusion matrix :

email    actual     predict 
         spam         spam    ---->  TP  
         not spam     spam    ----> FP
         not spam     not spam   ---->TN   
         spam         not spam   ----->FN


true positive      false positive
true negative      false negative

classification report :
"""
