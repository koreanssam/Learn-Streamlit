import streamlit as st

# Title 작성
st.title("Select Button 구현")

# 코드 표시
st.subheader("코드")
code = """
import streamlit as st

option = st.selectbox(
    "어떤 과일을 좋아하시나요?",
    ("사과", "바나나", "딸기"),
)

st.write("내 선택:", option)
"""
st.code(code, language="python")

# 구분선
st.divider()

# 코드 실행 결과

value = st.selectbox(
    "어떤 과일을 좋아하시나요?",
    ("사과", "바나나", "딸기"),
)

st.write("내 선택:", value)
