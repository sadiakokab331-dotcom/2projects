import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
])
plan_a = np.array([
    1000,
    1200,
    1500,
    1400,
    1800,
    2100,
    2500,
    2400,
    2700,
    3000,
    3400,
    3800,
])
plan_b = np.array([
    800,
    1100,
    1300,
    1600,
    1700,
    2000,
    2200,
    2600,
    2800,
    3100,
    3300,
    3900,
])

plt.figure(figsize=(10, 5))
plt.plot(months, plan_a, marker="o", label="Savings Plan A", color="blue")
plt.plot(months, plan_b, marker="s", label="Savings Plan B", color="green")

plt.fill_between(
    months,
    plan_a,
    plan_b,
    color="orange",
    alpha=0.3,
    label="Difference in Savings",
)

plt.title("Monthly Savings Progress Comparison")
plt.xlabel("Months")
plt.ylabel("Savings Amount ($)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()