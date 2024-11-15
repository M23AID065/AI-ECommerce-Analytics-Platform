
from sklearn.cluster import KMeans

def segment_customers(data):
    model = KMeans(n_clusters=3, random_state=42)
    clusters = model.fit_predict(data)
    return {"clusters": clusters.tolist()}
