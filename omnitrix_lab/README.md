# ⚡ OMNITRIX LAB — Superhero Analytics Dashboard

A **Ben 10 themed** Streamlit web app featuring alien analytics, interactive charts,
a CSS-animated Omnitrix watch, image editing, data analysis tools, and a turn-based battle game.

> Built as a college portfolio project. No official Ben 10 images are used — all visuals
> are CSS/SVG/emoji only.

---

## 🚀 How to Run Locally

### 1. Prerequisites
- **Python 3.10+** installed on your machine
- **pip** (comes with Python)

### 2. Clone / Download
Place the `omnitrix_lab/` folder anywhere on your computer.

### 3. Install Dependencies
Open a terminal inside the `omnitrix_lab/` folder and run:

```bash
pip install -r requirements.txt
```

### 4. Start the App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🌐 Deploy on Streamlit Community Cloud (Free)

1. **Push to GitHub** — Create a GitHub repo and push the entire `omnitrix_lab/` folder.
2. **Go to** [share.streamlit.io](https://share.streamlit.io)
3. **Sign in** with your GitHub account.
4. Click **"New app"** and select:
   - **Repository**: your GitHub repo
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click **Deploy** — your app will be live in ~2 minutes!

---

## 📁 File Structure

```
omnitrix_lab/
│
├── app.py                  # Main file — page config, CSS loading, sidebar nav
├── requirements.txt        # Python packages needed
├── README.md               # This file
│
├── data/
│   └── aliens.csv          # Sample data: 12 Ben 10 aliens with stats
│
├── assets/
│   └── style.css           # All custom dark-theme CSS (glassmorphism, glow, etc.)
│
├── pages_code/
│   ├── __init__.py
│   ├── omnitrix.py         # Animated Omnitrix watch (HTML/CSS/JS)
│   ├── vault.py            # Alien cards grid with filters
│   ├── analytics.py        # Plotly charts dashboard
│   ├── data_lab.py         # CSV upload & analysis tool
│   ├── gallery.py          # Image upload, gallery & Pillow filters
│   └── arena.py            # Turn-based battle game
│
└── utils/
    ├── __init__.py
    └── helpers.py           # Shared functions: data loading, card HTML, etc.
```

---

## 🎮 Pages Overview

| Page | What it does |
|------|-------------|
| ⌚ Omnitrix | Animated CSS/JS Omnitrix watch — tap to transform into an alien |
| 🗃️ Alien Vault | Card/table grid of all aliens with search, filter, and sort |
| 📊 Analytics | KPI cards + Plotly charts (bar, radar, donut, scatter, histogram) |
| 🧪 Data Lab | Upload any CSV → preview, stats, auto chart builder, download |
| 🖼️ Gallery | Upload images → grid view + Pillow filters (resize, rotate, green tint) |
| ⚔️ Battle Arena | Pick alien vs villain, turn-based combat with HP bars |

---

## 🛠️ Tech Stack

- **Streamlit** — Web framework
- **Pandas** — Data handling
- **Plotly** — Interactive charts
- **Pillow** — Image processing
- **HTML/CSS/JS** — Custom animations via `st.components.v1.html`

---

*Made with ❤️ for learning and fun.*
