import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder

onehot_encoder = OneHotEncoder(sparse=False)
X = np.array([[18, 2, "Tbilisi", "Engineer", 1000, 345667],
              [20, 6, "Tbilisi", "IT", 1400, 314313],
              [22, 6, "Batumi",  "IT", 1500, 134562],
              [25, 8, "Batumi",  "IT", 2400, 562334],
              [16, 2, "Tbilisi", "Engineer", 2000, 235621],
              [32, 7, "Tbilisi", "Engineer", 2234, 678433],
              [26, 3, "Batumi",  "Doctor", 3342, 442215],
              [28, 4, "Batumi",  "Doctor", 1234, 123456],
              [22, 5, "Batumi",  "Engineer", 4212, 544321],
              [19, 12, "Tbilisi", "Doctor", 5444, 712345]
              ])

df_x = pd.DataFrame(X, columns=['Age', 'WorkExperience', "City", "Proff", "Income", "LoanAmount"])

new_x = df_x[['Age', 'WorkExperience', 'Income', 'LoanAmount']]

cp = df_x[['City', 'Proff']]

onehot_encoded = pd.DataFrame(onehot_encoder.fit_transform(cp))

new_data = onehot_encoded.join(new_x)
print('New_Coordinates=')
print(new_data)

kmeans = KMeans(n_clusters=2)
kmeans.fit(new_data)

print(kmeans.cluster_centers_)
df_x['Class'] = kmeans.labels_
print(df_x)
