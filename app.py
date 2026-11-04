import streamlit as st
from PIL import Image
import google.generativeai as genai

# Cấu hình trang
st.set_page_config(
    page_title="Locket AI Valuer - Dashboard",
    page_icon="✨",
    layout="wide"
)

# CSS tùy chỉnh giao diện: Tăng độ sáng và độ rõ nét của chữ
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Màu nền chính tối sang trọng */
    .stApp {
        background-color: #121212;
        color: #ffffff !important; /* Đổi toàn bộ chữ mặc định thành màu trắng tinh để siêu rõ */
    }

    /* Thanh Sidebar bên trái */
    [data-testid="stSidebar"] {
        background-color: #1e1e1e;
        border-right: 1px solid #2c2c2c;
    }
    
    [data-testid="stSidebar"] span, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: #ffffff !important;
        font-weight: 600;
    }

    /* Khung thẻ (Card) nội dung */
    .dashboard-card {
        background-color: #1e1e1e;
        border: 1px solid #3a3a3a;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.5);
    }

    /* Tiêu đề trong card làm nổi bật sáng rực */
    .card-title {
        color: #00ffcc !important; /* Xanh neon sáng rực giúp dễ phân biệt các mục */
        font-weight: 800;
        font-size: 1.25rem;
        margin-bottom: 15px;
    }

    /* Chữ mô tả, nhãn (label) trong app sáng và rõ hơn */
    label, .stRadio label, .stTextInput label {
        color: #f1f5f9 !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }

    /* ================= TÙY CHỈNH NÚT BẤM (BUTTON) ================= */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%) !important; 
        color: #121212 !important; 
        border-radius: 10px;
        height: 3.2em;
        font-weight: 900 !important; 
        font-size: 1.15rem;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 165, 0, 0.5);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #ffea75 0%, #ffb732 100%) !important;
        box-shadow: 0 6px 20px rgba(255, 165, 0, 0.7);
        transform: translateY(-2px);
        color: #000000 !important;
    }

    /* Khu vực tải file */
    [data-testid="stFileUploader"] {
        background-color: #1a1a1a;
        border: 2px dashed #00ffcc;
        border-radius: 12px;
        padding: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== THANH MENU BÊN TRÁI (SIDEBAR) ====================
with st.sidebar:
    st.image("https://images.chesscomfiles.com/uploads/v1/images_users/three_column/user/pixelated_king.png", width=50)
    st.markdown("### **TrọngPhúc0777**")
    st.caption("🔥 1 Day Streak")
    st.divider()
    
    st.markdown("### 🧭 Menu Điều Hướng")
    menu_chon = st.radio("Chọn tính năng:", ["🏠 Trang Chủ & Định Giá", "⭐ Gói Thành Viên", "⚙️ Cài đặt hệ thống"])
    
    st.divider()
    st.info("💡 Mẹo: Dùng API Key của Gemini để kích hoạt AI nhận diện.")

# ==================== GIAO DIỆN CHÍNH (DASHBOARD) ====================
if menu_chon == "🏠 Trang Chủ & Định Giá":
    st.markdown("""
        <div style="background: linear-gradient(90deg, #1e3a8a 0%, #172554 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px; text-align: center; border: 1px solid #3b82f6;">
            <h1 style="color: #ffffff; margin: 0; font-size: 2.2rem; font-weight: 800;">📸 LOCKET AI - HỆ THỐNG THẨM ĐỊNH VẬT PHẨM</h1>
            <p style="color: #93c5fd; margin-top: 8px; font-size: 1.1rem; font-weight: 600;">Chụp ảnh hoặc tải lên hình ảnh để hệ thống tự động nhận diện và tính tiền thông minh.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<p class="card-title">🔑 Cấu hình kết nối API</p>', unsafe_allow_html=True)
        api_key = st.text_input("Nhập Google Gemini API Key:", type="password", placeholder="AIzaSy...")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<p class="card-title">📁 Tải ảnh hoặc chụp hình</p>', unsafe_allow_html=True)
        upload_type = st.radio("Chọn phương thức:", ["Tải ảnh có sẵn", "Chụp bằng Camera"], horizontal=True)
        
        image = None
        if upload_type == "Tải ảnh có sẵn":
            uploaded_file = st.file_uploader("Chọn file ảnh món đồ...", type=["jpg", "jpeg", "png"])
            if uploaded_file:
                image = Image.open(uploaded_file)
        else:
            camera_file = st.camera_input("Chụp ảnh trực tiếp")
            if camera_file:
                image = Image.open(camera_file)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown('<p class="card-title">📊 Kết quả phân tích & Định giá</p>', unsafe_allow_html=True)
        
        if image is not None:
            image.thumbnail((1024, 1024))
            st.image(image, caption="Hình ảnh đã chọn", use_container_width=True)
            
            if st.button("🚀 BẮT ĐẦU PHÂN TÍCH NGAY"):
                if not api_key:
                    st.error("⚠️ Vui lòng nhập API Key ở cột bên trái trước!")
                else:
                    with st.spinner("AI đang xử lý hình ảnh..."):
                        try:
                            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                            model = genai.GenerativeModel('gemini-3.8-flash')
                            
                            prompt = (
                                "Bạn là chuyên gia thẩm định giá. "
                                "Hãy phân tích món đồ trong ảnh và trả về các thông tin bằng tiếng Việt:\n"
                                "1. Tên món đồ\n"
                                "2. Mô tả chi tiết\n"
                                "3. Ước tính giá tiền thị trường (VNĐ)\n"
                                "4. Nhận xét / Đánh giá"
                            )
                            response = model.generate_content([image, prompt])
                            
                            st.success("✨ Hoàn tất!")
                            st.markdown(response.text)
                        except Exception as e:
                            st.error(f"Lỗi: {e}")
        else:
            st.info("👈 Vui lòng tải ảnh lên ở cột bên trái để hiển thị kết quả phân tích tại đây.")
        st.markdown('</div>', unsafe_allow_html=True)

elif menu_chon == "⭐ Gói Thành Viên":
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<p class="card-title">💎 Nâng cấp tài khoản VIP</p>', unsafe_allow_html=True)
    st.write("Trở thành hội viên cao cấp để sử dụng các mô hình AI phân tích nhanh hơn, không giới hạn số lượng ảnh quét mỗi ngày.")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.markdown('<p class="card-title">⚙️ Cài đặt hệ thống</p>', unsafe_allow_html=True)
    st.write("Tùy chỉnh giao diện, ngôn ngữ và cấu hình lưu trữ lịch sử quét.")
    st.markdown('</div>', unsafe_allow_html=True)
