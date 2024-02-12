import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

dataset = pd.read_csv("Diabetes_RF.csv")
print(dataset.head())

# Bar Chart for the 'Class variable' (Outcome)
plt.figure(figsize=(8, 5))
sns.countplot(x='Class variable', data=dataset)
plt.title('Bar Chart - Diabetes Outcome')
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.show()

# Pie Chart for the 'Class variable' (Outcome)
plt.figure(figsize=(8, 5))
labels = ['No Diabetes', 'Diabetes']
sizes = dataset['Class variable'].value_counts()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightblue'])
plt.title('Pie Chart - Diabetes Outcome')
plt.show()

# Line Graph for Age vs Plasma glucose concentration
plt.figure(figsize=(8, 5))
sns.lineplot(x='Age', y='Plasma glucose concentration', data=dataset)
plt.title('Line Graph - Age vs Plasma Glucose Concentration')
plt.xlabel('Age')
plt.ylabel('Plasma Glucose Concentration')
plt.show()

# Box Plot for each feature
plt.figure(figsize=(7, 4))
sns.boxplot(data=dataset.drop('Class variable', axis=1))
plt.title('Box Plot - Features Distribution')
plt.xticks(rotation=45)
plt.show()

# Histogram for each feature
dataset.drop('Class variable', axis=1).hist(figsize=(12, 7), bins=20)
plt.suptitle('Histograms of Features', y=1.02)
plt.show()

# Scatter Plot for Age vs Plasma glucose concentration
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Plasma glucose concentration', data=dataset, hue='Class variable')
plt.title('Scatter Plot - Age vs Plasma Glucose Concentration')
plt.xlabel('Age')
plt.ylabel('Plasma Glucose Concentration')
plt.legend(title='Outcome')
plt.show()
