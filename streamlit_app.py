import streamlit as st

st.title("👋🏻 연수 실습 페이지(1023)")
st.subheader("저의 페이지에 오신 것을 환영합니다!")
st.info("반갑습니다. 반포고등학교 황수빈입니다. 수학을 좋아하고 코딩을 좋아합니다:)")

# 깃허브 페이지 넣기
st.link_button("황수빈의 깃허브 페이지 바로가기", "https://github.com/Surihub")

# st.success("초록색 창")
# st.error("빨간색 창")
# st.info("파란색 창")
# st.warning("노란색 창") # ctrl+/ : 주석처리

st.image("https://media.giphy.com/media/2IudUHdI075HL02Pkk/giphy.gif?cid=790b7611x3uotlioi6qzp7vt8aalxxvdg1rhimafd9wy9jxi&ep=v1_gifs_search&rid=giphy.gif&ct=g", caption="Welcome to coding world") 
st.video("https://www.youtube.com/watch?v=V7QcsrpRZhA")
st.image("data/streamlit.png")