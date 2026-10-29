"""Fit a line to noisy data, writing metrics, a figure, and a table."""

import json
import os

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

x, y = np.loadtxt("data/raw.csv", delimiter=",", unpack=True)
offset = np.loadtxt(
    "data/calibration.csv", delimiter=",", skiprows=1, usecols=1
).mean()
y = y - offset
n = len(x)
slope, intercept = np.polyfit(x, y, 1)
pred = slope * x + intercept
rmse = float(np.sqrt(np.mean((y - pred) ** 2)))
r2 = float(1 - np.sum((y - pred) ** 2) / np.sum((y - y.mean()) ** 2))
os.makedirs("results", exist_ok=True)
with open("results/fit.json", "w") as f:
    json.dump(
        {
            "n_samples": n,
            "rmse": rmse,
            "r2": r2,
            "fit": {"slope": float(slope), "intercept": float(intercept)},
        },
        f,
        indent=2,
    )
os.makedirs("figures", exist_ok=True)
fig, ax = plt.subplots(figsize=(5, 3.5))
ax.scatter(x, y, s=8, alpha=0.5, label="Data")
ax.plot(x, pred, color="C1", label=f"Fit (slope {slope:.2f})")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
fig.tight_layout()
fig.savefig("figures/fit.png", dpi=150)
os.makedirs("tables", exist_ok=True)
with open("tables/fit.tex", "w") as f:
    f.write("\\begin{tabular}{lr}\n\\hline\nQuantity & Value \\\\\n\\hline\n")
    f.write(f"Slope & {slope:.3f} \\\\\n")
    f.write(f"Intercept & {intercept:.3f} \\\\\n")
    f.write(f"RMSE & {rmse:.3f} \\\\\n")
    f.write(f"$R^2$ & {r2:.3f} \\\\\n")
    f.write("\\hline\n\\end{tabular}\n")
