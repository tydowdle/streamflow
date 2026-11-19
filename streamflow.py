# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def load_streamflow(filename):
    """Read the streamflow CSV and return its dates and 2D array of gauge flows."""
    data_provo = np.genfromtxt(
        filename,
        delimiter=",",
        skip_header=1,
        dtype=str,
    )
    dates = [
        datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        for date in data_provo[:, 0]
    ]
    flows = data_provo[:, 1:6].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge with the Matplotlib homework formatting."""
    plt.figure(figsize=(11, 5))
    for column, site in enumerate(sites):
        plt.plot(dates, flows[:, column], label=f"Site {site}")

    plt.title("Provo River Streamflow Rates - June 2021")
    plt.xlabel("Date")
    plt.ylabel("Streamflow Rate (cfs)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
