import matplotlib.pyplot as plt
import numpy as np
from step_calc import StepCalc

start_orbit = 1
end_orbit = 512
base_multiplier = 3
number_of_steps = 4

exp_1 = 4
exp_2 = 5

chart_title = f"{base_multiplier} {number_of_steps}-step"

fig, ax = plt.subplots()

orbit_numbers = StepCalc.generate_orbit_numbers(start_orbit, end_orbit)

step_calc = StepCalc(base_multiplier, number_of_steps, orbit_numbers)

step_calc.calc_steps(exp_1)
calc1_x = np.array(step_calc.x)
calc1_y = np.array(step_calc.y)

step_calc.calc_steps(exp_2)
calc2_x = np.array(step_calc.x)
calc2_y = np.array(step_calc.y)

fig, ax = plt.subplots()

ax.plot(
    np.array(orbit_numbers),
    np.array(orbit_numbers),
    zorder=1, label='Loop Line', color='blue', linewidth=1.0)

ax.scatter(
    calc1_x,
    calc1_y,
    zorder=2,
    label=f"{chart_title} 2^{exp_1}", s=0.25, color="red")

ax.scatter(
    calc2_x,
    calc2_y,
    zorder=3,
    label=f"{chart_title} 2^{exp_2}", s=0.25, color="green")

ax.set_xlabel('n')
ax.set_ylabel('(n*m+a)/2^e')
ax.set_title(chart_title)

plt.legend()
plt.savefig(f"images/{StepCalc.calc_filename(step_calc, False)}.svg")

step_calc.write_log(f"{StepCalc.calc_filename(step_calc, False)}")
