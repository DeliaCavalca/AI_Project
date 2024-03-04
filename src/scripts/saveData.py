# import libraries
import pandas as pd

"""
function that calculate mean and variance for each feature in the dataset, for each cluster
and save this data a new excel file
"""
def save_output_data(dataset, filePath):
    # calculate mean and variance for each feature, for each cluster
    mean_data = dataset.drop(columns=['Cluster']).groupby(dataset['Cluster']).mean()
    var_data = dataset.drop(columns=['Cluster']).groupby(dataset['Cluster']).var()

    summary_df = pd.concat([mean_data.stack(), var_data.stack()], axis=1)

    # rename columns
    summary_df.columns = ['Mean', 'Variance']
    summary_df.index.names = ['Cluster', 'Feature']
    # set index
    summary_df.reset_index(inplace=True)

    # save data in a new excel file
    summary_df.to_excel(filePath, index=False)

    return