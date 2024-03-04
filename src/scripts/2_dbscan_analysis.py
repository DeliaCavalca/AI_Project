# import libraries
import pandas as pd
import sys

# load dataset
#data = pd.read_excel(r'ai-project-template\data\results\outputDBSCAN\output_1A.xlsx')
#data = pd.read_excel('../../data/results/outputDBSCAN/output_3A.xlsx')

def main(dataset_path):
    # load dataset
    data = pd.read_excel(dataset_path)
    num_clusters = 1

    # EVALUATE THE FEATURES IN DIFFERENT CLUSTERS

    features_diff = set()

    for i in range(num_clusters):

        cluster1_data = data[data['Cluster'] == 0]

        for (index1, row1) in (cluster1_data.iterrows()):
            feature= row1['Feature']
            mean = row1['Mean']
            var = row1['Variance']

            #print(feature, " Cluster - mean: ", mean, " - var: ", var)

            if (var < 0.5):
                features_diff.add(feature)
            
            #print()
    
    print("---------------------------")
    print("Feature rappresentative del cluster: ")
    print(sorted(features_diff))

# Check if the dataset path is provided as a command-line argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2_dbscan_analysis.py <dataset_path>")
        sys.exit(1)

    dataset_path = sys.argv[1]
    main(dataset_path)
