import pandas as pd

data = {
    "이름": ["철수", "영희", "민수", "지수", "현우"],
    "학과": [
        "전자정보통신공학과",
        "컴퓨터공학과",
        "전자정보통신공학과",
        "전자정보통신공학과",
        "컴퓨터공학과"
    ],
    "Python": [90, 85, None, 95, 80],
    "SQL": [80, 95, 75, None, 85]
}

df = pd.DataFrame(data)
python_mean = df['Python'].mean()
df['Python'] = df["Python"].fillna(python_mean)
SQL_mean = df['SQL'].mean()
df['SQL'] = df["SQL"].fillna(SQL_mean)
df["평균"] = df[["Python", "SQL"]].mean(axis=1)
result = df[df['평균']>=85]
result = result.sort_values('평균',ascending=False)
print(result)
