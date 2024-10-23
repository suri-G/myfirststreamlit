import streamlit as st

st.title("형성평가를 봅시다!")

# option = st.radio("연수 장소는 어디일까요?", ["강남역", "역삼역", "서초역", "교대역", "선릉역"])
# if option=='강남역':
#     st.success("정답입니다!")
#     # st.balloons()
# elif option =="교대역":
#     st.write("엇... 비슷한데... 더 가까운 역이 있어요.")
# elif option =="서초역":
#     st.write("어... 아닐걸요?")
# else:
#     st.error("다시 풀어보세요!")
#     # st.snow()



# option1 = st.selectbox("식사는 맛있으셨나요?", ["매우 불만족", "불만족", "보통", "만족", "매우 만족"])

# agree = st.checkbox("동의하시나요?")

# if agree:
#     st.write("동의하셨군요!")
# else:
#     st.write("동의버튼을 눌러주세요.")

# name = st.text_input("이름을 입력해주세요.")
# if name:
#     st.write(f"{name}님 환영합니다!🤗")

# import streamlit as st

# # 제목
# st.title("형성평가를 봅시다!")

# # 질문 1: 연수 장소 선택
# option = st.radio("연수 장소는 어디일까요?", ["강남역", "역삼역", "서초역", "교대역", "선릉역"])

# # 장소 선택에 따른 피드백
# if option == '강남역':
#     st.success("정답입니다! 🎉")
#     st.balloons()  # 풍선 애니메이션
# elif option == "교대역":
#     st.warning("엇... 비슷한데... 더 가까운 역이 있어요.")
# elif option == "서초역":
#     st.warning("어... 아닐걸요?")
# else:
#     st.error("다시 풀어보세요!")
#     st.snow()  # 오답일 경우 눈 애니메이션

# # 질문 2: 식사 만족도
option1 = st.selectbox("식사는 맛있으셨나요?", ["매우 불만족", "불만족", "보통", "만족", "매우 만족"])

# 만족도 선택에 따른 피드백
if option1 == "매우 만족":
    st.write("아! 다행이에요! 😊")
elif option1 == "만족":
    st.write("만족하셨다니 기뻐요!")
else:
    st.write("다음에 더 노력할게요! 😅")

# 질문 3: 동의 여부
agree = st.checkbox("동의하시나요?")

# 동의 여부에 따른 피드백
if agree:
    st.write("동의하셨군요! 👍")
else:
    st.warning("동의버튼을 눌러주세요.")

# 질문 4: 이름 입력
name = st.text_input("이름을 입력해주세요.")
if name:
    st.write(f"{name}님 환영합니다! 🤗")
else:
    st.error("이름을 입력해 주세요.")

# 추가: 사용자 평가 요약
if name and agree:
    st.subheader("평가 요약")
    st.write(f"{name}님은 '{option}'을(를) 선택하셨고, 식사 만족도는 '{option1}'입니다.")


# import streamlit as st
# import random

# # 앱 제목
# st.title("숫자 맞추기 게임! 🎯")

# # 임의의 숫자 생성 (1~100 사이)
# if 'random_number' not in st.session_state:
#     st.session_state.random_number = random.randint(1, 100)

# if 'attempts' not in st.session_state:
#     st.session_state.attempts = 0

# # 게임 설명
# st.write("1부터 100 사이의 숫자를 맞춰보세요! 😎")

# # 숫자 입력
# guess = st.number_input("숫자를 입력하세요", min_value=1, max_value=100, step=1)

# # 확인 버튼
# if st.button("확인"):
#     st.session_state.attempts += 1  # 시도 횟수 증가
#     if guess < st.session_state.random_number:
#         st.warning("더 큰 숫자를 시도해보세요! 🚀")
#     elif guess > st.session_state.random_number:
#         st.warning("더 작은 숫자를 시도해보세요! 🛬")
#     else:
#         st.success(f"정답입니다! 🎉 {st.session_state.attempts}번 만에 맞추셨어요!")
#         st.balloons()
#         # 게임을 다시 시작할 수 있도록 숫자 초기화
#         if st.button("다시 시작하기"):
#             st.session_state.random_number = random.randint(1, 100)
#             st.session_state.attempts = 0
#             st.experimental_rerun()

# # 시도 횟수 표시
# st.write(f"시도 횟수: {st.session_state.attempts}번")
