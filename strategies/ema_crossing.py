import pandas as pd
import matplotlib.pyplot as plt

from indicators.ema import EMA

class EMA_Crossing:

    def get_transaction_point(self, data, data_open, span1, span2):
        ema = EMA()
        ema_span1 = ema.get_ema(data, span1)
        ema_span2 = ema.get_ema(data, span2)
        df = pd.DataFrame(
            {'date': ema_span1.index, 'ema_' + str(span1): ema_span1.values, 'ema_' + str(span2): ema_span2.values})
        df.set_index('date', inplace=True, drop=True)
        df.index = pd.to_datetime(df.index)
        df.plot()
        plt.show()
        print(df)