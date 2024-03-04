# import libraries
import pandas as pd

"""
function that evaluate features in different clusters,
find rilevant features
"""
def evaluate_features(data, par):
    features_diff = set()
    features_diff_2 = set()

    # extract clusters 
    clusters = data['Cluster'].unique()
    #print("Cluster presenti nel dataset:", clusters)

    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            # compare cluster i with cluster j            
            cluster1_data = data[data['Cluster'] == clusters[i]]
            cluster2_data = data[data['Cluster'] == clusters[j]]
            #print(f"Confronto tra il cluster {clusters[i]} e il cluster {clusters[j]}")
            
            for ((index1, row1), (index2, row2)) in zip(cluster1_data.iterrows(), cluster2_data.iterrows()):
                feature= row1['Feature']
                # get mean and var of a specific feature, cluster i
                mean_1 = row1['Mean']
                var_1 = row1['Variance']
                # get mean and var of a specific feature, cluster j
                mean_2 = row2['Mean']
                var_2 = row2['Variance']

                #print(feature, " Cluster ", i, " - mean: ", mean_1, " - var: ", var_1)
                #print(feature, " Cluster ", j, " - mean: ", mean_2, " - var: ", var_2)
                
                if mean_1 < mean_2:
                    # Ideal check: no overlap
                    if mean_1 + var_1 < mean_2 - var_2:
                        features_diff.add(feature)
                    else:
                        # Second check: small overlap
                        if abs((mean_1 + var_1) - (mean_2 - var_2)) < par :
                            features_diff_2.add(feature)
                elif mean_1 > mean_2:
                    # Ideal check: no overlap
                    if mean_2 + var_2 < mean_1 - var_1:
                        features_diff.add(feature)
                    else:
                        # Second check: small overlap
                        if abs((mean_1 + var_1) - (mean_2 - var_2)) < par :
                            features_diff_2.add(feature)
                #print()

    print("---------------------------")
    print("Feature rappresentative dei due cluster: ")
    print(sorted(features_diff))
    print("Feature rappresentative (ma meno) dei due cluster: ")
    print(sorted(features_diff_2))
