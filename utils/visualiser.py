import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import List
from core.board import Board
import numpy as np

class Visualiser:
    def __init__(self):
        # Initialize figure once for dynamic updates
        plt.ion()  # turn on interactive mode
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_box_aspect([1, 1, 1])

    def plot_board(self, board: Board):
        size = board.size

        # Clear the previous scatter plot
        self.ax.cla()

        xs: List[float] = []
        ys: List[float] = []
        zs: List[float] = []
        colors = []

        for x in range(size):
            for y in range(size):
                for z in range(size):
                    val = board.board[x, y, z]

                    if val == 0:
                        continue

                    # Swap axes: X and Z are floor, Y is height
                    xs.append(x)
                    ys.append(y)  # vertical
                    zs.append(z)

                    colors.append("red" if val == 1 else "blue")

        # Convert to numpy arrays for matplotlib
        xs = np.array(xs, dtype=float) # type: ignore
        ys = np.array(ys, dtype=float) # type: ignore
        zs = np.array(zs, dtype=float) # type: ignore

        # Plot
        self.ax.scatter(xs, ys, zs, c=colors, s=200)  # type: ignore

        # Set labels
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y (Height)")
        self.ax.set_zlabel("Z")

        # Set limits
        self.ax.set_xlim(0, size-1)
        self.ax.set_ylim(0, size-1)
        self.ax.set_zlim(0, size-1)

        # Optional: fix the box aspect ratio so it looks cubic
        self.ax.set_box_aspect([size, size, size])

        plt.draw()  # update the figure
        plt.pause(0.01)  # small pause to allow the GUI to update