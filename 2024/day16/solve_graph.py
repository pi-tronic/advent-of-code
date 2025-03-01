def solve_graph(start_node, end_node, nodes, edges, lenghts, orientations):
    paths = [[start_node]]
    w_edges = edges.copy()
    while True:
        # break out
        done = True
        for path in paths:
            if type(path[-1])==int:
                done = False
                break
        if done:
            break

        past_corners = []
        new_paths = []
        for path in paths:
            #
            if type(path[-1])==int:
                past_corners.append(path[-1])
            else:
                new_paths.append(path)
                continue
            # find all neighbours
            neighbours = []
            for edge in w_edges:
                if edge[0]==path[-1]:
                    if edge[1] in path:
                        pass
                    else:
                        neighbours.append(edge[1])
                    if edge[1] in past_corners:
                        past_corners.remove(edge[1])
                elif edge[1]==path[-1]:
                    if edge[0] in path:
                        pass
                    else:
                        neighbours.append(edge[0])
                    if edge[0] in past_corners:
                        past_corners.remove(edge[0])
            for neighbour in neighbours:
                if neighbour==end_node:
                    new_paths.append(path+[neighbour]+['t'])
                else:
                    new_paths.append(path+[neighbour])
        paths = new_paths

        # delete old neighbours and their edges
        for corner in past_corners:
            try:
                nodes.remove(corner)
            except ValueError:
                continue
        for edge in w_edges:
            if edge[0] in past_corners or edge[1] in past_corners:
                w_edges.remove(edge)
        
    res = []
    for path in paths:
        lenght = 0
        o = 'h'
        for i in range(len(path)-2):
            # find edge
            if [path[i], path[i+1]] in edges:
                index = edges.index([path[i],path[i+1]])
            else:
                index = edges.index([path[i+1],path[i]])
            lenght += lenghts[index]
            if o!=orientations[index]:
                lenght += 1000
                o = orientations[index]
        # print(lenght, path[:-1])
        # res.append([lenght, path[:-1]])
        res.append(lenght)
    

    return res


# graph representation, 3-end, 8-start
#   0--1----2-3
#   |  |    |
#   4--5    6---7
#   |       |
#   8-------9
# edges = [[0,1], [1,2], [2,3], [4,5], [6,7], [8,9], [0,4], [4,8], [1,5], [2,6], [6,9]]
# lenghts = [2,4,1,2,3,7,1,1,1,1,1]
# orienation = ['h','h','h','h','h','h','v','v','v','v','v']
# corners = [0,1,2,3,4,5,6,7,8,9]

# start = 8
# end = 3

# solve_graph(start, end, corners, edges, lenghts, orienation)


if __name__ == "__main__":
    edges = [[0,1],[2,3],[4,5],[6,7],[8,9],[10,11],[12,13],[14,15],[15,16],[17,18],[19,20],[21,22],[22,23],[24,25],[26,27],[28,29],[30,31],[33,34],[34,35],[0,12],[12,32],[1,13],[13,17],[17,33],[2,18],[26,30],[30,34],[3,8],[21,27],[4,9],[14,22],[5,10],[10,15],[19,23],[28,31],[6,11],[11,16],[24,29],[7,20],[20,25]]
    lenghts = [2,2,2,2,2,2,2,2,2,2,4,2,2,2,2,2,6,2,10,4,10,4,2,8,6,2,2,2,2,2,4,2,2,2,2,2,2,2,6,2]
    orienation = ['h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','h','v','v','v','v','v','v','v','v','v','v','v','v','v','v','v','v','v','v','v','v','v']
    corners = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]

    start = 32
    end = 7

    solve_graph(start, end, corners, edges, lenghts, orienation)