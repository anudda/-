import streamlit as st

# 1. 페이지 설정 (탭 제목을 길게 해서 Streamlit 글자를 최대한 가립니다)
st.set_page_config(
    page_title="🌸 서연이의 소중한 첫 번째 생일 파티에 초대합니다 🌸", 
    page_icon="👶",
    layout="centered"
)

# 2. 스타일 포장지 (애니메이션 + 버튼 색상 + 출처 숨기기)
st.markdown("""
    <style>
    /* 배경색 설정 */
    .stApp { background-color: #fffaf0 !important; }
    
    /* 하단 출처 및 메뉴 숨기기 */
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

    /* 버튼 색상 커스텀: 카카오(노랑), 네이버(초록) */
    /* 카카오 버튼 (왼쪽) */
    div[data-testid="column"]:nth-of-type(1) div.stLinkButton a {
        background-color: #FEE500 !important;
        color: #3C1E1E !important;
        border: none !important;
    }
    /* 네이버 버튼 (오른쪽) */
    div[data-testid="column"]:nth-of-type(2) div.stLinkButton a {
        background-color: #03C75A !important;
        color: white !important;
        border: none !important;
    }

    /* 하트 애니메이션 설정 */
    @keyframes hearts-fall {
        0% { top: -10%; }
        100% { top: 100%; }
    }
    @keyframes hearts-shake {
        0%, 100% { transform: translateX(0); }
        50% { transform: translateX(80px); }
    }
    .heart {
        position: fixed;
        top: -10%;
        z-index: 0; /* 배경보다 위, 콘텐츠보다 아래 */
        user-select: none;
        cursor: default;
        animation: hearts-fall 10s linear infinite, hearts-shake 3s ease-in-out infinite;
        color: #ffb7c5; /* 연분홍색 */
        opacity: 0.6;
        font-size: 20px;
    }
    /* 하트들 위치 분산 */
    .heart:nth-of-type(1) { left: 10%; animation-delay: 0s, 0s; }
    .heart:nth-of-type(2) { left: 25%; animation-delay: 1s, 1s; }
    .heart:nth-of-type(3) { left: 40%; animation-delay: 6s, 0.5s; }
    .heart:nth-of-type(4) { left: 55%; animation-delay: 4s, 2s; }
    .heart:nth-of-type(5) { left: 70%; animation-delay: 2s, 2s; }
    .heart:nth-of-type(6) { left: 85%; animation-delay: 8s, 3s; }
    </style>
    
    <div class="heart">❤</div>
    <div class="heart">❤</div>
    <div class="heart">❤</div>
    <div class="heart">❤</div>
    <div class="heart">❤</div>
    <div class="heart">❤</div>
    """, unsafe_allow_html=True)

# 3. 타이틀 및 문구
st.markdown("<h1 style='text-align: center;'>서연이의 첫 번째 생일</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>배서연의 돌잔치에 초대합니다</p>", unsafe_allow_html=True)

# 4. 사진 출력 (사용자님이 성공하셨던 그 방식 그대로)
st.image("baby.jpg", use_column_width=True)

st.write("---")

# 5. 일정 및 장소 정보
st.markdown("""
    <div class='info-box'>
        <h3>📅 일
