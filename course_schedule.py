"""
Given an integer n representing the number of courses(courses are labeled from
0 to n-1), and an array prerequisites where prerequisites[i] = [a,b] means that you first
need to take the course b before taking the course a, determine if it's possible to finish
all the courses.
"""

from collections import deque

# Depth-First Search
def dfs(graph, vertex, path, order, visited) -> bool:
    path.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor in path:
            return False
        if neighbor not in visited:
            visited.add(neighbor)
            if not dfs(graph, neighbor, path, order, visited):
                return False
    path.remove(vertex)
    order.append(vertex)
    return True

def dfs_course_schedule(n, prerequisites) -> bool:
    graph = [[] for _ in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
    visited = set()
    path = set()
    order = []
    for course in range(n):
        if course not in visited:
            visited.add(course)
            if not dfs(graph, course, path, order, visited):
                return False
    return True


# Breadth-First Search
def bfs_course_schedule(n, prerequisites) -> bool:
    graph = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1
    order = []
    queue = deque([i for i in range(n) if indegree[i] == 0])
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return len(order) == n


if __name__ == '__main__':
    n = 6
    true_prerequisites = [[3,0], [1,3], [2,1], [4,1], [4,2], [5,3], [5,4]]
    false_prerequisites = [[0,1], [3,0], [1,3], [2,1], [4,1], [4,2], [5,3], [5,4]]
    dfs_result = dfs_course_schedule(n, true_prerequisites)
    bfs_result = bfs_course_schedule(n, true_prerequisites)
    print(f"Check whether the student can pass all the courses using DFS: {dfs_result}")
    print(f"Check whether the student can pass all the courses using BFS: {bfs_result}")