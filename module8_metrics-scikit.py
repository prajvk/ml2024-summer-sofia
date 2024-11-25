import numpy as np
from sklearn.metrics import precision_score, recall_score

# Read the number of points N from the user
N = int(input("Enter the number of points N: "))

# Initialize NumPy arrays to store the ground truth labels (X) and predicted labels (Y)
X = np.array([])  
Y = np.array([])  

# Read the N data points (x, y) from the user
for i in range(N):
    # read the input
    X_i = int(input(f"\nEnter either 0 or 1 as the x (ground truth) value for point {i + 1}: "))
    Y_i = int(input(f"Enter either 0 or 1 as the y (predicted) value for point {i + 1}: "))
    # assign the input to corresponding numpy arrays
    X = np.insert(X, i, X_i) 
    Y = np.insert(Y, i, Y_i)
    
# calculate Precision and Recall using Scikit-learn
precision = precision_score(X, Y)
recall = recall_score(X, Y)

#print results
print(f"\nPrecision = {precision:.2f}")
print(f"Recall = {recall:.2f}")