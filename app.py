import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="🌸 서연이의 첫 번째 생일 파티에 초대합니다 🌸", 
    page_icon="👶",
    layout="centered"
)

# 2. 스타일 설정 (예쁜 폰트 + 화사한 색상 + 애니메이션)
st.markdown("""
    <style>
    /* 구글 폰트에서 '나눔펜글씨'와 '가나초콜릿' 느낌의 폰트 불러오기 */
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&family=Gamja+Flower&display=swap');

    /* 배경색 설정 */
    .stApp { background-color: #fffaf0 !important; }
    
    /* 출처 숨기기 */
    /* 하단바, 툴팁, 메뉴 버튼 모두 숨기기 */
    footer {visibility: hidden !important;}
    #MainMenu {visibility: hidden !important;}
    header {visibility: hidden !important;}
    div[data-testid="stStatusWidget"] {visibility: hidden !important;}

    /* 모바일 하단 여백 및 문구 강제 삭제 */
    .stAppDeployButton {display:none !important;}
    #viewerBadge {display:none !important;}
    
    /* 메인 타이틀 폰트 및 색상 (진한 로즈 핑크) */
    h1 {
        font-family: 'Nanum Pen Script', cursive !important;
        color: #e91e63 !important;
        font-size: 4rem !important;
        text-align: center;
        margin-bottom: 0px;
    }


    /* 본문 및 박스 텍스트 폰트 (감자꽃 폰트) */
    h3, p, span, b, div {
        font-family: 'Gamja Flower', cursive !important;
        color: #8d6e63 !important; /* 부드러운 갈색 */
    }

    /* 정보 박스 스타일 */
    .info-box {
        background-color: #ffffff !important;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 2px 5px 15px rgba(233, 30, 99, 0.1); /* 핑크빛 그림자 */
        text-align: center;
        margin-bottom: 25px;
        border: 1px solid #fce4ec;
    }

    /* 버튼 색상 커스텀 (카카오-네이버) */
    div[data-testid="column"]:nth-of-type(1) div.stLinkButton a {
        background-color: #FEE500 !important;
        color: #3C1E1E !important;
        border: none !important;
        font-family: 'Gamja Flower', cursive !important;
        font-size: 1.2rem !important;
    }
    div[data-testid="column"]:nth-of-type(2) div.stLinkButton a {
        background-color: #03C75A !important;
        color: white !important;
        border: none !important;
        font-family: 'Gamja Flower', cursive !important;
        font-size: 1.2rem !important;
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
        font-size: 25px;
        user-select: none;
    }
    </style>
    
    <div class="heart" style="left:10%; animation-delay:0s;">❤</div>
    <div class="heart" style="left:30%; animation-delay:2s;">🌸</div>
    <div class="heart" style="left:50%; animation-delay:4s;">✨</div>
    <div class="heart" style="left:70%; animation-delay:6s;">💕</div>
    <div class="heart" style="left:90%; animation-delay:8s;">🧸</div>
    """, unsafe_allow_html=True)

# 3. 타이틀 및 문구 (이모티콘 추가)
st.markdown("<h1 style='text-align: center;'>배서연의<br>첫 생일 🎂</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.5rem;'>서연이의 돌잔치에 초대합니다 🌸</p>", unsafe_allow_html=True)

# 4. 사진 또는 동영상 출력 (사용자님이 성공한 방식 유지)
st.video("baby.mp4", autoplay=True, loop=True, muted=True)
# 동영상으로 바꾸려면 위 줄을 지우고 아래 줄 주석(#)을 해제하세요.
# st.video("baby.mp4", loop=True, autoplay=True, muted=True)

st.write("---")

# 5. 일정 및 장소 정보
st.markdown("""
    <div class='info-box'>
        <h3 style='font-size: 1.8rem;'>📅 언제인가요?</h3>
        <p style='font-size: 1.4rem; font-weight: bold;'>2026년 6월 6일 (토요일)</p>
        <p style='font-size: 1.4rem; font-weight: bold;'>저녁 6시 🕕</p>
    </div>
    
    <div class='info-box'>
        <h3 style='font-size: 1.8rem;'>📍 어디인가요?</h3>
        <p style='font-size: 1.3rem;'><b>신라 스테이 동탄 카페 (7층) </b></p>
        <p style='font-size: 1.1rem;'>경기도 화성시 노작로 161 7층</p>
    </div>
""", unsafe_allow_html=True)

# 6. 지도 버튼
col1, col2 = st.columns(2)
with col1:
    st.link_button("💛 카카오맵 보기", "https://kko.to/ZvFmNhulyG", use_container_width=True)
with col2:
    st.link_button("💚 네이버 지도 보기", "https://naver.me/Fuz51F6w", use_container_width=True)

# 7. 하단 안내
st.markdown("""
    <p style='text-align: center; font-size: 1.1rem; color: #9e9e9e !important; margin-top: 50px;'>
        서연이의 첫 생일을 축하해 주셔서 감사합니다! 🙇‍♀️ <br>
        
    </p>
    """, unsafe_allow_html=True)
