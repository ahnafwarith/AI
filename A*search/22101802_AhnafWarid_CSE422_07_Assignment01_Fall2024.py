import heapq

# Load graph data from file
def load_graph(filename):
    graph = {}
    heuristics = {}

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            city = parts[0]
            heuristic = int(parts[1])
            heuristics[city] = heuristic
            neighbors = {}

            for i in range(2, len(parts), 2):
                neighbor = parts[i]
                distance = int(parts[i + 1])
                neighbors[neighbor] = distance

            graph[city] = neighbors

    return graph, heuristics

# A* search algorithm
def a_star_search(graph, heuristics, start, goal):
    sets = []
    heapq.heappush(sets, (0, start))
    parentN = {}
    gSC = {node: float('inf') for node in graph}
    gSC[start] = 0
    fSC = {node: float('inf') for node in graph}
    fSC[start] = heuristics[start]

    while sets:
        current = heapq.heappop(sets)[1]

        if current == goal:
            return reconstruct_path(parentN, current), gSC[goal]

        for neighbor, distance in graph[current].items():
            tentative_gSC = gSC[current] + distance

            if tentative_gSC < gSC[neighbor]:
                parentN[neighbor] = current
                gSC[neighbor] = tentative_gSC
                fSC[neighbor] = gSC[neighbor] + heuristics[neighbor]
                heapq.heappush(sets, (fSC[neighbor], neighbor))

    return None, None

# Reconstruct path from start to goal
def reconstruct_path(parentN, current):
    path = []
    while current in parentN:
        path.append(current)
        current = parentN[current]
    path.append(current)
    path.reverse()
    return path

# Main function
def main():
    filename = input("Enter the filename: ")
    graph, heuristics = load_graph(filename)

    startNode = input("Start node: ")
    goalNode = input("Destination: ")

    path, total_distance = a_star_search(graph, heuristics, startNode, goalNode)

    if path:
        print("Path:", " -> ".join(path))
        print("Total distance:", total_distance, "km")
    else:
        print("NO PATH FOUND")

if __name__ == "__main__":
    main()