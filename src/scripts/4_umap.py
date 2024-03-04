from umap import UMAP
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.metrics import silhouette_score

from saveData import save_output_data

# Loading the dataset
#dataset = pd.read_excel(r'C:\GitLab\ai-project-template\data\processed\subset_3.xlsx')
dataset = pd.read_excel('../../data/processed/subset_1.xlsx')


# Select dataset columns with and without exclusions
#------------------------------------------------------------------#
# test A
#features = dataset.loc[:, :]
# test B
#features = dataset.drop(columns=["ETA", "CDL", "GENERE"])
# test C
features = dataset.drop(columns=["ETA", "CDL", "GENERE", "N_ESAMI"])
#------------------------------------------------------------------#


# Apply UMAP to reduce dimensionality to 2 and 3 dimensions
umap_2d = UMAP(n_components=2, init='random', random_state=0)
umap_3d = UMAP(n_components=3, init='random', random_state=0)

proj_2d = umap_2d.fit_transform(features)
proj_3d = umap_3d.fit_transform(features)


# Determine the optimal number of clusters using the elbow method
max_clusters = 10  # Maximum number of clusters to be considered
silhouette_scores = []
for n_clusters in range(2, max_clusters + 1):
   #Execute Kmean clustering with the current number of clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    cluster_labels = kmeans.fit_predict(features)
    
    #calculates the silhouette
    silhouette_avg = silhouette_score(features, cluster_labels)
    silhouette_scores.append(silhouette_avg)


# Find the optimal number of clusters using the elbow method
optimal_num_clusters = np.argmax(silhouette_scores) + 2  # +2 because we started with 2 clusters

# Perform KMeans clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=0)
cluster_labels = kmeans.fit_predict(features)

dataset['Cluster'] = cluster_labels


# calculate mean and variance for each feature, for each cluster found
# save mean and variance in a new excel file
save_output_data(dataset, '../../data/results/outputUMAP/output_1C.xlsx')

# ----------------


"""
# Calculate cluster centroids
centroids = kmeans.cluster_centers_


# Selects the nearest records to the centroids
nearest_records = []
for centroid in centroids:
    distances = np.linalg.norm(features - centroid, axis=1)
    nearest_index = np.argmin(distances)
    nearest_records.append(features.iloc[nearest_index])


# Create the two-dimensional scatter plot
fig_2d = px.scatter(
    dataset, x=proj_2d[:, 0], y=proj_2d[:, 1],
    colour=dataset.Cluster.astype(str), labels={'colour': 'Cluster'}
)

# Create the three-dimensional scatter plot
fig_3d = px.scatter_3d(
    dataset, x=proj_3d[:, 0], y=proj_3d[:, 1], z=proj_3d[:, 2],
    colour=dataset.Cluster.astype(str), labels={'colour': 'Cluster'}
)
fig_3d.update_traces(marker_size=5)

# display graphs
fig_2d.show()
fig_3d.show()


# Print the nearest records to the centroids
nearest_records_df = pd.DataFrame(nearest_records)
print("Records nearest to centroids:")
print(nearest_records_df)
"""

# EVALUATION OF THE ALGORITHM
print("---------------------------")
# Silhouette coefficient
silhouette_avg = silhouette_score(features, cluster_labels)
print("Il coefficiente di silhouette medio è:", silhouette_avg)
