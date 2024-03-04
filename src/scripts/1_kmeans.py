# import libraries
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

from saveData import save_output_data

"""
K-MEANS algorithm: 
clusters data by trying to separate samples in n groups of equal variance, 
minimizing a criterion known as the inertia or within-cluster sum-of-squares

input: number of clusters

"""

# load dataset
#dataset = pd.read_excel('../../data/processed/subset_1.xlsx')
#dataset = pd.read_excel('../../data/processed/subset_2.xlsx')
dataset = pd.read_excel('../../data/processed/subset_3.xlsx')

# remove columns before the clustering
# test A
dataset.drop(columns=['ANNO'], inplace=True)

# test B
dataset.drop(columns=['ETA'], inplace=True)
dataset.drop(columns=['CDL'], inplace=True)
dataset.drop(columns=['GENERE'], inplace=True)

# test C
n_esami = dataset['N_ESAMI']
dataset.drop(columns=['N_ESAMI'], inplace=True)



# data normalization
X = dataset.values
#print(X)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ----------------------------
# define the appropriate number of clusters: 
# check Silhouette coefficients
"""
# range of k values ​​to explore
k_range = range(2, 10)

silhouette_scores = []

for k in k_range:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X_scaled)
    # silhouette coefficient for each k
    silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)
    silhouette_scores.append(silhouette_avg)

# silhouette graph
plt.figure(figsize=(10, 6))
plt.plot(k_range, silhouette_scores, marker='o')
plt.xlabel('Number of cluster (k)')
plt.ylabel('Silhouette coefficient')
plt.xticks(k_range)
plt.grid(True)
plt.show()

"""
# ----------------------------


# define the number of cluster
# ----------------
num_clusters = 2

# create an instance of the K-Means algorithm
kmeans = KMeans(n_clusters=num_clusters, random_state=42)

# training the model
kmeans.fit(X_scaled)

# cluster labels for each instance
labels = kmeans.labels_

# add cluster labels to the original dataset
dataset['Cluster'] = labels
dataset['N_ESAMI'] = n_esami


# calculate mean and variance for each feature, for each cluster found
# save mean and variance in a new excel file
save_output_data(dataset, '../../data/results/outputKMEANS/output_3C.xlsx')

# ----------------


# EVALUATION OF THE ALGORITHM
print("---------------------------")
# Silhouette coefficient
silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)
print("Il coefficiente di silhouette medio è:", silhouette_avg)



# PLOT DATA
"""
dataset_cluster_0 = dataset[dataset['Cluster'] == 0]
dataset_cluster_1 = dataset[dataset['Cluster'] == 1]

# extract values of the feature 
sodd_values_0 = dataset_cluster_0['N_ESAMI']
sodd_values_1 = dataset_cluster_1['N_ESAMI']

# plots the histogram of the distribution of feature values
#plt.hist(sodd_values_0, bins=20)
plt.hist(sodd_values_0, bins=30, alpha=0.5, label='Cluster 0', color='#28AFEA')  
plt.hist(sodd_values_1, bins=30, alpha=0.5, label='Cluster 1', color='#454FC3') 
plt.legend()
plt.title('Distribution of the feature N_ESAMI')
plt.xlabel('Values')
plt.ylabel('Freq')
plt.show()
"""