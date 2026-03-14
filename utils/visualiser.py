import matplotlib
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import List
from core.board import Board
import numpy as np

class Visualiser:
    def __init__(self):
        plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def plot_board(self, board: Board):
        size = board.size
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

                    # Correct mapping: X/Z on floor, Y vertical
                    xs.append(x)      # X-axis left-right
                    ys.append(z)      # Z-axis (floor depth)
                    zs.append(y)      # Y-axis vertical height

                    colors.append("red" if val == 1 else "blue")

        xs = np.array(xs, dtype=float) # type: ignore
        ys = np.array(ys, dtype=float) # type: ignore
        zs = np.array(zs, dtype=float) # type: ignore

        self.ax.scatter(xs, ys, zs, c=colors, s=200)  # type: ignore

        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Z (Floor depth)")
        self.ax.set_zlabel("Y (Height)")

        self.ax.set_xlim(0, size-1)
        self.ax.set_ylim(0, size-1)
        self.ax.set_zlim(0, size-1)

        self.ax.set_box_aspect([size, size, size])

        plt.draw()
        plt.pause(0.01)