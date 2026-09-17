import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Read the dataset
data = pd.read_csv('iris.csv')

print("First few rows of the dataset:")
print(data.head())

# Separate features and labels
x = data.iloc[:,:4]
y = data.iloc[:, -1]

print("\nFeature data (first 5 rows):")
print(x.head())

print("\nLabels (first 5 rows):")
print(y.head())

# Split the dataset into training and testing data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20,random_state=42
)

print("\nTraining features (first 5 rows):")
print(x_train.head())

print("\nTesting features (first 5 rows):")
print(x_test.head())

# Standardize the features
sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Create K-NN classifier
classifier = KNeighborsClassifier(n_neighbors=5)

# Train the classifier
print(classifier.fit(x_train, y_train))

# Predict the test data
y_pred = classifier.predict(x_test)

print("\nArray:", y_pred)
print("\nActual labels:", y_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Accuracy
ac = accuracy_score(y_test, y_pred)

print("\nConfusion Matrix:", cm)
print("\nAccuracy:", ac)