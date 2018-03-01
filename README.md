# Principal-Component-Analysis
Using PCA for dimensionality reduction on a sample data-set with multiple attributes information related to given number of patients. After PCA, we identify 5 nearest patients to a given patient data. 

Input Format

Line 1: D (number of data dimensions that can be between 1 to 10000)

Line 2: N (number of patients-between 1 to 1000)

Line 3: The type of distance metric (1: Manhattan distance, 2: Euclidean distance, 3: Supremum distance, 4: Cosine similarity)

Line 4: X, the number of principal components in PCA to use to transform the original dataset to a new space.

Line 5: Patient P data that contains D integers

Line 6 to 6+N: The original dataset--- each line contains D integers for each patient

Output:

5 most neareast patients in new line followed by cumulative explained variance ratio in a new line.
