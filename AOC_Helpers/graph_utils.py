
# 5. Graph and Pathfinding Utilities
import heapq
from collections import defaultdict


def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    return graph


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited


def dijkstra(use_graph=False, grid=None, graph=None, grid_wall_val="#"):
    """Dijkstra's algorithm either with a grid (with numbers as distances and grid_wall_val as wall)
    or graph as list of tuples as (start, dist, end), returns total distance and path points"""

    if use_graph:
        return dijkstra_graph(graph)
    else:
        return dijkstra_grid(grid, grid_wall_val)


def dijkstra_grid(grid, wall_val, start=(0, 0), end=None, save_distances=False):
    if not grid:
        return 0, []

    rows, cols = len(grid), len(grid[0])
    distances = {(r, c): float('inf') for r in range(rows) for c in range(cols)}
    distances[start] = 0

    min_heap = [(0, start)]
    path = {}

    while min_heap:
        dist, node = heapq.heappop(min_heap)
        r, c = node

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != wall_val:
                alt = dist + 1
                if alt < distances[(new_r, new_c)]:
                    distances[(new_r, new_c)] = alt
                    heapq.heappush(min_heap, (alt, (new_r, new_c)))
                    path[(new_r, new_c)] = (r, c)

    if end not in path:
        return -1, []

    total_dist = distances[end]
    path_points = []
    current = end

    while current:
        path_points.append(current)
        current = path.get(current)

    path_points.reverse()
    return total_dist, path_points


def dijkstra_graph(graph):
    if not graph:
        return 0, []

    graph_dict = {}
    for start, dist, end in graph:
        if start not in graph_dict:
            graph_dict[start] = []
        graph_dict[start].append((dist, end))

    distances = {node: float('inf') for _, node in graph}
    distances[graph[0][0]] = 0

    min_heap = [(0, graph[0][0])]
    path = {}

    while min_heap:
        dist, node = heapq.heappop(min_heap)
        if node not in graph_dict:
            continue

        for next_dist, neighbor in graph_dict[node]:
            alt = dist + next_dist
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                heapq.heappush(min_heap, (alt, neighbor))
                path[neighbor] = node

    if graph[-1][2] not in path:
        return -1, []

    total_dist = distances[graph[-1][2]]
    path_points = []
    current = graph[-1][2]

    while current:
        path_points.append(current)
        current = path.get(current)

    path_points.reverse()
    return total_dist, path_points
