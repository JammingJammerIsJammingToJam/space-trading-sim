def dist(pos1, pos2):
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2 + (pos2[2] - pos1[2]) ** 2) ** 0.5

def points_in_radius(pos, points, radius):
    return [point for point in points if dist(pos, point) <= radius]

def create_edges(points, radius):
    edges = []
    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            d = dist(points[i], points[j])
            if d <= radius:
                edges.append([i, j, d])
    return edges

def dijkstra():
print(create_edges([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 2))