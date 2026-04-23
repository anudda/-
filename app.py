import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="🌸 서연이의 소중한 첫 번째 생일 파티에 초대합니다 🌸", 
    page_icon="👶",
    layout="centered"
)

# 2. 스타일 및 애니메이션 (에러 방지를 위해 f-string을 제거하고 안전하게 작성)
st.markdown("""
    <style>
    /* 배경색 및 출처 숨기기 */
    .stApp { background-color: #fffaf0 !important; }
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    header {visibility: hidden !important;}
    
    /* 모든 글자색 고정 */
    h1, h2, h3, p, span, b, div {
        color: #5d4037 !important;
    }

    /* 정보 박스 스타일 */
    .info-box {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 20px;
    }

    /* 버튼 색상 커스텀: 첫 번째(카카오-노랑), 두 번째(네이버-초록) */
    div[data-testid="column"]:nth-of-type(1) div.stLinkButton a {
        background-color: #FEE500 !important;
        color: #3C1E1E !important;
        border: none !important;
    }
    div[data-testid="column"]:nth-of-type(2) div.stLinkButton a {
        background-color: #03C75A !important;
        color: white !important;
        border: none !important;
    }

    /* 하트 애니메이션 */
    @keyframes hearts-fall {
        0% { top: -10%; }
        100% { top: 100%; }
    }
    .heart {
        position: fixed;
        top: -10%;
        z-index: 0;
        animation: hearts-fall 10s linear infinite;
        color: #ffb7c5;
        opacity: 0.6;
        font-size: 20px;
        user-select: none;
    }
    </style>
    
    <div class="heart" style="left:10%; animation-delay:0s;">❤</div>
    <div class="heart" style="left:30%; animation-delay:2s;">❤</div>
    <div class="heart" style="left:50%; animation-delay:4s;">❤</div>
    <div class="heart" style="left:70%; animation-delay:6s;">❤</div>
    <div class="heart" style="left:90%; animation-delay:8s;">❤</div>
    """, unsafe_allow_html=True)

# 3. 타이틀
st.markdown("<h1 style='text-align: center;'>서연이의 첫 번째 생일</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>배서연의 돌잔치에 초대합니다</p>", unsafe_allow_html=True)

# 4. 사진 출력 (사용자님이 성공했던 원본 방식 그대로 복구)
st.image("baby.jpg", use_column_width=True)

st.write("---")

# 5. 일정 및 장소 정보
st.markdown("""
    <div class='info-box'>
        <h3>📅 일시</h3>
        <p style='font-size: 1.2rem; font-weight: bold;'>2026년 6월 6일 (토요일)</p>
        <p style='font-size: 1.2rem; font-weight: bold;'>오후 6:00</p>
    </div>
    
    <div class='info-box'>
        <h3>📍 장소</h3>
        <p style='font-size: 1.1rem;'><b>신라 스테이 동탄 카페 (7층)</b></p>
        <p style='font-size: 0.9rem;'>경기도 화성시 노작로 161 7층</p>
    </div>
    """, unsafe_allow_html=True)

# 6. 지도 버튼
col1, col2 = st.columns(2)
with col1:
    st.link_button("카카오맵 보기", "https://kko.to/ZvFmNhulyG", use_container_width=True)
with col2:
    st.link_button("네이버 지도 보기", "https://naver.me/Fuz51F6w", use_container_width=True)

# 7. 하단 안내 (따옴표 오류 완벽 수정)
st.markdown("""
    <p style='text-align: center; font-size: 0.8rem; color: #9e9e9e !important; margin-top: 50px;'>
        주차는 호텔 지하 주차장을 이용해 주세요
    </p>
    """, unsafe_allow_html=True)
