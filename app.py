import streamlit as st
import pandas as pd 

# 제목
st.title("📈 방문자 수 대시보드")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("visitors_sample.csv", parse_dates=["날짜"])

df = load_data()

# 요약 지표
st.metric("총 방문자 수", f"{df['방문자수'].sum():,}명")
st.metric("총 페이지뷰", f"{df['페이지뷰'].sum():,}회")

# 꺾은선 그래프: 방문자수
st.subheader("일자별 방문자 수")
fig, ax = plt.subplots()
ax.plot(df["날짜"], df["방문자수"], marker="o")
ax.set_ylabel("방문자수")
ax.set_xlabel("날짜")
plt.xticks(rotation=45)
st.pyplot(fig)

# 꺾은선 그래프: 페이지뷰
st.subheader("일자별 페이지뷰")
st.line_chart(df.set_index("날짜")["페이지뷰"])
