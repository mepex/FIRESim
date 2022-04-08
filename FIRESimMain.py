import numpy as np
import matplotlib.pyplot as plt
from FIRESim import FIRESim

# current portfolio + spending info
portfolio = {
    "horizon": 45,
    "starting_amount": 6000000,
    "stocks_percentage": 0.6,
    "bonds_percentage": 0.38,
    "cash_percentage": 0.02,
    "yearly_withdrawal": 180000,
}

# rates of returns and their standard deviations
market = {
    "stocks_return_avg": 0.075,
    "stocks_return_std": 0.08,
    "bonds_return_avg": 0.03,
    "bonds_return_std": 0.01,
    "inflation_avg": 0.02,
    "inflation_std": 0.01,
    "horizon_padding": 15,
}


def main():

    sim = FIRESim(portfolio, market, 1000)
    sim.run(True)
    # for i in range(100):
    #     r = FIRESimRun(portfolio, market)
    #     r.run()
    #     run.append(r)

    plt = sim.get_value_plot()
    plt.show()

    # p = [portfolio]
    # yearly_return = [0]
    # inflation_adj_return = [0]
    # s_returns = np.random.normal(stocks_return_avg, stocks_return_std, horizon + horizon_padding)
    # b_returns = np.random.normal(bonds_return_avg, bonds_return_std, horizon + horizon_padding)
    # inflation = np.random.normal(inflation_avg, inflation_std, horizon + horizon_padding)
    #
    # for i in range(1, horizon + horizon_padding):
    #     r = s_returns[i] * portfolio_stocks_percentage + b_returns[i] * portfolio_bonds_percentage
    #     yearly_return.append(r)
    #     iar = (1 + yearly_return[i])/(1 + inflation[i]) - 1
    #     inflation_adj_return.append(iar)
    #     nextp = (p[i-1] - yearly_withdrawal) * (1 + inflation_adj_return[i])
    #     p.append(nextp)
    #     print(f"Year {i:2}: portfolio: {p[i]:.2f}, return {inflation_adj_return[i]:.3f}")




    # mu, sigma = 0, 0.1  # mean and standard deviation
    # s = np.random.normal(mu, sigma, 1000)
    # count, bins, ignored = plt.hist(s, 30, density=True)
    # plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
    #          np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
    #          linewidth=2, color='r')
    # plt.show()




if __name__ == '__main__':
    main()
    exit(0)
