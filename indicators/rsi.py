import pandas as pd
import numpy as np

class RSI:

    def get_rsi(self, data, period):
        diff = data.diff(1).dropna()
        up_chg = diff * 0
        down_chg = diff * 0
        up_chg[diff > 0] = diff[diff > 0]
        down_chg[diff < 0] = diff[diff < 0]

        up_chg_avg = up_chg.ewm(com=period - 1, min_periods=period).mean()
        down_chg_avg = down_chg.ewm(com=period - 1, min_periods=period).mean()

        rs = abs(up_chg_avg/down_chg_avg)
        rsi = 100 - 100 / (1 + rs)

        return rsi