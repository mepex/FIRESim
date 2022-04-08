import numpy as np

from FIRESimRun import FIRESimRun
import matplotlib.pyplot as plt


class FIRESim:

    runs = []
    done = False
    failure_rate = 0.0
    horizon = 0
    horizon_padding = 0
    # stats for each year
    min = []
    max = []
    avg = []
    std = []

    def __init__(self, portfolio, market, run_count=100):
        self.horizon = portfolio["horizon"]
        self.horizon_padding = market["horizon_padding"]
        array_size = self.horizon + self.horizon_padding
        self.min = np.full(array_size, 1e8)
        self.max = np.zeros(array_size)
        self.avg = np.zeros(array_size)
        self.std = np.zeros(array_size)
        for i in range(run_count):
            r = FIRESimRun(portfolio, market, i)
            self.runs.append(r)

    def run(self, log=True):
        failure = 0
        for r in self.runs:
            if log:
                print(f"\nRun # {r.run_number}")
            r.run(log)
            if r.fail:
                failure = failure + 1
        self.failure_rate = failure / len(self.runs)
        self.compute_stats()
        self.done = True

    def compute_stats(self):
        for i in range(self.horizon + self.horizon_padding):
            vert_vals = np.zeros(len(self.runs))
            for r in self.runs:
                vert_vals[i] = r.value[i]
            self.max[i] = vert_vals.max()
            self.min[i] = vert_vals.min()
            self.avg[i] = vert_vals.mean()
            self.std[i] = vert_vals.std()

    def get_failure_rate(self):
        return self.failure_rate

    def get_value_plot(self):
        for r in self.runs:
            plt.plot(range(self.horizon + self.horizon_padding), r.value)
        max_max = self.max.max()
        min_min = self.min.min()
        max_y = round(max_max / 1000000) * 1000000
        min_y = round(min_min / 1000000) * 1000000
        ticks = list(range(min_y, max_y, 5000000))
        labels = map(lambda x: x / 1000000, ticks)
        plt.yticks(ticks, labels)
        plt.title(f"FIRE failure rate {self.get_failure_rate() * 100:.2f}%")
        return plt

    def get_stats_plot(self):
        plt.plot(range(self.horizon + self.horizon_padding), self.avg)
        plt.plot(range(self.horizon + self.horizon_padding), self.max)
        plt.plot(range(self.horizon + self.horizon_padding), self.min)
        return plt


