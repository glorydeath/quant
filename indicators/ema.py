
class EMA:

    def get_ema(self, data, span):
        ema = data.ewm(span=span, adjust=False).mean()
        return ema