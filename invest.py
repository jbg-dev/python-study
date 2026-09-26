import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
# 1. Apple 주가 데이터 조회
aapl = yf.download(
    "AAPL",
    period="5y",
    interval="1d",
    auto_adjust=True,
    multi_level_index=False,
    progress=False,
)
if aapl.empty:
    raise RuntimeError(
        "AAPL 데이터를 받지 못했습니다. 잠시 후 다시 실행하세요."
    )
aapl = aapl.sort_index()
aapl = aapl.loc[
    ~aapl.index.duplicated()
].copy()
# 2. 일일 수익률과 이동평균 계산
aapl["return_1d"] = aapl["Close"].pct_change(
    fill_method=None
)
aapl["MA20"] = aapl["Close"].rolling(20).mean()
aapl["MA60"] = aapl["Close"].rolling(60).mean()
# 3. 매매 신호 생성
aapl["signal"] = (
    aapl["MA20"] > aapl["MA60"]
).astype(int)
# 종가로 만든 신호를 다음 거래일부터 적용
aapl["position"] = (
    aapl["signal"].shift(1).fillna(0)
)
# 4. 매수·매도 발생 시점
aapl["position_change"] = (
    aapl["position"].diff().fillna(0)
)
aapl["buy"] = aapl["position_change"] == 1
aapl["sell"] = aapl["position_change"] == -1
# 5. 거래비용을 반영한 전략 수익률
fee_rate = 0.001
aapl["trade"] = aapl[
    "position_change"
    ].abs()
aapl["strategy_return"] = (
    aapl["position"] * aapl["return_1d"]
    - aapl["trade"] * fee_rate
)
# 6. 누적 자산 계산
aapl["buy_hold_equity"] = (
    1 + aapl["return_1d"].fillna(0)
).cumprod()
aapl["strategy_equity"] = (
    1 + aapl["strategy_return"].fillna(0)
).cumprod()
# 7. 결과 출력
buy_hold_return = (
    aapl["buy_hold_equity"].iloc[-1] - 1
)
strategy_return = (
    aapl["strategy_equity"].iloc[-1] - 1
)
trade_count = int(
    aapl["trade"].sum()
)
print(f"단순 보유 수익률: {buy_hold_return:.2%}")
print(f"이동평균 전략 수익률: {strategy_return:.2%}")
print(f"포지션 변경 횟수: {trade_count}회")
# 8. 가격과 매수·매도 시점 표시
fig, axes = plt.subplots(
    2,
    1,
    figsize=(11, 9),
    sharex=True,
)
aapl["Close"].plot(
    ax=axes[0],
    color="black",
    label="Close",
)
aapl["MA20"].plot(
    ax=axes[0],
    color="royalblue",
    label="MA20",
)
aapl["MA60"].plot(
    ax=axes[0],
    color="orange",
    label="MA60",
)
axes[0].scatter(
    aapl.index[aapl["buy"]],
    aapl.loc[aapl["buy"], "Close"],
    marker="^",
    color="green",
        s=70,
    label="Buy",
)
axes[0].scatter(
    aapl.index[aapl["sell"]],
    aapl.loc[aapl["sell"], "Close"],
    marker="v",
    color="red",
    s=70,
    label="Sell",
)
axes[0].set_title("AAPL Moving Average Strategy")
axes[0].set_ylabel("Price (USD)")
axes[0].legend()
axes[0].grid(alpha=0.3)
# 9. 누적 자산 비교
aapl[[
    "buy_hold_equity",
    "strategy_equity",
]].plot(
    ax=axes[1]
)
axes[1].set_title("Equity Curve")
axes[1].set_xlabel("Date")
axes[1].set_ylabel("Growth of $1")
axes[1].grid(alpha=0.3)
plt.tight_layout()
plt.show()