#!/usr/bin/env python

"""K- means clustering algorithm"""

import json
import math
import random

def kmeans(k_factor, json_file):
    """Takes in a json file and k and outputs k clusters after llyod's algo
    is applied.

    """
    parsed = parse_json(json_file)
    points = get_features(parsed)
    return apply_llyod(k_factor, points)

def parse_json(json_file):
    return json.loads(open(json_file,'r').read())

def get_features(parsed):
    return [(item['coordinates']['lat'], item['coordinates']['lng']) for item in parsed]

def apply_lloyd(points, k):
    centers = set_initial_centers(points, k)
    clusters = []
    i = 0
    while True:
        new_clusters = assign_points_to_clusters(points, centers)
        update_centers(centers, new_clusters)
        # ensure minimum number of iterations
        if new_clusters == clusters and i > 5:
            # TODO: return centers too?
            return new_clusters
        clusters = new_clusters
        i += 1

def set_initial_centers(points, k):
    # pick random centers
    return random.sample(points, k)

def assign_points_to_clusters(points, centers):
    # intialize clusters
    clusters = {}
    for (j,pt) in enumerate(centers):
        clusters[j] = []
    # TODO efficiency optimizations
    for point in points:
        least_distance = compute_distance(point, centers[0])
        best_center_index = 0
        for (i, center) in enumerate(centers):
            dist = compute_distance(point, center)
            if i > 0 and dist < least_distance:
                least_distance = dist
                best_center_index = i
        clusters[best_center_index].append(point)
    return clusters

def compute_distance(point1, point2):
    # l2 distance
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

def update_centers(centers, clusters):
    new_centers = []
    for (i, center) in enumerate(centers):
        cluster = clusters[i]
        new_centers.append(update_center(cluster))

def update_center(cluster):
    # compute the WCSS
    centroid_sum_x = 0
    centroid_sum_y = 0
    for point in cluster:
        centroid_sum_x += point[0]
        centroid_sum_y += point[1]
    return (centroid_sum_x / len(cluster), centroid_sum_y / len(cluster))
