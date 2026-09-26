import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"

data = {
    "온도": [20, 22, 24, 26, 28, 30, 32],
    "센서출력": [101, 108, 115, 121, 130, 138, 145]
}

df = pd.DataFrame(data)

# 산점도
plt.scatter(df["온도"], df["센서출력"])

plt.xlabel("온도")
plt.ylabel("센서 출력값")
plt.title("온도와 센서 출력값의 관계")

plt.show()

# 상관계수
correlation = df["온도"].corr(df["센서출력"])

print("상관계수:", correlation)