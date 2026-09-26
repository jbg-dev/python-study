import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

df = pd.read_csv('student.csv')

# 결측치 확인
print(df.isna().sum())

# 각 과목별 평균
print(df['Python'].mean())
print(df['SQL'].mean())
print(df['알고리즘'].mean())

# 학생별 평균
df['평균'] = df[['Python','알고리즘','SQL']].mean(axis=1)

# 각 과목별 평균점수
subject_mean = df[["Python", "SQL", "알고리즘"]].mean()
plt.bar(subject_mean.index,subject_mean.values)
plt.xlabel("과목")
plt.ylabel("평균 점수")
plt.title("과목별 평균 점수")
plt.show()

# 학생별 평균점수
plt.bar(df["이름"], df["평균"])
plt.xlabel("학생")
plt.ylabel("평균 점수")
plt.title("학생별 평균 점수")
plt.show()

# Python과 SQL의 산점도 및 상관관계
plt.scatter(df["Python"], df["SQL"])
plt.xlabel("Python 점수")
plt.ylabel("SQL 점수")
plt.title("Python과 SQL 점수의 관계")
plt.show()

correlation = df["Python"].corr(df["SQL"])
print("Python과 SQL의 상관계수:", correlation)
