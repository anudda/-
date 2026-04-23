import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="배서연 돌잔치 초대장", page_icon="👶")

# 커스텀 CSS (글자색 강제 지정 및 군더더기 제거)
st.markdown("""
    <style>
    /* 배경색 전체 적용 */
    .stApp {
        background-color: #fffaf0 !important;
    }

    /* 하단 로고, 상단 메뉴, 헤더 숨기기 */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}

    /* 제목 스타일 */
    .title-text {
        text-align: center;
        color: #5d4037 !important; /* 진한 갈색 */
        margin-bottom: 5px;
    }
    
    /* 부제목 스타일 */
    .sub-text {
        text-align: center;
        color: #8d6e63 !important;
        margin-bottom: 20px;
    }

    /* 정보 박스 내부 글자색 강제 지정 (흰 배경에 검은 글씨) */
    .info-box {
        background-color: #ffffff !important;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* 박스 안의 모든 텍스트를 검은색 계열로 고정 */
    .info-box h3, .info-box p, .info-box b {
        color: #333333 !important;
    }

    /* 하단 안내 문구 */
    .footer-note {
        text-align: center;
        font-size: 0.8rem;
        color: #9e9e9e !important;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 헤더 및 타이틀
st.markdown("<h1 class='title-text'>서연이의 첫 번째 생일</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>배서연의 돌잔치에 초대합니다</p>", unsafe_allow_html=True)

# 3. 대표 사진 (파일명 대소문자 확인 필수!)
try:
    st.image("baby.jpg", use_column_width=True)
except:
    st.error("이미지 파일(baby.jpg)을 찾을 수 없습니다. 파일명을 확인해 주세요.")

st.write("---")

# 4. 일정 및 장소 정보
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

# 5. 지도 연결
