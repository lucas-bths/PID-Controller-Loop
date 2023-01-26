import matplotlib.pyplot as plt

# import time

# TODO: Create settings using the time library and make the pid smoother
#  & (give it a time limit instead of error limit)


# Set positions and instantiate initial errors for PID loop
target_position = 100
current_position = [300]
initial_error = target_position - current_position[-1]
error_list = [initial_error, initial_error]


# Instantiate PID constants and starting time
kP = 1
kI = 0.1
kD = 0.1
time_list = [0]


# PID formula that determines change in position (replaced integral with sum of total errors, and derivative with
# consecutive error difference)
def PID(error, kP, kI, kD):
    delta_position = kP * error[-1] + kI * sum(error) + kD * (error[-1] - error[-2])
    return delta_position


# Keep running PID until magnitude of error <= 0.1
plt.ion()
while abs(error_list[-1]) > 0.1:
    # Updates current position axis by appending latest position added with Δposition
    current_position.append(current_position[-1] + PID(error_list, kP, kI, kD))
    # Updates time axis
    time_list.append(sum(time_list) + 0.3)
    # Updates latest error
    error_list.append(target_position - current_position[-1])

    # Matplotlib plot creations
    plt.plot(time_list, current_position)
    plt.title("PID Loop")
    plt.xlabel("Time")
    plt.ylabel("Position")
    plt.show()
    plt.pause(0.3)  # Pauses iteration for 0.3 seconds (could likely use time.sleep(0.3))
    print(error_list[-1])  # Prints current error value
