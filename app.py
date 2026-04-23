import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="배서연 돌잔치 초대장", page_icon="👶")

# 2. 스타일 보정 (출처 제거 + 글자색 고정)
st.markdown("""
    <style>
    /* 배경색과 글자색을 강제로 고정 (다크모드 대비) */
    .stApp {
        background-color: #fffaf0 !important;
    }
    
    /* 하단 Streamlit 출처와 상단 메뉴 숨기기 */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}

    /* 모든 텍스트 색상을 진한 갈색으로 고정 */
    h1, h2, h3, p, span, b, div {
        color: #5d4037 !important;
    }

    .title-text {
        text-align: center;
        font-family: 'Nanum Pen Script', cursive;
    }
    
    .info-box {
        background-color: #ffffff !important; /* 박스 배경은 하얀색 */
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* 박스 안의 작은 글씨 색상 조절 */
    .info-box p {
        color: #5d4037 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 헤더 및 타이틀
st.markdown("<h1 class='title-text'>서연이의 첫 번째 생일</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>사랑스러운 서연이의 돌잔치에 초대합니다</p>", unsafe_allow_html=True)

# 3. 대표 사진 (잘 나온다고 하신 방식 그대로 유지)
st.image("baby.jpg", use_container_width=True)

st.write("---")

# 4. 일정 및 장소 정보 (장소 정보 업데이트)
st.markdown("""
    <div class='info-box'>
        <h3>📅 일시</h3>
        <p style='font-size: 1.2rem; font-weight: bold;'>2026년 6월 20일 (토요일)</p>
        <p style='font-size: 1.2rem; font-weight: bold;'>오후 12:00</p>
    </div>
    
    <div class='info-box'>
        <h3>📍 장소</h3>
        <p style='font-size: 1.1rem;'><b>신라 스테이 동탄</b></p>
        <p style='font-size: 0.9rem;'>경기도 화성시 노작로 161</p>
    </div>
    """, unsafe_allow_html=True)

# 5. 지도 연결 버튼 (링크는 그대로 두었으니 필요시 수정하세요)
col1, col2 = st.columns(2)
with col1:
    st.link_button("카카오맵 보기", "https://map.kakao.com", use_container_width=True)
with col2:
    st.link_button("네이버 지도 보기", "https://map.naver.com", use_container_width=True)

# 6. 하단 안내
st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #9e9e9e !important; margin-top: 50px;'>주차는 호텔 지하 주차장을 이용해 주세요 (3시간 무료)</p>", unsafe_allow_html=True)
