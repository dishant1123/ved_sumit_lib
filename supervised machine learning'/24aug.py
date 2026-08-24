"""
ML -----> sklearn
1. read_csv,read_excel ------> pandas 
2. data  understanding  ------> info () ,describe(),describe(include='all')
3. data  cleaning  ----> missing value  ----> df.isnull().sum()
        fill value   ----> df.fillna(value) 
        drop   ----> df.drop(col_name,axis=1)
        outlier ----> box plot , ----> IQR ,Z-score  , ---> clipping 
4. feature engineering 
    ex : 
    id    name    age  salary   predict salary 
    1     john    25    90
    2     mary    27    90
    3     peter   23    78
    4     sam     29    67
    5     tom     25    90
    6     harry   22    88
5. data split -----> train test split  ----> 0.2  ----> testing 
6. model selection   -----> linear regression ,classification  
7. model fit   ----> 
8. model evaluation  ----> actual vs  predicted 
9.model prediction  ----> new data set 
10.deploy model  ----> streamlit ,docker,GIT-HUB
"""