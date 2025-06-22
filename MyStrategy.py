from freqtrade.strategy import IStrategy
import pandas_ta as ta
import pandas as pd

class MyStrategy(IStrategy):
    timeframe = '5m'

    def populate_indicators(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        dataframe['ema'] = ta.ema(dataframe['close'], length=20)
        dataframe['rsi'] = ta.rsi(dataframe['close'], length=14)
        return dataframe

    def populate_buy_trend(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        dataframe.loc[
            (dataframe['close'] > dataframe['ema']) &
            (dataframe['rsi'] < 30),
            'buy'] = 1
        return dataframe

    def populate_sell_trend(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        dataframe.loc[
            (dataframe['close'] < dataframe['ema']) &
            (dataframe['rsi'] > 70),
            'sell'] = 1
        return dataframe
