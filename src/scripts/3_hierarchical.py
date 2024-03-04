# import libraries
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score, calinski_harabasz_score

from saveData import save_output_data

"""
Agglomerative Hierarchical Clustering: 
build nested clusters by merging or splitting them successively;
performs a hierarchical clustering using a bottom up approach: each observation starts in its own cluster, 
and clusters are successively merged together;

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

#dataset.drop(columns=['VOTO_DIPLOMA'], inplace=True)

# test C
#n_esami = dataset['N_ESAMI']
#dataset.drop(columns=['N_ESAMI'], inplace=True)


# ----------------
# initialize the clustering obj
# n_clusters default = 2
clustering = AgglomerativeClustering(n_clusters=2, linkage='ward')

# training the model
clustering.fit(dataset)

# cluster labels for each instance
labels = clustering.labels_

num_clusters = len(set(labels))
print("Numero di cluster:", num_clusters)
print(labels)


# visualization of cluster hierarchy (dendrogram)
linkage_matrix = linkage(dataset, method='ward')  
dendrogram(linkage_matrix)
plt.title('Dendrogramma gerarchico')
plt.xlabel('Indici dei campioni')
plt.ylabel('Distanza')
plt.show()



# add cluster labels to the original dataset
dataset['Cluster'] = labels
#dataset['N_ESAMI'] = n_esami


# calculate mean and variance for each feature, for each cluster found
# save mean and variance in a new excel file
save_output_data(dataset, '../../data/results/outputHIERARCHICAL/output_3B.xlsx')

# ----------------


# EVALUATION OF THE ALGORITHM
print("---------------------------")
silhouette_avg = silhouette_score(dataset, labels)
print("Silhouette Score:", silhouette_avg)
