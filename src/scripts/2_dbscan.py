# import libraries
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt

from saveData import save_output_data

"""
DBSCAN (Density-Based Spatial Clustering of Applications with Noise): 
this algorithm views clusters as areas of high density separated by areas of low density;
it groups together data points that are densely clustered in space,
identifying regions of high density separated by regions of low density

input: eps and min_samples
eps = radius of the neighborhood
min_samples = minimum number of points needed to form a cluster
higher min_samples or lower eps indicate higher density necessary to form a cluster;

"""

# load dataset
dataset = pd.read_excel('../../data/processed/subset_1.xlsx')
#dataset = pd.read_excel('../../data/processed/subset_2.xlsx')
#dataset = pd.read_excel('../../data/processed/subset_3.xlsx')

print(f"\nThe dataset has {dataset.shape[0]} rows and {dataset.shape[1]} columns.\n")

# remove columns before the clustering
# test A
dataset.drop(columns=['ANNO'], inplace=True)

# test B
dataset.drop(columns=['ETA'], inplace=True)
dataset.drop(columns=['CDL'], inplace=True)
dataset.drop(columns=['GENERE'], inplace=True)

#dataset.drop(columns=['VOTO_DIPLOMA'], inplace=True)
#dataset.drop(columns=['MEDIA_VOTI'], inplace=True)

# test C
#n_esami = dataset['N_ESAMI']
#dataset.drop(columns=['N_ESAMI'], inplace=True)



# data normalization
X = dataset.values
#print(X)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ----------------------------
# define the appropriate number of eps
"""
n_neighbors = 30
# calculate the distance between points
nearest_neighbors = NearestNeighbors(n_neighbors=n_neighbors)
nearest_neighbors.fit(X_scaled)
distances, _ = nearest_neighbors.kneighbors(X_scaled)


mean_distances = np.mean(distances, axis=1)

# Plot della distribuzione delle distanze
plt.hist(mean_distances, bins=30)
plt.xlabel('Distanza media')
plt.ylabel('Frequenza')
plt.title('Distribuzione delle distanze medie')
plt.show()

eps_initial = np.mean(mean_distances)
print("Valore iniziale di eps:", eps_initial)

# ----------------------------
avg_distances_sorted = np.sort(mean_distances)

plt.plot(avg_distances_sorted)

knee_index = np.argmax(np.diff(avg_distances_sorted)) + 1
knee_distance = avg_distances_sorted[knee_index]

plt.axvline(x=knee_index, color='r', linestyle='--')
plt.xlabel('Indice dei campioni')
plt.ylabel('Distanza media dei vicini più prossimi')
plt.show()
"""
# ----------------------------


# define the DBSCAN model
# ----------------
eps = 5
min_samples = 30
dbscan = DBSCAN(eps=eps, min_samples=min_samples)

# training the model
dbscan.fit(X_scaled)

# cluster labels for each instance (-1 = noise point)
labels = dbscan.labels_

# number of clusters found
num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print("Numero di cluster:", num_clusters)

# noise points
num_noise_points = np.sum(labels == -1, axis=0)
print("Numero di punti di rumore:", num_noise_points)


# add cluster labels to the original dataset
dataset['Cluster'] = labels
#dataset['N_ESAMI'] = n_esami


# calculate mean and variance for each feature, for each cluster found
# save mean and variance in a new excel file
save_output_data(dataset, '../../data/results/outputDBSCAN/output_1B.xlsx')

# ----------------



# EVALUATION OF THE ALGORITHM
print("---------------------------")
silhouette_avg = silhouette_score(dataset, labels)
print("Silhouette Score:", silhouette_avg)

