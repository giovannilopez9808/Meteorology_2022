import matplotlib.pyplot as plt
from functions import *
import os

parameters = obtain_parameters()
parameters["dataset"] = ["PM10", "PM2.5"]
parameters["file graphics"] = "Daily_mean.png"
files = sorted(os.listdir(parameters["path data"]))
dates = [yyyymmdd2yyyy_mm_dd(date) for date in files]
columns = ["mean", "std"]
data = {"PM10": pd.DataFrame(index=dates, columns=columns),
        "PM2.5": pd.DataFrame(index=dates, columns=columns)}

for date, file in zip(dates, files):
    data_per_date = read_data(parameters["path data"],
                              file)
    for column in parameters["dataset"]:
        mean = data_per_date[column].mean()
        std = data_per_date[column].std()
        data[column]["mean"][date] = mean
        data[column]["std"][date] = std
dates = pd.to_datetime(dates)
fig, (ax1, ax2) = plt.subplots(2, 1,
                               sharex=True,
                               figsize=(12, 6))
ax1.errorbar(dates,
             data["PM10"]["mean"],
             data["PM10"]["std"],
             color="#1a759f",
             label="PM$_{10}$",
             fmt='o',
             markersize=8,
             capsize=20)
ax1.set_ylim(0, 40)
ax2.errorbar(dates,
             data["PM2.5"]["mean"],
             data["PM2.5"]["std"],
             color="#40916c",
             label="PM$_{2.5}$",
             fmt='o',
             markersize=5,
             capsize=10)
ax2.set_ylim(0, 24)
ax2.set_yticks([ytick for ytick in range(0, 28, 4)])
fig.legend(ncol=2,
           frameon=False,
           bbox_to_anchor=(0.95, 0.95))
plt.tight_layout()
plt.savefig("{}{}".format(parameters["path graphics"],
                          parameters["file graphics"]))
