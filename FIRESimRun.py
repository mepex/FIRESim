import numpy as np


class FIRESimRun:

    def __init__(self, portfolio, market, run_number):
        self.portfolio = portfolio
        self.market = market
        self.value = [self.portfolio["starting_amount"]]
        self.yearly_returns = [0]
        self.stock_returns = []
        self.bond_returns = []
        self.inflation = [0]
        self.expenses = []
        self.fail = False
        self.run_number = run_number

    def run(self, log=True):
        horizon = self.portfolio["horizon"]
        horizon_padding = self.market["horizon_padding"]
        self.stock_returns = np.random.normal(self.market["stocks_return_avg"], self.market["stocks_return_std"],
                                              horizon + horizon_padding)
        self.bond_returns = np.random.normal(self.market["bonds_return_avg"], self.market["bonds_return_std"],
                                             horizon + horizon_padding)
        self.inflation = np.random.normal(self.market["inflation_avg"], self.market["inflation_std"],
                                          horizon + horizon_padding)
        self.expenses = np.full(horizon + horizon_padding, self.portfolio["yearly_withdrawal"])
        columns = ["Year", "Value", "Expenses", "Return", "Inflation"]
        for c in columns:
            print(f"{c:15}", end='')
        print()
        for i in range(1, horizon + horizon_padding):
            total_returns = self.stock_returns[i] * self.portfolio["stocks_percentage"] + self.bond_returns[i] * \
                            self.portfolio["bonds_percentage"]
            inflation_adjusted_returns = (1 + total_returns) / (1 + self.inflation[i]) - 1
            self.yearly_returns.append(inflation_adjusted_returns)
            self.expenses[i] = (1 + self.inflation[i]) * self.expenses[i - 1]
            nextp = (self.value[i - 1] * (1 + total_returns)) - self.expenses[i]
            self.value.append(nextp)
            if nextp < 0:
                self.fail = True
            print(
                f"{i:2} {self.value[i]:15.2f} {self.expenses[i]:15.2f} {self.yearly_returns[i]:15.3f} {self.inflation[i]:15.3f}")
