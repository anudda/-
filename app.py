import streamlit as st

# 1. 페이지 설정 (브라우저 탭 제목)
st.set_page_config(page_title="배서연의 돌잔치에 초대합니다", page_icon="👶")

# 깔끔한 디자인을 위한 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경색 설정 */
    .stApp {
        background-color: #fffaf0;
    }

    /* 하단 로고 및 메뉴 숨기기 */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}

    /* 일시 및 장소 텍스트 색상 강제 지정 */
    .info-text {
        color: #333333 !important; /* 진한 회색/검정으로 고정 */
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 10px;
    }
    
    /* 타이틀 색상 */
    h1 {
        color: #5d4037 !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 화면에 보여지는 부분 ---

st.title("🎂 00이의 첫 번째 생일")

# 사진 출력
st.image("baby.jpg", use_column_width=True)

# 텍스트 출력 시 위에서 만든 'info-text' 클래스를 사용합니다.
st.markdown("<p class='info-text'>📅 일시: 2026년 6월 20일 오후 12시</p>", unsafe_allow_html=True)
st.markdown("<p class='info-text'>📍 장소: OO컨벤션 2층 웨딩홀</p>", unsafe_allow_html=True)

st.link_button("네이버 지도 보기", "https://naver.me/your_link", use_container_width=True)
