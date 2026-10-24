import streamlit as st
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, models
from PIL import Image, ImageGrab
import os
import pandas as pd
from datetime import datetime
import time

try:
    import win32gui
    import win32con
except ImportError:
    st.error("🚨 'pywin32' library missing. Terminal mein 'pip install pywin32' run karein!")

# ==========================================
# 1. PREMIUM PAGE SETUP
# ==========================================
st.set_page_config(page_title="2221 Master Sniper Terminal", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    button[kind="primary"] { background-color: #6200ea !important; color: white !important; border: none !important; border-radius: 8px; font-weight: bold; transition: 0.3s; }
    button[kind="primary"]:hover { transform: scale(1.02); background-color: #7c4dff !important; }
    .metric-card { background-color: #1e222d; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #333; }
    .entry-verdict { font-size: 24px; font-weight: bold; padding: 15px; border-radius: 8px; text-align: center; margin-top: 15px;}
    </style>
""", unsafe_allow_html=True)

st.title("🦅 2221 Master Sniper Engine (The 58% Edge)")
st.markdown("---")

# ==========================================
# 2. THE RGB-VISION ARCHITECTURE
# ==========================================
class RgbEmaBrain(nn.Module):
    def __init__(self):
        super(RgbEmaBrain, self).__init__()
        
        self.vision = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
        num_ftrs = self.vision.fc.in_features
        self.vision.fc = nn.Linear(num_ftrs, 128) 
        
        self.context = nn.Linear(1, 16)
        
        self.fusion = nn.Sequential(
            nn.Linear(128 + 16, 64),
            nn.ReLU(),
            nn.Dropout(0.5), 
            nn.Linear(64, 2) # Binary Predictor (0 = Trap, 1 = Safe Entry)
        )

    def forward(self, image, trade_type):
        x_vision = torch.relu(self.vision(image))
        x_context = torch.relu(self.context(trade_type))
        x_combined = torch.cat((x_vision, x_context), dim=1) 
        output = self.fusion(x_combined)
        return output

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
base_dir = r"C:\Models\Model_12"

# 🚨 LOADING THE NEW MASSIVE 2221 MODEL
model_path = os.path.join(base_dir, "rgb_sniper_2221.pth")

live_img_dir = os.path.join(base_dir, "live_dataset_images")
live_csv_path = os.path.join(base_dir, "dataset.csv") 

os.makedirs(live_img_dir, exist_ok=True)

@st.cache_resource
def load_model():
    model = RgbEmaBrain().to(device)
    try:
        model.load_state_dict(torch.load(model_path, map_location=device), strict=False)
        st.sidebar.success("✅ 2221 Master Engine Online (57.98% Edge)")
    except Exception as e:
        st.error(f"Critical Model Loading Error: {e}")
    model.eval() 
    return model

model = load_model()

# STRICT PURE RGB TRANSFORM
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

if 'current_image' not in st.session_state:
    st.session_state.current_image = None

# ==========================================
# 3. USER INTERFACE & LOGIC
# ==========================================
col_img, col_logic = st.columns([1.5, 1])

with col_img:
    st.markdown("### 📸 Live Chart Capture")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("📋 Paste Chart (Ctrl+C)", use_container_width=True):
            try:
                img = ImageGrab.grabclipboard()
                if img is not None and isinstance(img, Image.Image):
                    st.session_state.current_image = img
                else:
                    st.warning("⚠️ Clipboard khali hai!")
            except Exception as e:
                st.error(f"Error: {e}")
                
    with col_btn2:
        if st.button("📸 Auto-Capture TradingView", type="primary", use_container_width=True):
            try:
                hwnd = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
                time.sleep(0.7) 
                img = ImageGrab.grab(bbox=(167, 104, 1385, 1004))
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                st.session_state.current_image = img
                st.rerun()
            except Exception as e:
                st.error(f"⚠️ Auto-Capture Error: {e}")

    if st.session_state.current_image is not None:
        st.image(st.session_state.current_image, caption='Master Engine Vision', use_container_width=True)

with col_logic:
    st.markdown("### ⚙️ Master Scalper Analysis")
    trade_dir = st.selectbox("Market Direction:", ["Buy", "Sell"])
    
    if st.button("🚀 Analyze Setup", type="primary", use_container_width=True):
        if st.session_state.current_image is not None:
            with st.spinner('Analyzing Pure Colors & Logic...'):
                img_tensor = transform(st.session_state.current_image.convert('RGB')).unsqueeze(0).to(device)
                type_val = 1.0 if trade_dir == "Buy" else 0.0
                tabular_tensor = torch.tensor([[type_val]], dtype=torch.float32).to(device)
                
                with torch.no_grad():
                    output = model(img_tensor, tabular_tensor) 
                    probs = F.softmax(output, dim=1)[0]
                
                # RGB Binary Output Map: 0 = SKIP (SL), 1 = ENTRY (TP/CTC)
                prob_skip = probs[0].item() * 100
                prob_safe = probs[1].item() * 100
                
                st.markdown("### 📊 AI Verdict")
                
                col_prob1, col_prob2 = st.columns(2)
                col_prob1.metric("🟢 SAFE ENTRY", f"{prob_safe:.1f}%")
                col_prob2.metric("🔴 TRAP RISK", f"{prob_skip:.1f}%")
                
                # The 65% Boby Bhai Confidence Filter!
                if prob_safe >= 65.0:
                    st.markdown('<div class="entry-verdict" style="background-color: #00c853; color: white;">✅ GOLDEN SETUP - TAKE ENTRY</div>', unsafe_allow_html=True)
                elif prob_safe > prob_skip:
                    st.markdown('<div class="entry-verdict" style="background-color: #ff9100; color: white;">⚠️ AVERAGE SETUP - PROCEED WITH CAUTION</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="entry-verdict" style="background-color: #ff3d00; color: white;">❌ SKIP TRADE - TRAP DETECTED</div>', unsafe_allow_html=True)
                    
        else:
            st.error("Pehle chart lijiye!")

    st.markdown("---")
    
    st.markdown("### 💾 Harvest Data (Keep Growing)")
    st.caption("AI ka prediction chahe jo ho, real result log karein taaki data badhta rahe.")
    actual_result = st.radio("Actual Outcome:", ["TP", "SL", "CTC"], horizontal=True)
    
    if st.button("💾 Save to Master Dataset", use_container_width=True):
        if st.session_state.current_image is not None:
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                img_name = f"trade_master_{timestamp}.png"
                img_full_path = os.path.join(live_img_dir, img_name)
                
                st.session_state.current_image.convert('RGB').save(img_full_path)
                
                new_data = {
                    "Image_Path": img_full_path,
                    "Type": trade_dir.lower(),
                    "Result": actual_result.lower() 
                }
                new_df = pd.DataFrame([new_data])
                
                if not os.path.exists(live_csv_path):
                    new_df.to_csv(live_csv_path, index=False)
                else:
                    new_df.to_csv(live_csv_path, mode='a', header=False, index=False)
                    
                st.success("✅ Trade Saved! Database Growing.")
                st.session_state.current_image = None
                time.sleep(1)
                st.rerun()
                
            except Exception as e:
                st.error(f"Error saving data: {e}")
        else:
            st.error("Save karne ke liye image missing hai!")