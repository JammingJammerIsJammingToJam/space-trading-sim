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

def edges_for_point(edges, point):
    new_edges = []
    for edge in edges:
        if edge[0] == point:
            new_edges.append(edge[1:])
        elif edge[1] == point:
            new_edges.append(edge[::2])
    return new_edges

def dijkstra(points, start, end, radius):
    edges = create_edges(points, radius)
    unvisited = [i for i in range(0, len(points))]
    shortest = [float('inf') for i in range(0, len(points))]
    shortest[start] = 0
    previous = ['' for i in range(0, len(points))]
    while unvisited != []:
        p = min(unvisited, key=lambda i: shortest[i])
        if shortest[p] == float('inf'):
            break
        for edge in edges_for_point(edges, p):
            if shortest[edge[0]] > shortest[p] + edge[1]:
                shortest[edge[0]] = shortest[p] + edge[1]
                previous[edge[0]] = str(p)
        unvisited.remove(p)
    if shortest[end] == float('inf'):
        return []
    path = [end]
    node = previous[end]
    while node != '':
        path.append(int(node))
        node = previous[int(node)]
    return path[::-1]

def dijkstra_dist(points, start, end, radius):
    path = dijkstra(points, start, end, radius)
    distance = 0
    for i in range(0, len(path) - 1):
        distance += dist(points[path[i]], points[path[i+1]])
    return distance



    



print(create_edges([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 2), 1)
print(dijkstra([[1, 1, 1], [2, 2, 2], [3, 3, 3], [5, 5, 5]], 0, 2, 2))
print(dijkstra_dist([[1, 1, 1], [2, 2, 2], [3, 3, 3], [5, 5, 5]], 0, 2, 2))