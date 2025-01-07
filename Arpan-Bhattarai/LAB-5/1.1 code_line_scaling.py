import numpy as np
import matplotlib.pyplot as plt

def bresenham_line():
    # Input the points
    x0 = int(input("Enter the point x0: "))
    y0 = int(input("Enter the point y0: "))
    x1 = int(input("Enter the point x1: "))
    y1 = int(input("Enter the point y1: "))

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x1 > x0 else -1
    sy = 1 if y1 > y0 else -1

    xes = [x0]
    yes = [y0]

    if dx > dy:
        p = 2 * dy - dx
        while x0 != x1:
            x0 = x0 + sx
            if p >= 0:
                y0 = y0 + sy
                p = p + 2 * (dy - dx)
            else:
                p = p + 2 * dy
            xes.append(x0)
            yes.append(y0)
    else:
        p = 2 * dx - dy
        while y0 != y1:
            y0 = y0 + sy
            if p >= 0:
                x0 = x0 + sx
                p = p + 2 * (dx - dy)
            else:
                p = p + 2 * dx
            xes.append(x0)
            yes.append(y0)

    return xes, yes

def apply_2d_transformation(x_coords, y_coords, transformation_matrix):
    # Convert points to homogeneous coordinates
    points = np.vstack([x_coords, y_coords, np.ones_like(x_coords)])

    # Apply transformation matrix
    transformed_points = transformation_matrix @ points

    return transformed_points[0], transformed_points[1]

def plot_line_with_transformations():
    # Generate original line points
    x_orig, y_orig = bresenham_line()

    # Define transformation matrices
    # 1. Scaling Matrix (scale x by 2, y by 0.5)
    scaling_matrix = np.array([
        [2, 0, 0],
        [0, 0.5, 0],
        [0, 0, 1]
    ])

    # 2. Translation Matrix (translate by 3 units right and 2 units up)
    translation_matrix = np.array([
        [1, 0, 3],
        [0, 1, 2],
        [0, 0, 1]
    ])

    # Composite Transformation Matrix (Scaling * Translation)
    composite_matrix = scaling_matrix @ translation_matrix

    # Apply transformations
    x_transformed, y_transformed = apply_2d_transformation(x_orig, y_orig, composite_matrix)

    # Plot original and transformed lines
    plt.figure(figsize=(8, 6))

    # Original line
    plt.plot(x_orig, y_orig, marker='*', color='blue', linestyle='-', label='Original Line')

    # Transformed line
    plt.plot(x_transformed, y_transformed, color='red', linestyle='--', label='Transformed Line')

    # Plot settings
    plt.title("Bresenham Line with 2D Transformations")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    plt.show()

# Example Usage
plot_line_with_transformations()