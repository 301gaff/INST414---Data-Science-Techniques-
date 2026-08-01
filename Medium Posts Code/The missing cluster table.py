import numpy as np
import pandas as pd

cluster_results = pd.DataFrame(index=actor_genre_l1_df.index)
cluster_results["cluster"] = kmeans.labels_

# Distance from every actor to every centroid
distances_to_centroids = kmeans.transform(actor_genre_l1_df)

summary_rows = []

for cluster_id in range(kmeans.n_clusters):
    member_positions = np.where(kmeans.labels_ == cluster_id)[0]
    cluster_size = len(member_positions)

    # Find the three largest genre values in the centroid
    centroid = kmeans.cluster_centers_[cluster_id]
    top_genre_positions = np.argsort(centroid)[::-1][:3]
    top_genres = actor_genre_l1_df.columns[top_genre_positions].tolist()

    # Find two actors closest to the centroid
    member_distances = distances_to_centroids[
        member_positions, cluster_id
    ]
    representative_positions = member_positions[
        np.argsort(member_distances)[:2]
    ]
    representative_ids = actor_genre_l1_df.index[
        representative_positions
    ].tolist()

    summary_rows.append({
        "cluster": cluster_id,
        "actor_count": cluster_size,
        "top_genres": ", ".join(top_genres),
        "representative_actors": ", ".join(
            map(str, representative_ids)
        )
    })

cluster_summary_df = pd.DataFrame(summary_rows)
cluster_summary_df
