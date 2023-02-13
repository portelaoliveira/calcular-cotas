import numpy as np
import matplotlib.pyplot as plt


def calculate_intermediate_elevation(
    elevation_data, spacing, calculation_type="horizontal"
):
    """
    Calculates the intermediate elevations based on the input elevation data and desired spacing.

    Parameters:
    elevation_data (list): The elevation data for the measured points.
    spacing (float): The desired spacing between the intermediate points.
    calculation_type (str): The type of calculation to use, either 'horizontal' or 'topographic'.

    Returns:
    intermediate_elevations (list): The calculated elevations for the intermediate points.
    """
    x = np.arange(
        0, len(elevation_data) * 100, 100
    )  # The x-coordinates of the measured points
    y = np.array(elevation_data)  # The y-coordinates of the measured points

    if calculation_type == "horizontal":
        # Calculate a horizontal projection
        x_intermediate = np.arange(0, len(elevation_data) * 100, spacing)
        y_intermediate = np.interp(x_intermediate, x, y)
    else:
        # Calculate a topographic projection
        x_intermediate = np.arange(0, len(elevation_data) * 100, spacing)
        f = np.polyfit(x, y, len(elevation_data) - 1)
        y_intermediate = np.polyval(f, x_intermediate)

    intermediate_elevations = y_intermediate.tolist()

    return intermediate_elevations


def save_output(intermediate_elevations, output_file):
    """
    Saves the calculated intermediate elevations to a file.

    Parameters:
    intermediate_elevations (list): The calculated elevations for the intermediate points.
    output_file (str): The name of the output file to save the data to.
    """
    with open(output_file, "w") as f:
        f.write("Position (m), Elevation (m)\n")
        for i, elevation in enumerate(intermediate_elevations):
            f.write("{}, {}\n".format(i * spacing, elevation))


def plot_elevations(elevation_data, intermediate_elevations, calculation_type):
    """
    Plots the original elevation data and the calculated intermediate elevations for comparison.

    Parameters:
    elevation_data (list): The elevation data for the measured points.
    intermediate_elevations (list): The calculated elevations for the intermediate points.
    calculation_type (str): The type of calculation used to generate the intermediate elevations.
    """
    x = np.arange(
        0, len(elevation_data) * 100, 100
    )  # The x-coordinates of the measured points
    y = np.array(elevation_data)  # The y-coordinates of the measured points

    x_intermediate
