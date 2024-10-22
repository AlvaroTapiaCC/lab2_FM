import numpy as np
import matplotlib.pyplot as plt

# Function to read the .txt file and extract position and velocity data
def read_data(filename):
    # Skip the first 3 lines, then load the rest
    data = np.loadtxt(filename, delimiter=',', skiprows=3, dtype=str)
    
    # Replace 'NaN' with '0' and convert data to float
    data[data == 'NaN'] = '0'
    data = data.astype(float)
    
    return data

# Function to calculate the theoretical velocity profile
def theoretical_velocity_profile(y, u_avg, R):
    u_max = 2 * u_avg
    return u_max * (1 - (y**2 / R**2))

# Function to plot experimental and theoretical velocity profiles
def plot_velocity_profiles(data, block_num, velocity_type='u', R=0.0425):
    # Calculate the starting line of the block
    start_line = block_num * 29
    end_line = start_line + 29

    # Extract the y position and velocity (u or v)
    y = data[start_line:end_line, 1]  # y position
    if velocity_type == 'u':
        velocity_exp = data[start_line:end_line, 2]  # u (axial velocity)
    elif velocity_type == 'v':
        velocity_exp = data[start_line:end_line, 3]  # v (radial velocity)
    print(y)
    # Calculate average velocity from experimental data
    u_avg = np.nanmean(velocity_exp)  # Replace NaN with 0 if necessary before calculating
    # Calculate the theoretical velocity profile
    velocity_theory = theoretical_velocity_profile(y, u_avg, R)

    # Plot the experimental and theoretical velocity profiles
    plt.figure(figsize=(10, 6))
    
    # Experimental velocity profile
    plt.plot(y, velocity_exp, label='Experimental Velocity Profile', color='b', marker='o')
    
    # Theoretical velocity profile
    plt.plot(y, velocity_theory, label='Theoretical Velocity Profile', color='r', linestyle='--')

    # Set labels and title
    plt.xlabel('Y Position [m]')
    plt.ylabel('Velocity [m/s]')
    plt.title(f'Comparison of Experimental and Theoretical Velocity Profiles (Block {block_num})')

    # Set y-axis limits from 0 to -0.4
    plt.ylim(0, -0.4)  # Set limits for y-axis

    # Invert y-axis to have higher velocities at the bottom
    plt.gca().invert_yaxis()  # Invert y-axis
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Reference line at y=0
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage
filename = 'PIVlab0.txt'  # Replace with your actual file path
data = read_data(filename)

# Choose which block to plot (0 for the first block, 1 for the second, etc.)
block_to_plot = 1  # Change this to the desired block number (each block is 28 lines)
plot_velocity_profiles(data, block_to_plot, velocity_type='u')  # 'u' for axial velocity, 'v' for radial velocity
