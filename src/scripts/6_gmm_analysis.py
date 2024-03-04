import pandas as pd
import sys

from analyzeData import evaluate_features

# Reading file excel
#data = pd.read_excel(r'C:\GitLab\ai-project-template\data\results\outputGMM\output_1A.xlsx')
#data = pd.read_excel('../../data/results/outputGMM/output_1B.xlsx')

def main(dataset_path):
    # load dataset
    data = pd.read_excel(dataset_path)
    
    # EVALUATE FEATURES IN DIFFERENT CLUSTERS
    # use par = 0.1 as accepted sovrapposition
    evaluate_features(data, 0.1)


# Check if the dataset path is provided as a command-line argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 6_gmm_analysis.py <dataset_path>")
        sys.exit(1)

    dataset_path = sys.argv[1]
    main(dataset_path)