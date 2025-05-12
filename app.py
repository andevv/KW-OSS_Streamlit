import streamlit as st

st.title("2025_OSS_HW2_퀴즈")

st.header("1. 객관식 퀴즈")
st.write("다음 중 먹어선 안되는 때를 고르시오.")
options = ["아침", "점심", "저녁", "야식"]
mc_answer = st.radio("선택하세요:", options)

if st.button("객관식 제출"):
    if mc_answer == "야식":
        st.success("정답입니다!")
    else:
        st.error("오답입니다. 다시 생각해보세요!")

st.markdown("---")

st.header("2. 주관식 퀴즈")
st.write("오픈소스소프트웨어 과목이 열리는 과의 이름은?")
subjective_answer = st.text_input("정답을 입력하세요:")

if st.button("주관식 제출"):
    if subjective_answer.strip().lower() == "정보융합학부":
        st.success("정답입니다!")
    else:
        st.error("오답입니다. '정보융합학부'입니다.")

