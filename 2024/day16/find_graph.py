import numpy as np

def find_graph(file):
    # get data
    inputs = open(file)

    # read in instruction lines
    contents = inputs.readlines()

    # array representation
    array = np.asarray([np.array(list(line[:-1])) for line in contents])

    # start + end position
    start_position = np.argwhere(array=='S')[0]
    end_position = np.argwhere(array=='E')[0]

    # change start and and to free space
    array[start_position[0], start_position[1]] = '.'
    array[end_position[0], end_position[1]] = '.'

    # find corners
    corners = []
    for row in range(np.shape(array)[0]):
        for col in range(np.shape(array)[1]):
            if row==start_position[0] and col==start_position[1]:
                corners.append([row, col])
                continue
            elif row==end_position[0] and col==end_position[1]:
                corners.append([row, col])
                continue

            if array[row, col] == '.':
                # check if corner
                up_down = False
                left_right = False
                # up
                if row-1 >= 0:
                    if array[row-1, col]=='.':
                        up_down = True
                # down
                if row+1 < np.shape(array)[0]:
                    if array[row+1, col]=='.':
                        up_down = True
                # left
                if col-1 >= 0:
                    if array[row, col-1]=='.':
                        left_right = True
                # right
                if col+1 < np.shape(array)[1]:
                    if array[row, col+1]=='.':
                        left_right = True
                
                if up_down and left_right:
                    corners.append([row, col])

    edges = []
    orientation = []
    lenghts = []
    corners_arr = np.asarray(corners)
    rows = np.unique(corners_arr[:,1])
    cols = np.unique(corners_arr[:,0])

    print(corners_arr)

    for row in rows:
        cs = corners_arr[corners_arr[:,0]==row]
        for c in range(len(cs)-1):
            is_conescutive = True
            for v in range(cs[c,1]+1, cs[c+1,1]):
                if array[row, v] == '#':
                    is_conescutive = False
                    break
            if is_conescutive:
                index_0 = corners.index(list(cs[c]))
                index_1 = corners.index(list(cs[c+1]))
                edges.append([index_0,index_1])
                orientation.append('h')
                lenghts.append(abs(cs[c+1,1]-cs[c,1]))

    for col in cols:
        cs = corners_arr[corners_arr[:,1]==col]
        for c in range(len(cs)-1):
            is_conescutive = True
            for v in range(cs[c,0]+1, cs[c+1,0]):
                if array[v, col] == '#':
                    is_conescutive = False
                    break
            if is_conescutive:
                index_0 = corners.index(list(cs[c]))
                index_1 = corners.index(list(cs[c+1]))
                edges.append([index_0,index_1])
                orientation.append('v')
                lenghts.append(abs(cs[c+1,0]-cs[c,0]))

    nodes = [i for i in range(len(corners))]
    start = corners.index(list(start_position))
    end = corners.index(list(end_position))

    # print(edges)
    # print(lenghts)
    # print(orientation)
    # print(nodes)
    # print(start)
    # print(end)

    return edges, lenghts, orientation, nodes, start, end

if __name__=="__main__":
    edges, lenghts, orientation, nodes, start, end = find_graph('./my_file01.txt')
    
    print(edges)
    print(lenghts)
    print(orientation)
    print(nodes)
    print(start)
    print(end)