from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0, 10, 0.5)
amplitude = np.sin(time)
# print(f"time:{time}")
# print(f"amplitude:{amplitude}")

f = CubicSpline(time, amplitude, bc_type="natural")
# print(f"CubicSpline:{f}")
x_new = time
y_new = f(x_new)
# print(f"CubicSpline_y_new:{y_new}")
print(f"CubicSpline_x_new:{x_new}")

plt.figure(figsize=(8, 4))
plt.plot(x_new, y_new, "b--")

plt.plot(time, amplitude, "ro")

plt.title("Cubic Spline Interpolation")
plt.xlabel("Time")
plt.ylabel("Amplitude = sin(time)")

plt.show()
