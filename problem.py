# In DFS first the ending point is defined
# In BFS first the sibling points checked
# I have solved it with the DFS algorithm because it goes at the ending point first

# -------------------------------------------------------------------------


def check(mat, visited, x, y):
    return (x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and mat[x][y] == 1 and (not visited[x][y]))


def findShortestPath(mat, visited, i, j, x, y, min_dist, dist):
    # end of the path added to tyhe array
    # print(i, j, dist)
    if (i == x and j == y):
        alldist.append(dist)
        print(alldist)
        min_dist = min(alldist)
        # min_dist = min(dist, min_dist)
        return min_dist

    # set mat(i, j) as visited
    visited[i][j] = True

    # bottom
    if (check(mat, visited, i + 1, j)):
        min_dist = findShortestPath(
            mat, visited, i + 1, j, x, y, min_dist, dist + 1)

    # right
    if (check(mat, visited, i, j + 1)):
        min_dist = findShortestPath(
            mat, visited, i, j + 1, x, y, min_dist, dist + 1)

    # top
    if (check(mat, visited, i - 1, j)):
        min_dist = findShortestPath(
            mat, visited, i - 1, j, x, y, min_dist, dist + 1)

    # left
    if (check(mat, visited, i, j - 1)):
        min_dist = findShortestPath(
            mat, visited, i, j - 1, x, y, min_dist, dist + 1)

    visited[i][j] = False
    return min_dist


def findPathLen(arr, s, e):
    # check the neighbourd value of starting point
    if (len(arr) == 0 or arr[s[0]][s[1]] == 0
            or arr[e[0]][e[1]] == 0):
        return -1

    row = len(arr)
    col = len(arr[0])

    visited = []
    for i in range(row):
        visited.append([None for _ in range(col)])

    dist = e[0]*e[1]
    dist = findShortestPath(arr, visited, s[0],
                            s[1], e[0], e[1], dist, 0)

    if (dist > 0):
        return dist
    return -1


arr = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
]
alldist = []
starting = [0, 0]
ending = [5, 5]
dist = findPathLen(arr,  starting, ending)
if (dist != -1):
    print("Shortest Path is", dist)

else:
    print("Shortest Path doesn't exist")
