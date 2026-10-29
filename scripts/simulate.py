"""Simulate noisy linear data from the parameters in data/params.json."""

import json

import numpy as np

with open("data/params.json") as f:
    params = json.load(f)
rng = np.random.default_rng(params["seed"])
x = np.linspace(0, 10, params["n"])
y = (
    params["slope"] * x
    + params["intercept"]
    + rng.normal(0, params["noise"], params["n"])
)
np.savetxt("data/raw.csv", np.column_stack([x, y]), delimiter=",", header="x,y")
