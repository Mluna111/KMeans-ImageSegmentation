
#Kmeans applied to image for color segmentation

import numpy as np
from PIL import Image
from numpy import asarray

def distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# Implementing Expectation step
def assign_clusters(X, clusters):
    for idx in range(X.shape[0]):
        dist = []
        curr_x = X[idx]
        for i in range(k):
            dis = distance(curr_x, clusters[i]['center'])
            dist.append(dis)
        curr_cluster = np.argmin(dist)
        clusters[curr_cluster]['points'].append(curr_x)
    return clusters

# Implementing the Matching Step
def update_clusters(X, clusters):
    difference = 0
    for i in range(k):
        points = np.array(clusters[i]['points'])
        if points.shape[0] > 0:
            new_center = points.mean(axis=0)
            difference += distance(new_center, clusters[i]['center']) ** 2
            clusters[i]['center'] = new_center
            clusters[i]['points'] = []
    return clusters, difference

# Calculate distance again for new centers of each cluster and assign them to a cluster in the prediction
def pred_cluster(X, clusters):
    pred = []
    for i in range(X.shape[0]):
        dist = []
        for j in range(k):
            dist.append(distance(X[i], clusters[j]['center']))
        pred.append(np.argmin(dist))
    return pred

# Generating data
img = Image.open('super.png')
numpydata = asarray(img)
original_shape = numpydata.shape
print("Original shape:", original_shape)

# Reshape image data for processing
numpydata = numpydata.reshape((-1, original_shape[2]))
new_image_data = np.zeros((original_shape[0] * original_shape[1], original_shape[2]))

print("Numpy data shape:", numpydata.shape)
np.savetxt('test1.txt', numpydata, fmt='%d')

k = 7
clusters = {}

seed = 3
np.random.seed(seed)

# Initialize the clusters
for idx in range(k):
    center = 255 * np.random.random((numpydata.shape[1],))
    if idx > 0:
        for idx2 in range(idx):
            while distance(clusters[idx2]['center'], center) < 10:
                center = 255 * np.random.random((numpydata.shape[1],))
    cluster = {
        'center': center,
        'points': []
    }
    clusters[idx] = cluster

print("Initial clusters:")
for idx in range(k):
    print(f"Cluster {idx}: Center = {clusters[idx]['center']}")

squared_diff = 1
while squared_diff > 0:
    squared_diff -= 1
    clusters = assign_clusters(numpydata, clusters)
    clusters, squared_diff = update_clusters(numpydata, clusters)

print("Final clusters:")
for idx in range(k):
    print(f"Cluster {idx}: Center = {clusters[idx]['center']}")

pred = pred_cluster(numpydata, clusters)
np.savetxt('pred1.txt', pred, fmt='%d')

# Fill in the new image array with the colors of the cluster centers
for i in range(len(pred)):
    cluster_id = pred[i]
    cluster_center_color = clusters[cluster_id]['center']
    new_image_data[i] = cluster_center_color

# Reshape to the original image shape
new_image_data = new_image_data.reshape(original_shape)
print("New image data shape:", new_image_data.shape)

# Check some values of new image data before saving
print("Sample values from new image data:")
print(new_image_data[:5])

# Create and save the new image
    # use RGB or RGBA depending on the shape
if(len(clusters[0]['center']) == 4):
    new_image = Image.fromarray(new_image_data.astype('uint8'), 'RGBA')
else:
    new_image = Image.fromarray(new_image_data.astype('uint8'), 'RGB')

new_image.save('reconstructed_super.png')
print('Image reconstructed and saved.')



