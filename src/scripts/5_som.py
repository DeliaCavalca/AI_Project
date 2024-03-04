from minisom import MiniSom
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from saveData import save_output_data

# Loading the dataset
#dataset = pd.read_excel(r'C:\GitLab\ai-project-template\data\processed\subset_3.xlsx')
dataset = pd.read_excel('../../data/processed/subset_1.xlsx')


# Exclude columns from feature selection
#---------------------------------------------------------------------------#
# test A
#features_to_exclude = []
# test B
#features_to_exclude = ["ETA", "CDL", "GENERE"]
# test C
features_to_exclude = ["ETA", "CDL", "GENERE", "N_ESAMI"]
features = [col for col in dataset.columns if col not in features_to_exclude]
#---------------------------------------------------------------------------#


# divide data into features (X) and targets (y)
data_x = dataset[features].values # features (independent)
data_y = dataset.iloc[:, 10].values # target (dependent)


# Split into training and test sets
train_x, test_x, train_y, test_y = train_test_split(data_x, data_y, test_size=0.2, random_state=42)


# SOM map size
som_width = 10
som_height = 10


# Creation and training of the SOM
som = MiniSom(som_width, som_height, len(train_x[0]), sigma=0.5, learning_rate=0.5)
som.train_random(train_x, 100)  # Training with 100 iterations


# Determination of BMUs (Best Matching Units) for each training data
bmu_indexes = np.array([som.winner(x) for x in train_x])


# SOM map plot
plt.figure(figsize=(som_width, som_height))
plt.pcolor(som.distance_map().T, cmap='bone_r')  # Plot of distances between neurons
plt.colorbar()


# Mark BMUs
for i, (x, y) in enumerate(bmu_indexes):
    plt.text(x + 0.5, y + 0.5, str(train_y[i]), color='k', ha='center', va='center', fontsize=10)
plt.grid()
plt.title('Self-Organizing Map')
plt.show()


# Calculating BMUs for the test dataset
bmu_indexes_test = np.array([som.winner(x) for x in test_x])


# Group the rows of the training dataset by clusters
clustered_data = {}
for i, (x, y) in enumerate(bmu_indexes):
    if (x, y) not in clustered_data:
        clustered_data[(x, y)] = []
    clustered_data[(x, y)].append(i)


# Calculating centroids for each cluster
centroids = {cluster: np.mean(train_x[indices], axis=0) for cluster, indices in clustered_data.items()}

# ----------------

# Creating the DataFrame for results
results_data = {'Cluster': [], 'Feature': [], 'Media': [], 'Varianza': []}

# Calculate mean and variance for each feature in each cluster
for (x, y), indices in clustered_data.items():
    cluster_data = train_x[indices]
    for feature_idx, feature_name in enumerate(features):
        feature_values = cluster_data[:, feature_idx]
        mean = np.mean(feature_values).round(2)
        variance = np.var(feature_values).round(2)
        results_data['Cluster'].append((x, y))
        results_data['Feature'].append(feature_name)
        results_data['Media'].append(mean)
        results_data['Varianza'].append(variance)


# Creating the DataFrame
results_df = pd.DataFrame(results_data)

# Saving the DataFrame to an Excel sheet
results_df.to_excel('../../data/results/outputSOM/output_1C.xlsx', index=False)

# ----------------