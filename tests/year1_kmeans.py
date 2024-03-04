import subprocess
import os

# Define a list of tuples where each tuple contains the Python file to execute and the dataset path
# test kmeans algorithm on students of year 1 (test A: all features; test B: ETA, GENERE, CDL excluded; test C: ETA, GENERE, CDL, N_ESAMI excluded)

"""
files_to_execute = [
    (r"C:\GitLab\ai-project-template\src\scripts\1_kmeans_analysis.py", r'C:\GitLab\ai-project-template\data\results\outputKMEANS\output_1A.xlsx'),
    (r"C:\GitLab\ai-project-template\src\scripts\1_kmeans_analysis.py", r'C:\GitLab\ai-project-template\data\results\outputKMEANS\output_1B.xlsx'),
    (r"C:\GitLab\ai-project-template\src\scripts\1_kmeans_analysis.py", r'C:\GitLab\ai-project-template\data\results\outputKMEANS\output_1C.xlsx'),
    
]"""
files_to_execute = [
    ('../src/scripts/1_kmeans_analysis.py', '../data/results/outputKMEANS/output_1A.xlsx'),
    ('../src/scripts/1_kmeans_analysis.py', '../data/results/outputKMEANS/output_1B.xlsx'),
    ('../src/scripts/1_kmeans_analysis.py', '../data/results/outputKMEANS/output_1C.xlsx'),
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
