import numpy as np

class KNN_Regression:
    def __init__(self, N, k, points, distance_metric='euclidean'):
        self.N = N
        self.k = k
        self.points = np.array(points)  
        self.distance_metric = distance_metric
    
    def get_distance(self, x1, x2):
        if self.distance_metric == "euclidean":
            # Calculate Euclidean distance between given two points
            return np.sqrt((x1 - x2)**2)
        elif self.distance_metric == "manhattan":
            # Calculate Manhattan distance between given two points
            return np.abs(x1 - x2)
        else:
            print("Invalid distance metric! Choose either Euclidean or Manhattan.")
            return

    def predict(self, X):
        """Predict the Y value using k-NN regression."""
        if self.k > self.N:
            return "Error: k cannot be greater than N"
        
        # Get X and Y values
        X_train = self.points[:, 0]
        Y_train = self.points[:, 1]
        
        # Calculate distance between X and all training data points
        distances = self.get_distance(X_train, X)
        
        # Sort the distances and get indices of k nearest neighbors
        sorted_indices = np.argsort(distances)
        
        # Select the k nearest neighbors' output(Y) values
        nearest_neighbors_y = Y_train[sorted_indices[:self.k]]
        
        # Return the average of the k nearest neighbors' output(Y) values
        return np.mean(nearest_neighbors_y)

def main():
    # Read input from user
    N = int(input("Enter the number of data points N: "))
    k = int(input("Enter the number of nearest neighbors k: "))
    
    if k > N:
        print("Error: k cannot be greater than N")
        return
    
    distance_metric = str(input("Enter the distance metric (euclidean or manhattan): "))
    
    # Create a list for storing data points
    data_points = []
    
    for i in range(N):
        x = float(input(f"Enter the x value for point {i+1}: "))
        y = float(input(f"Enter the y value for point {i+1}: "))
        data_points.append((x, y))
    
    # Initialize KNN Regression model
    model = KNN_Regression(N, k, data_points)
    
    # Get the test point X
    X_test = float(input("Enter the test point X: "))
    
    # Predict the output y
    prediction = model.predict(X_test)
    print(f"Predicted Y value for X = {X_test}: {prediction}")

if __name__ == "__main__":
    main()