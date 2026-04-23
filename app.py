import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="배서연 돌잔치 초대장", page_icon="👶")

# 2. 스타일 포장지 (출처 숨기기 + 글자색 고정)
# 사용자님이 잘 된다고 한 코드의 '앞'에 들어가는 부분입니다.
st.markdown("""
    <style>
    .stApp { background-color: #fffaf0 !important; }
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    header {visibility: hidden !important;}
    
    /* 모든 글자색을 강제로 고정 */
    h1, h2, h3, p, span, b, div {
        color: #5d4037 !important;
    }
    .info-box {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 여기서부터는 사용자님이 "잘 나온다"고 하신 코드와 100% 동일한 구조입니다 ---

# 타이틀
st.markdown("<h1 style='text-align: center;'>서연이의 첫 번째 생일</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>배서연의 돌잔치에 초대합니다</p>", unsafe_allow_html=True)

# ★ 사용자님이 잘 나온다고 확인해주신 그 코드 그대로 ★
st.image("baby.jpg", use_column_width=True)

st.write("---")

# 정보 박스
st.markdown("""
    <div class='info-box'>
        <h3>📅 일시</h3>
        <p style='font-size: 1.2rem;'>2026년 6월 20일 (토요일)</p>
        <p style='font-size: 1.2rem;'>오후 12:00</p>
    </div>
    <div class='info-box'>
        <h3>📍 장소</h3>
        <p style='font-size: 1.1rem;'><b>신라 스테이 동탄</b></p>
        <p style='font-size: 0.9rem;'>경기도 화성시 노작로 161</p>
    </div>
    """, unsafe_allow_html=True)

# 지도 버튼
col1, col2 = st.columns(2)
with col1:
    st.link_button("카카오맵 보기", "https://map.kakao.com", use_container_width=True)
with col2:
    st.link_button("네이버 지도 보기", "https://map.naver.com", use_container_width=True)

st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #9e9e9e !important; margin-top: 50px;'>주차는 호텔 지하 주차장을 이용해 주세요 (3시간 무료)</p>", unsafe_allow_html=True)
