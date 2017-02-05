from heapq import heappush, heappop

def dijkstra(graph, start, end):
	visited = [False] * len(graph)
	heap = [(0, start)]

	while heap:
		# get the smallest dist node
		node_dist, node = heappop(heap)
		if node == end:
			return node_dist
		if visited[node] is False:
			visited[node] = True
			# update its neighbors' distances
			for neighbor, edge_weight in graph[node].items():
				if visited[neighbor] is False:
					heappush(heap, (node_dist + edge_weight, neighbor))

	# we loop through the graph and cannot find the end node
	return -1

if __name__ == "__main__":
	graph = {
		0: {
			1: 2,
			2: 5,
			3: 9
		},
		1: {
			0: 2,
			3: 1
		},
		2: {
			0: 5,
			3: 2
		},
		3: {
			0: 9,
			1: 1,
			2: 2
		}
	}

	print dijkstra(graph, 0, 3)