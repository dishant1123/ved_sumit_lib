"""

1. data set : salary 
2. feature selection 
3. train split 
4. feature scale  :fit_transform(),transform()
5. linear model 
6. ridge 
7. lasso 
8. elasticnet 

| Alpha | Effect                                        |
| ----- | --------------------------------------------- |
| 0     | No regularization (same as Linear Regression) |
| 0.001 | Very little regularization                    |
| 0.01  | Small regularization                          |
| 0.1   | Mild regularization                           |
| 1     | Default in most examples                      |
| 10    | Strong regularization                         |
| 100   | Very strong regularization                    |
| 1000  | May cause underfitting                        |

The alpha and l1_ratio values are hyperparameters, meaning there is no fixed value. They are usually chosen by cross-validation


| Model      | Recommended Value         |
| ---------- | ------------------------- |
| Ridge      | alpha=1                 	 |
| Lasso      | alpha=0.1 or alpha=1 	 |
| ElasticNet | alpha=1, l1_ratio=0.5 	 |

"""
