from freqtrade.strategy import IStrategy
import talib.abstract as ta
import pandas as pd

class MyStrategy(IStrategy):
    timeframe = '5m'

    def populate_indicators(self, dataframe: pd.DataFrame, metadata: dict) -> pd.DataFrame:
        dataframe['ema'] = ta.EMA(dataframe['close'], timeperiod=20)
        dataframe['rsi'] = ta.RSI(dataframe['close'], timeperiod=14)
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