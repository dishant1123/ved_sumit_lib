# K-MEANS CLUSTERING - CUSTOMER SEGMENTATION
import  pandas as pd 
import numpy as np  
import  matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 

"""
Step 1: Load dataset : using mall csv 
Step 2: Select features
Step 3: Feature scaling
Step 4: Elbow Method
Step 5: Display Elbow graph
Step 6: Apply K-Means
Step 7: predict
Step 8: Display cluster labels
Step 9: Display centroids : using scaler.inverse_transform()
Step 10: Calculate WCSS
Step 11: Visualize clusters
Step 12: Cluster analysis
Step 13: Count customers in each cluster
"""
# note : 
"""
n_init : n_init specifies how many times K-Means will run with different initial centroid selections.
K-Means can produce different clusters depending on where the initial centroids are placed.
To get a better clustering result, we run the algorithm multiple times and select the result with the lowest WCSS (inertia).
"""
# read csv : 

df=pd.read_csv("unsupervised/Mall_Customers (1).csv") 

# select features :
X=df[['Annual Income (k$)','Spending Score (1-100)']] 

# feature scaling :
scaler=StandardScaler()
X=scaler.fit_transform(X)

# Elbow Method :
wcss=[] 

for i in range(1,11):
    kmeans=KMeans(n_clusters=i,
                  init='k-means++', #
                  random_state=42,
                  n_init=10 # how many time  kmeans will run with  different  starting centroid
                  )
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),
         wcss,
         marker='o')
plt.show()  

# model  : 

model =KMeans(
    n_clusters=5,
    init='k-means++',
    random_state=42,
    n_init=10
)  

df['Cluster'] =model.fit_predict(X) 

# display centroid  : 

centroid =scaler.inverse_transform(model.cluster_centers_) 
print("centroid : ",centroid)

# calculate  wcss : 
print("WCSS : ",model.inertia_)

# visualize :
plt.scatter(
    X[:,0],  # row , col 
    X[:,1],
    marker='o',
    cmap="coolwarm",
    c=df['Cluster'],
    s=100
)
plt.scatter(
    model.cluster_centers_[:,0],
    model.cluster_centers_[:,1],
    marker='X',
    s=300,
)
plt.title("KMeans Clustering (Centroid)")
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()
"""
total  : 5 cluster hint  : group , sort_value , count_values()

cluster     0   total customer  to  included in 0  ----> 20 
cluster     1 
clustrer    2 
cluster     3 
cluster     4

"""
