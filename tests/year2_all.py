import subprocess
import os

# Define a list of tuples where each tuple contains the Python file to execute and the dataset path
# test all algorithms on the same subset: students of year 2 (test B: ETA, GENERE, CDL excluded)

"""
files_to_execute = [
    (r"C:\GitLab\ai-project-template\src\scripts\1_kmeans_analysis.py", r'C:\GitLab\ai-project-template\data\results\outputKMEANS\output_2B.xlsx'),
    (r"C:\GitLab\ai-project-template\src\scripts\2_dbscan_analysis.py", r'C:\GitLab\ai-project-template\data\results\outputDBSCAN\output_2B.xlsx'),
    (r"C:\GitLab\ai-project-template\src\scripts\3_hierarchical_analysis.py", r'C:\GitLab\ai-project-template\data\results\outputHIERARCHICAL\output_2B.xlsx'),
    (r"C:\GitLab\ai-project-template\src\scripts\4_umap_analysis.py", r'C:\GitLab\ai-project-template\data\results\outputUMAP\output_2B.xlsx'),
    (r"C:\GitLab\ai-project-template\src\scripts\5_som_analysis.py", r'C:\GitLab\ai-project-template\data\results\outputSOM\output_2B.xlsx'),
    (r"C:\GitLab\ai-project-template\src\scripts\6_gmm_analysis.py", r'C:\GitLab\ai-project-template\data\results\outputGMM\output_2B.xlsx')
]"""
files_to_execute = [
    ('../src/scripts/1_kmeans_analysis.py', '../data/results/outputKMEANS/output_2B.xlsx'),
    ('../src/scripts/2_dbscan_analysis.py', '../data/results/outputDBSCAN/output_2B.xlsx'),
    ('../src/scripts/3_hierarchical_analysis.py', '../data/results/outputHIERARCHICAL/output_2B.xlsx'),
    ('../src/scripts/4_umap_analysis.py', '../data/results/outputUMAP/output_2B.xlsx'),
    ('../src/scripts/5_som_analysis.py', '../data/results/outputSOM/output_2B.xlsx'),
    ('../src/scripts/6_gmm_analysis.py', '../data/results/outputGMM/output_2B.xlsx')
]

# Loop through the files and execute them one by one
for file, dataset_path in files_to_execute:
    # Extract only the file name from the path string
    filename = os.path.basename(file)
    print(f"Executing {filename}:")
    try:
        # Execute the Python file using subprocess and capture the output
        result = subprocess.run(["python", file, dataset_path], capture_output=True, text=True, check=True)
        # Print the output
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # If an error occurs during execution, print an error message
        print(f"Error during execution of {filename}: {e}")
