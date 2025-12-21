import numpy as np
import matplotlib.pyplot as plt

inputs = open("demo_inputs.txt")

coords = np.array([list(map(int, line[:-1].split(','))) for line in inputs.readlines()]).__invert__()

# find area of polygon
area = 0.5 * sum([coords[i,0] * (coords[i+1,1] + 1) - (coords[i+1,0] + 1) * coords[i,1] if i<coords.shape[0]-1 else coords[i,0] * coords[0,1] - coords[0,0] * coords[i,1] for i in range(coords.shape[0])])
print(f"Area: {area}")


X = sorted(list(set(coords[:,0])))
Y = sorted(list(set(coords[:,1])))
# find boxes inside polygon
for block_y in range(len(Y)-1):
    for block_x in range(len(X)-1):
        print(X[block_x], Y[block_y], X[block_x+1], Y[block_y+1])


# plotting
fig, ax = plt.subplots()
for x in X:
    ax.plot([x,x],[0,8], c='black', alpha=0.2)
for y in Y:
    ax.plot([0,12],[y,y], c='black', alpha=0.2)

ax.scatter(coords[:,0], coords[:,1], c='black', s=10, alpha=0.5)

plt.gca().invert_yaxis()
ax.set_xlabel('X', fontsize=15)
ax.set_ylabel('Y', fontsize=15)
ax.set_title('Find biggest rectangle')

fig.tight_layout()

plt.show()


inputs.close()