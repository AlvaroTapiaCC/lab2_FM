import matplotlib.pyplot as plt
import numpy as np

def read_file(filename):
    with open(filename, "r") as data:
        lines = []
        for line in data:
            linea = line.strip()
            linea = linea[:-1]
            linea = linea[:-1]
            linea = linea.replace("NaN", str(0))
            linea = linea.split(",")
            lines.append(linea)
    return lines

def usefull_lines(x_value, lines):
    first_line = 4 + (x_value * 29)
    last_line = first_line + 28
    u_lines = []
    for i in range(first_line, last_line):
        u_lines.append(lines[i])
    return u_lines

def theoretical_velocity_profile(y, u_avg, R):
    u_max = 2 * u_avg
    return u_max * (1 - (y**2 / R**2))

def theoretical_shear_stress(y, u_avg, R, mu):
    u_max = 2 * u_avg
    return (mu * -1) * (2*u_max *(y / R**2))

def velocity_profile(block, filename):
    u = []
    ulines = usefull_lines(block, read_file(filename))
    for j in ulines:
        u.append(j[2])
    for i in range(len(u)):
        u[i] = float(u[i])
    return u

def get_avg_velocity(block, file_list):
    avg_vel_prof = []
    velocities = []
    for i in file_list:
        velocities.append(velocity_profile(block, i))
    for j in range(len(velocities[0])):
        index_sum = sum(lst[j] for lst in velocities)
        avg_vel_prof.append(index_sum / len(file_list))
    return avg_vel_prof

def get_y_values(block, filename):
    ulines = usefull_lines(block, read_file(filename))
    y = []
    for line in ulines:
        y.append(line[1])
    for i in range(len(y)):
        y[i] = float(y[i])
    return y

def plot_velocity_profile(block, file_list):
    u = get_avg_velocity(block, file_list)
    y = get_y_values(block, file_list[0])
    u_avg = np.nanmean(u)
    u_arr = np.array(u)
    y_arr = np.array(y)
    velocity_theory = theoretical_velocity_profile(y_arr, u_avg, 0.053)
    plt.plot(y_arr, u_arr)
    plt.plot(y, velocity_theory)
    plt.ylim(0, -0.35)
    plt.xlim(0, 0.06)
    plt.xlabel("y position")
    plt.xticks(rotation = 90)
    plt.ylabel("velocity")
    plt.title("VELOCITY PROFILE")    
    plt.show()

def plot_shear_stress_profile(block, file_list):
    u = get_avg_velocity(block, file_list)
    y = get_y_values(block, file_list[0])
    u_avg = np.nanmean(u)
    u_arr = np.array(u)
    y_arr = np.array(y)
    dU_dy = np.gradient(u_arr, y_arr)
    exp_tau = -0.001 * dU_dy
    theo_tau = theoretical_shear_stress(y_arr, u_avg, 0.053, 0.001)
    plt.plot(y_arr, exp_tau)
    plt.plot(y_arr, theo_tau)
    #plt.ylim(0, 0.014)
    #plt.xlim(0, 0.06)
    plt.xlabel("y position")
    plt.xticks(rotation = 90)
    plt.ylabel("shear stress")
    plt.title("SHEAR STRESS PROFILE")    
    plt.show()
 
archivos = ["PIVlab0.txt","PIVlab1.txt","PIVlab2.txt","PIVlab3.txt","PIVlab4.txt","PIVlab5.txt","PIVlab6.txt",
            "PIVlab7.txt","PIVlab8.txt","PIVlab9.txt"]

mu = 0.001 #viscosity
q = 0.0015 #flow rate



plot_velocity_profile(0, archivos)
plot_shear_stress_profile(0, archivos)