import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder

onehot_encoder = OneHotEncoder(sparse=False)
X = np.array([[185, 72, "Tbilisi"],
              [170, 56, "Tbilisi"],
              [168, 60, "Batumi"],
              [179, 68, "Batumi"],
              [182, 72, "Kutaisi"],
              [188, 77, "Kutaisi"],
              [162, 72, "Gori"],
              [152, 72, "Gori"],
              [178, 77, "Gori"]
              ])

df_x = pd.DataFrame(X, columns=['X1', 'X2', "City"])
print(df_x)

new_x = df_x[['X1', 'X2']]
print(new_x)

Colors = df_x[['City']]
print(Colors)

onehot_encoded = pd.DataFrame(onehot_encoder.fit_transform(Colors))
print(onehot_encoded)

New_Coordinates = onehot_encoded.join(new_x)
print('New_Coordinates=')
print(New_Coordinates)

kmeans = KMeans(n_clusters=4)
kmeans.fit(New_Coordinates)

print(kmeans.cluster_centers_)
df_x['Class'] = kmeans.labels_
print(df_x)
