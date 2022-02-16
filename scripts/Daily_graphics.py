import matplotlib.pyplot as plt
from functions import *
import os


def obtain_ticks(date: str) -> list:
    dates = []
    for i in range(0, 24):
        hour = str(i).zfill(2)
        hour = pd.to_datetime("{} {}:00".format(date,
                                                hour))
        dates.append(hour)
    return dates


parameters = obtain_parameters()
files = sorted(os.listdir(parameters["path data"]))
dates = [yyyymmdd2yyyy_mm_dd(date) for date in files]
for date, file in zip(dates, files):
    data = read_data(parameters["path data"],
                     file)
    hours = obtain_ticks(date)
    fig, (ax1, ax2) = plt.subplots(2, 1,
                                   sharex=True,
                                   figsize=(8, 6))
    ax1.set_ylim(0, 120)
    ax1.plot(data["PM2.5"],
             label="PM$_{2.5}$",
             color="#99d98c")
    ax1.plot(data["PM10"],
             label="PM$_{10}$",
             color="#1a759f")
    ax1.grid(ls="--")
    ax2.set_ylim(0, 90)
    ax2.plot(data["TEMP"],
             label="Temperatura (°C)",
             color="#6a040f")
    ax2.plot(data["HUMI"],
             label="Humedad",
             color="#03071e")
    ax2.set_xlim(data.index[0],
                 data.index[-1])
    ax2.grid(ls="--")
    ax2.set_xticks(hours,
                   [hour.time().strftime("%H:%M") for hour in hours],
                   rotation=-60)
    ax1.set_title("Fecha {}".format(date))
    fig.legend(ncol=4,
               frameon=False,
               bbox_to_anchor=(0.72, 0.445, 0.1, 0.1))
    plt.tight_layout(pad=2)
    plt.savefig("{}{}.png".format(parameters["path graphics"],
                                  date))
