# crossovervision-ai 🎯

**An AI-powered, multi-modal trading decision-support system built with PyTorch and Streamlit.**
This project combines ResNet18 chart-image analysis with trade-direction context to classify EMA crossover trading setups as **Safe** or **Trap** and logs live trade outcomes for dataset expansion.

---

## ✨ Key Features

* **Multi-Modal Inference:** Fuses a 128-dimensional visual feature vector (pretrained ResNet18) with a 16-dimensional directional context vector (`Buy` or `Sell`).
* **Automated Chart Capture:** Captures active TradingView charts directly via Windows window-management automation (`PyWin32`) or system clipboard paste (`ImageGrab`).
* **Three-Tier Confidence Filter:** Categorises setups into actionable verdicts based on class probabilities:
  * **🟢 GOLDEN SETUP:** Safe probability $\ge$ 65%
  * **🟡 AVERAGE SETUP:** Safe $>$ Trap, but Safe $<$ 65%
  * **🔴 SKIP TRADE:** Trap $>$ Safe
* **Closed-Loop Dataset Logging:** Saves analyzed chart images locally and appends actual trade outcomes (`TP`, `SL`, `CTC`) to CSV datasets for future retraining.

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Deep Learning** | PyTorch & Torchvision | ResNet18 architecture, custom feature fusion, and model inference |
| **Data & ML** | Scikit-learn & Pandas | Dataset splitting, class-weight calculation, and CSV management |
| **Image Processing** | Pillow (PIL) | Image transformations, clipboard reading, and local file saving |
| **Dashboard UI** | Streamlit | Interactive web interface for chart analysis and trade logging |
| **OS Automation** | PyWin32 | Windows window control for automated TradingView screenshot capture |

---

## 🚀 Installation & Quick Start

### 1. Clone the Repository

```bash
git clone [https://github.com/Boby123design/crossovervision-ai.git](https://github.com/Boby123design/crossovervision-ai.git)
cd crossovervision-ai
```

### 2. Install Dependencies

Ensure Python is installed, then install the required packages:

```bash
python -m pip install torch torchvision streamlit scikit-learn pandas pillow pywin32
```

### 3. Launch the Application

Run the Windows batch launcher from Git Bash or PowerShell:

```bash
./run_2221_trader.bat
```

Alternatively, double-click `run_2221_trader.bat` in Windows File Explorer, or start the Streamlit server directly:

```bash
streamlit run live_trader_2221.py
```

---

## 💻 Usage

### Inputs

* **Chart Image:** Captured automatically from your active TradingView window or pasted from your clipboard (`Ctrl + C`).
* **Trade Direction:** Selected on the dashboard as either `Buy` (`1.0`) or `Sell` (`0.0`).

### Outputs

* **Class Probabilities:** Estimated percentage scores for **Safe (1)** and **Trap (0)**.
* **Filtered Verdict:** Visual badge indicating `GOLDEN SETUP`, `AVERAGE SETUP`, or `SKIP TRADE`.
* **Dataset Record:** Saved PNG screenshot and a new row appended to `live_dataset.csv` once the final trade outcome is logged.

### Example Workflow

1. Launch the dashboard using `run_2221_trader.bat`.
2. Click **Auto-Capture TradingView** or paste a copied chart screenshot.
3. Select your intended direction (**Buy** or **Sell**) and click **Analyse Setup**.
4. Review the **Safe / Trap** probabilities and confidence verdict.
5. After the trade finishes, click **TP**, **SL**, or **CTC** to save the labeled chart to the dataset.

---

## 📁 Project Structure

```text
crossovervision-ai/
├── live_dataset_images/     # Chart screenshots captured during live sessions
├── dataset.csv              # Historical training dataset (Image_Path, Type, Result)
├── live_dataset.csv         # Recorded outcomes from live dashboard usage
├── live_trader_2221.py      # Main Streamlit dashboard and inference script
├── rgb_sniper_2221.pth      # Trained PyTorch model weights
├── run_2221_trader.bat      # One-click Windows batch launcher
├── working.md               # Detailed step-by-step workflow documentation
├── result.md                # Live trading results and statistical breakdown
├── LICENSE                  # Project license file
└── README.md                # Project overview and quick-start guide
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
