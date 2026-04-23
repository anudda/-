import streamlit as st

# 1. 페이지 설정 (브라우저 탭 제목)
st.set_page_config(page_title="배서연 돌잔치 초대장", page_icon="👶")

# 깔끔한 디자인을 위한 커스텀 CSS
st.markdown("""
    <style>
    .main {
        background-color: #fffaf0; /* 따뜻한 아이보리 배경색 */
    }
    .title-text {
        text-align: center;
        color: #5d4037;
        font-family: 'Nanum Pen Script', cursive;
    }
    .info-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 헤더 및 타이틀
st.markdown("<h1 class='title-text'>서연이의 첫 번째 생일</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8d6e63;'>배서연의 돌잔치에 초대합니다</p>", unsafe_allow_html=True)

# 3. 대표 사진 (이미지 파일명을 본인의 파일명으로 수정하세요)
# 예: 'main_baby.jpg'
st.image("baby.jpg", use_column_width=True)

st.write("---")

# 4. 일정 및 장소 정보
st.markdown("""
    <div class='info-box'>
        <h3 style='color: #5d4037;'>📅 일시</h3>
        <p style='font-size: 1.2rem;'>2026년 6월 20일 (토요일)</p>
        <p style='font-size: 1.2rem;'>오후 12:00</p>
    </div>
    
    <div class='info-box'>
        <h3 style='color: #5d4037;'>📍 장소</h3>
        <p style='font-size: 1.1rem;'><b>그랜드 호텔 3층 라일락홀</b></p>
        <p style='font-size: 0.9rem; color: #757575;'>서울특별시 OO구 OO로 123</p>
    </div>
    """, unsafe_allow_html=True)

# 5. 지도 연결 버튼
col1, col2 = st.columns(2)
with col1:
    st.link_button("카카오맵 보기", "https://map.kakao.com", use_container_width=True)
with col2:
    st.link_button("네이버 지도 보기", "https://map.naver.com", use_container_width=True)

# 6. 하단 안내 (선택사항)
st.markdown("<p style='text-align: center; font-size: 0.8rem; color: #9e9e9e; margin-top: 50px;'>주차는 호텔 지하 주차장을 이용해 주세요 (3시간 무료)</p>", unsafe_allow_html=True)


여기서 어떻게 고치면 되는지 알려줘.
