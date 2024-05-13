import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from typing import List, Tuple

def model_size_comparison(model_sizes: List[Tuple[str, float]]) -> None:
    """
    Displays a 3D plot comparing the size of different models represented as pyramids.
    
    Args:
        model_sizes: List[Tuple[str, float]]
            A list of tuples, where each tuple contains a model label and its associated volume.
    
    Description:
        Each model's volume is represented by the volume of a pyramid with a square base,
        where the side length of the base and the height are calculated based on the volume.
        The function plots these pyramids side by side for visual comparison and displays the
        volume in scientific notation above each pyramid, along with the model label.
    """
    
    # Define a fixed color palette (can be expanded if more models are used)
    colors = ['skyblue', 'lightgreen', 'salmon', 'gold', 'violet']
    
    def draw_pyramid(ax, base_center, side, height, label, volume, color):
        """Helper function to draw a single pyramid and annotate it with label and volume."""
        x_offset, y_offset = base_center
        vertices = np.array([
            [0 + x_offset, 0 + y_offset, 0],
            [side + x_offset, 0 + y_offset, 0],
            [side + x_offset, side + y_offset, 0],
            [0 + x_offset, side + y_offset, 0],
            [side/2 + x_offset, side/2 + y_offset, height]
        ])
        faces = [
            [vertices[0], vertices[1], vertices[4]],
            [vertices[1], vertices[2], vertices[4]],
            [vertices[2], vertices[3], vertices[4]],
            [vertices[3], vertices[0], vertices[4]],
            [vertices[0], vertices[1], vertices[2], vertices[3]]  # base
        ]
        poly3d = Poly3DCollection(faces, color=color, edgecolor='black', alpha=0.8)
        ax.add_collection3d(poly3d)
        ax.text(vertices[4][0], vertices[4][1], vertices[4][2] + height * 0.1, f'{label} \n ({volume:.1e})', color='black', fontsize=8, ha='center')
        #ax.text(vertices[4][0], vertices[4][1], vertices[4][2] + height * 0.2, f'{volume:.1e}', color='red', fontsize=10, ha='center')

    # Set up plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    max_height = 0
    spacing = 10  # Additional space between pyramids

    # Calculate positions
    positions = []
    current_x = 0
    for i, (label, volume) in enumerate(model_sizes):
        side = (3 * volume) ** (1/3)  # Corrected formula for side length
        height = side
        max_height = max(max_height, height)
        positions.append((current_x, side))
        current_x += side + spacing

    for idx, ((label, volume), (x_offset, side)) in enumerate(zip(model_sizes, positions)):
        height = side
        color = colors[idx % len(colors)]
        draw_pyramid(ax, (x_offset, 0), side, height, label, volume, color)

    # Adjust axis limits and aspect
    ax.set_xlim(0, current_x)
    ax.set_ylim(0, side)
    ax.set_zlim(0, max_height * 1.4)
    ax.set_box_aspect([current_x, side, max_height * 1.4])  # Ensure the aspect ratio is visually accurate

    # Remove axis labels and tick labels for cleaner presentation
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_zlabel('')

    # Set title and layout adjustments
    plt.title("Model Size Comparison")
    plt.tight_layout()  # Adjust layout to prevent cutting off of margin elements

    plt.show()

# Example usage: