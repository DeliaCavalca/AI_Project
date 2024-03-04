import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from numpy import unique

from saveData import save_output_data

# loading dataset
#dataset = pd.read_excel(r'C:\GitLab\ai-project-template\data\processed\subset_3.xlsx')
dataset = pd.read_excel('../../data/processed/subset_1.xlsx')


# Exclude columns from feature selection
#----------------------------------------------------------#
# test A
#features_to_exclude = []
# test B
#features_to_exclude = ["ETA", "CDL", "GENERE"]
# test C
features_to_exclude = ["ETA", "CDL", "GENERE", "N_ESAMI"]
#----------------------------------------------------------#


# Exclude features specified by the dataset
dataset_filtered = dataset.drop(columns=features_to_exclude)


# Definition of Gaussian Mixture model with 4 components
model = GaussianMixture(n_components=4)

# Model training
model.fit(dataset_filtered)

# Assigning a cluster to each example
labels = model.predict(dataset_filtered)

# Adding the 'Cluster' column to the dataset
dataset['Cluster'] = labels

# Calculation of centroids for each cluster
centroids = model.means_


# calculate mean and variance for each feature, for each cluster found
# save mean and variance in a new excel file
save_output_data(dataset, '../../data/results/outputGMM/output_1C.xlsx')

# ----------------


# EVALUATION OF THE ALGORITHM
print("---------------------------")
# Silhouette coefficient
silhouette_avg = silhouette_score(dataset_filtered, labels)
print("Il coefficiente di silhouette medio è:", silhouette_avg)