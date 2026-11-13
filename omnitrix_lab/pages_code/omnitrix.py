"""
omnitrix.py — The Omnitrix Transform page.
Features a pure CSS/JS animated Omnitrix watch and authentic, animated Ben 10 aliens.
"""

import streamlit as st
import streamlit.components.v1 as components
from utils.helpers import load_alien_data, render_section_title
from utils.alien_graphics import get_alien_svg


def show():
    """Render the Omnitrix transform page."""
    render_section_title("⌚ OMNITRIX TRANSFORM")

    df = load_alien_data()
    alien_names = df["name"].tolist()

    # Manage alien selection state
    if "alien_idx" not in st.session_state:
        st.session_state.alien_idx = 0

    col_prev, col_select, col_next = st.columns([1, 4, 1])
    with col_prev:
        st.write("")
        st.write("")
        if st.button("◀ PREV", key="btn_prev_alien", use_container_width=True):
            st.session_state.alien_idx = (st.session_state.alien_idx - 1) % len(alien_names)
            st.rerun()

    with col_select:
        selected_name = st.selectbox(
            "Choose your alien transformation (or use arrows to turn the dial):",
            alien_names,
            index=st.session_state.alien_idx,
            key="omnitrix_alien_select_box",
        )
        new_idx = alien_names.index(selected_name)
        if new_idx != st.session_state.alien_idx:
            st.session_state.alien_idx = new_idx
            st.rerun()

    with col_next:
        st.write("")
        st.write("")
        if st.button("NEXT ▶", key="btn_next_alien", use_container_width=True):
            st.session_state.alien_idx = (st.session_state.alien_idx + 1) % len(alien_names)
            st.rerun()

    # Get alien data
    alien = df.iloc[st.session_state.alien_idx]

    # Build the full HTML/CSS/JS Omnitrix animation
    omnitrix_html = _build_omnitrix_html(alien)

    # Render with st.components
    components.html(omnitrix_html, height=860, scrolling=False)


def _build_omnitrix_html(alien):
    """Build the complete HTML for the animated Omnitrix watch with authentic alien visuals."""
    alien_svg = get_alien_svg(alien["name"])

    stats_html = "".join([
        f'<div class="tf-stat-row">'
        f'<span class="tf-stat-label">{label}</span>'
        f'<div class="tf-stat-bar-bg"><div class="tf-stat-bar-fill" style="width:{alien[key]}%"></div></div>'
        f'<span class="tf-stat-val">{alien[key]}</span>'
        f'</div>'
        for label, key in [("STR", "strength"), ("SPD", "speed"), ("DEF", "defense"), ("INT", "intelligence")]
    ])

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@500;600;700&display=swap');
    
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
        background: transparent;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        min-height: 840px;
        font-family: 'Rajdhani', sans-serif;
        overflow: hidden;
    }}

    .scene {{
        position: relative;
        width: 100%;
        max-width: 480px;
        min-height: 820px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    /* Floating particles */
    .particles {{
        position: absolute;
        width: 100%;
        height: 400px;
        top: 0;
        pointer-events: none;
        overflow: hidden;
    }}
    .particle {{
        position: absolute;
        width: 4px;
        height: 4px;
        border-radius: 50%;
        background: #39ff14;
        opacity: 0;
        animation: float-particle 3s infinite ease-in-out;
    }}
    @keyframes float-particle {{
        0% {{ opacity: 0; transform: translateY(0) scale(0.5); }}
        50% {{ opacity: 0.9; }}
        100% {{ opacity: 0; transform: translateY(-130px) scale(0); }}
    }}

    /* Omnitrix Watch */
    .watch-container {{
        position: relative;
        width: 280px;
        height: 280px;
        margin-top: 50px;
        cursor: pointer;
        z-index: 10;
        transition: transform 0.2s ease;
    }}
    .watch-container:hover {{
        transform: scale(1.02);
    }}

    .watch-strap {{
        position: absolute;
        top: -30px;
        left: 70px;
        width: 140px;
        height: 340px;
        background: linear-gradient(90deg, #182218 0%, #2b3d2b 50%, #182218 100%);
        border-radius: 20px;
        border: 2px solid #1a8a0a;
        box-shadow: 0 0 15px rgba(57,255,20,0.15);
        z-index: 1;
    }}

    .watch-ring {{
        position: absolute;
        inset: 0;
        border-radius: 50%;
        border: 10px solid #1f2b1f;
        background: radial-gradient(circle, #101910 0%, #060b06 100%);
        box-shadow: 0 0 25px rgba(57,255,20,0.35), inset 0 0 20px rgba(57,255,20,0.25);
        z-index: 2;
        transition: box-shadow 0.3s ease;
    }}
    .watch-container:hover .watch-ring {{
        box-shadow: 0 0 40px #39ff14, inset 0 0 25px #39ff1488;
    }}

    .dial {{
        position: absolute;
        inset: 22px;
        border-radius: 50%;
        background: radial-gradient(circle, #183318 0%, #081108 75%);
        border: 4px solid #39ff14;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        animation: pulse-glow 2.2s ease-in-out infinite;
        transition: transform 0.15s ease, box-shadow 0.3s ease;
        z-index: 3;
    }}
    @keyframes pulse-glow {{
        0%, 100% {{ box-shadow: 0 0 15px rgba(57,255,20,0.4), 0 0 30px rgba(57,255,20,0.2); }}
        50% {{ box-shadow: 0 0 35px rgba(57,255,20,0.9), 0 0 60px rgba(57,255,20,0.5); }}
    }}

    .hourglass {{
        width: 90px;
        height: 100px;
    }}
    .hourglass path {{
        fill: none;
        stroke: #39ff14;
        stroke-width: 5;
        stroke-linecap: round;
        stroke-linejoin: round;
        filter: drop-shadow(0 0 8px #39ff14);
    }}

    .dial-silhouette-name {{
        color: #39ff14;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.72rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-top: 4px;
        text-shadow: 0 0 8px #39ff14;
    }}

    /* Press & Spin Animations */
    .watch-container.pressing .dial {{
        transform: scale(0.9) translateY(4px);
        box-shadow: 0 0 50px #39ff14, 0 0 100px #39ff14 !important;
        animation: none;
    }}
    .watch-container.transforming .dial {{
        animation: spin-slam 0.85s cubic-bezier(0.68, -0.55, 0.27, 1.55) forwards;
    }}
    @keyframes spin-slam {{
        0% {{ transform: rotate(0deg) scale(0.9); }}
        50% {{ transform: rotate(270deg) scale(1.15); box-shadow: 0 0 70px #39ff14, 0 0 140px #ffffff; }}
        100% {{ transform: rotate(360deg) scale(1); }}
    }}

    /* Green-white flash */
    .flash-overlay {{
        position: absolute;
        inset: -100px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(255,255,255,1) 0%, rgba(57,255,20,0.95) 45%, transparent 75%);
        opacity: 0;
        z-index: 25;
        pointer-events: none;
    }}
    .flash-overlay.active {{
        animation: flash-burst 0.7s ease-out forwards;
    }}
    @keyframes flash-burst {{
        0% {{ opacity: 1; transform: scale(0.3); }}
        50% {{ opacity: 1; transform: scale(2.2); }}
        100% {{ opacity: 0; transform: scale(3.2); }}
    }}

    /* Energy rings */
    .energy-ring {{
        position: absolute;
        border-radius: 50%;
        border: 3px solid #39ff14;
        opacity: 0;
        pointer-events: none;
        z-index: 20;
    }}
    .energy-ring.active {{
        animation: ring-expand 1.1s cubic-bezier(0.1, 0.8, 0.3, 1) forwards;
    }}
    @keyframes ring-expand {{
        0% {{ opacity: 1; transform: scale(0.2); border-color: #ffffff; }}
        100% {{ opacity: 0; transform: scale(3); border-color: #39ff14; }}
    }}
    .energy-ring:nth-child(1) {{ inset: -30px; animation-delay: 0s; }}
    .energy-ring:nth-child(2) {{ inset: -60px; animation-delay: 0.2s; }}
    .energy-ring:nth-child(3) {{ inset: -90px; animation-delay: 0.4s; }}

    .tap-hint {{
        margin-top: 30px;
        color: #39ff14;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.85rem;
        letter-spacing: 4px;
        text-align: center;
        animation: blink-hint 1.8s infinite ease-in-out;
        z-index: 10;
        text-shadow: 0 0 10px rgba(57,255,20,0.6);
    }}
    @keyframes blink-hint {{
        0%,100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(0.97); }}
    }}

    /* ============================================================
       ALIEN TRANSFORMATION RESULT CARD
       ============================================================ */
    .alien-result {{
        position: absolute;
        top: 10px;
        width: 100%;
        max-width: 440px;
        background: rgba(14, 22, 14, 0.94);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 2px solid #39ff14;
        border-radius: 20px;
        padding: 1.5rem 1.4rem;
        text-align: center;
        opacity: 0;
        transform: scale(0.65) translateY(50px);
        pointer-events: none;
        z-index: 30;
        box-shadow: 0 0 35px rgba(57,255,20,0.4), inset 0 0 20px rgba(57,255,20,0.15);
    }}
    .alien-result.show {{
        animation: alien-entrance 0.65s cubic-bezier(0.175, 0.885, 0.32, 1.275) 0.35s forwards;
    }}
    @keyframes alien-entrance {{
        0% {{ opacity: 0; transform: scale(0.65) translateY(50px); }}
        70% {{ opacity: 1; transform: scale(1.04) translateY(-8px); }}
        100% {{ opacity: 1; transform: scale(1) translateY(0); pointer-events: auto; }}
    }}

    /* Transformation Announcement Banner */
    .tf-banner {{
        display: inline-block;
        background: rgba(57, 255, 20, 0.18);
        border: 1px solid #39ff14;
        color: #39ff14;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.72rem;
        letter-spacing: 2px;
        padding: 4px 14px;
        border-radius: 20px;
        margin-bottom: 8px;
        text-shadow: 0 0 8px #39ff14;
    }}

    /* Alien Graphic Container */
    .alien-graphic-box {{
        width: 240px;
        height: 240px;
        margin: 4px auto 10px auto;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    .alien-result .ar-name {{
        font-family: 'Orbitron', sans-serif;
        color: #39ff14;
        font-size: 1.6rem;
        letter-spacing: 4px;
        margin: 4px 0;
        text-shadow: 0 0 15px #39ff14;
        font-weight: 900;
    }}
    .alien-result .ar-meta {{
        display: flex;
        justify-content: center;
        gap: 10px;
        align-items: center;
        margin-bottom: 8px;
    }}
    .alien-result .ar-type {{
        background: rgba(57,255,20,0.2);
        color: #39ff14;
        font-size: 0.8rem;
        padding: 3px 12px;
        border-radius: 12px;
        border: 1px solid #1a8a0a;
        font-weight: 600;
    }}
    .alien-result .ar-planet {{
        color: #a0a0a0;
        font-size: 0.82rem;
    }}
    .alien-result .ar-desc {{
        color: #cccccc;
        font-size: 0.9rem;
        line-height: 1.35;
        margin: 6px 0 12px 0;
        background: rgba(0, 0, 0, 0.35);
        padding: 8px 12px;
        border-radius: 10px;
        border-left: 3px solid #39ff14;
        text-align: left;
    }}

    /* Stat Bars */
    .tf-stats-container {{
        margin-top: 6px;
    }}
    .tf-stat-row {{
        display: flex;
        align-items: center;
        gap: 8px;
        margin: 4px 0;
    }}
    .tf-stat-label {{
        color: #a0a0a0;
        font-size: 0.78rem;
        width: 34px;
        text-align: right;
        font-family: 'Orbitron', sans-serif;
    }}
    .tf-stat-bar-bg {{
        flex: 1;
        height: 10px;
        background: rgba(255,255,255,0.08);
        border-radius: 5px;
        overflow: hidden;
    }}
    .tf-stat-bar-fill {{
        height: 100%;
        background: linear-gradient(90deg, #1a8a0a, #39ff14);
        border-radius: 5px;
        box-shadow: 0 0 6px #39ff14;
        transition: width 0.8s ease;
    }}
    .tf-stat-val {{
        color: #39ff14;
        font-size: 0.78rem;
        width: 28px;
        font-family: 'Orbitron', sans-serif;
    }}

    /* Revert Button */
    .revert-btn {{
        margin-top: 14px;
        background: transparent;
        color: #ff4444;
        border: 1px solid #ff4444;
        border-radius: 8px;
        padding: 6px 16px;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.75rem;
        letter-spacing: 2px;
        cursor: pointer;
        transition: all 0.25s ease;
    }}
    .revert-btn:hover {{
        background: #ff4444;
        color: #0a0f0a;
        box-shadow: 0 0 15px rgba(255,68,68,0.7);
    }}

    /* Red timeout flash */
    .alien-result.timeout {{
        animation: red-flash-out 0.7s ease-in forwards;
    }}
    @keyframes red-flash-out {{
        0% {{ opacity: 1; transform: scale(1); box-shadow: 0 0 35px rgba(57,255,20,0.5); }}
        35% {{ box-shadow: 0 0 60px #ff3333, inset 0 0 30px #ff3333; border-color: #ff3333; }}
        100% {{ opacity: 0; transform: scale(0.65); }}
    }}

    /* ============================================================
       CUSTOM ALIEN ANIMATIONS
       ============================================================ */

    /* Four Arms Animations */
    .four-arms-anim {{
        animation: fa-ground-pound 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    @keyframes fa-ground-pound {{
        0% {{ transform: scale(0.5) translateY(40px); }}
        70% {{ transform: scale(1.1) translateY(-10px); }}
        100% {{ transform: scale(1) translateY(0); }}
    }}
    .fa-aura-pulse {{
        animation: fa-aura-anim 1.8s infinite ease-in-out;
    }}
    @keyframes fa-aura-anim {{
        0%, 100% {{ opacity: 0.4; transform: scale(0.95); transform-origin: center; }}
        50% {{ opacity: 0.9; transform: scale(1.08); transform-origin: center; }}
    }}
    .fa-ground-ring {{
        animation: fa-ring-anim 1.4s infinite ease-out;
    }}
    @keyframes fa-ring-anim {{
        0% {{ opacity: 1; r: 20px; }}
        100% {{ opacity: 0; r: 75px; }}
    }}
    .fa-arm-top-left {{
        animation: fa-arm-l1 1.6s infinite ease-in-out;
        transform-origin: 115px 110px;
    }}
    @keyframes fa-arm-l1 {{
        0%, 100% {{ transform: rotate(0deg); }}
        50% {{ transform: rotate(-14deg) translateY(-4px); }}
    }}
    .fa-arm-top-right {{
        animation: fa-arm-r1 1.6s infinite ease-in-out;
        transform-origin: 165px 110px;
    }}
    @keyframes fa-arm-r1 {{
        0%, 100% {{ transform: rotate(0deg); }}
        50% {{ transform: rotate(14deg) translateY(-4px); }}
    }}
    .fa-arm-bot-left {{
        animation: fa-arm-l2 1.6s infinite ease-in-out 0.2s;
        transform-origin: 110px 145px;
    }}
    @keyframes fa-arm-l2 {{
        0%, 100% {{ transform: rotate(0deg); }}
        50% {{ transform: rotate(12deg) translateX(-4px); }}
    }}
    .fa-arm-bot-right {{
        animation: fa-arm-r2 1.6s infinite ease-in-out 0.2s;
        transform-origin: 170px 145px;
    }}
    @keyframes fa-arm-r2 {{
        0%, 100% {{ transform: rotate(0deg); }}
        50% {{ transform: rotate(-12deg) translateX(4px); }}
    }}

    /* Heatblast Animations */
    .hb-heat-pulse {{
        animation: hb-pulse 1.6s infinite alternate ease-in-out;
    }}
    @keyframes hb-pulse {{
        0% {{ opacity: 0.4; transform: scale(0.95); transform-origin: center; }}
        100% {{ opacity: 0.85; transform: scale(1.1); transform-origin: center; }}
    }}
    .hb-head-fire {{
        animation: hb-flicker 0.4s infinite alternate ease-in-out;
        transform-origin: 140px 90px;
    }}
    @keyframes hb-flicker {{
        0% {{ transform: scaleY(0.95) skewX(-2deg); }}
        100% {{ transform: scaleY(1.08) skewX(2deg); }}
    }}
    .hb-hand-flames-left {{
        animation: hb-flame-l 0.5s infinite alternate ease-in-out;
    }}
    @keyframes hb-flame-l {{
        0% {{ transform: scale(0.9) rotate(-4deg); transform-origin: 50px 140px; }}
        100% {{ transform: scale(1.15) rotate(4deg); transform-origin: 50px 140px; }}
    }}
    .hb-hand-flames-right {{
        animation: hb-flame-r 0.5s infinite alternate ease-in-out 0.1s;
    }}
    @keyframes hb-flame-r {{
        0% {{ transform: scale(0.9) rotate(4deg); transform-origin: 230px 140px; }}
        100% {{ transform: scale(1.15) rotate(-4deg); transform-origin: 230px 140px; }}
    }}

    /* XLR8 Animations */
    .xlr8-anim {{
        animation: xlr-dash 0.6s cubic-bezier(0.1, 0.9, 0.2, 1);
    }}
    @keyframes xlr-dash {{
        0% {{ transform: translateX(-160px) skewX(25deg); opacity: 0; }}
        70% {{ transform: translateX(12px) skewX(-10deg); opacity: 1; }}
        100% {{ transform: translateX(0) skewX(0); opacity: 1; }}
    }}
    .xlr-tail {{
        animation: xlr-tail-whip 1.2s infinite ease-in-out;
        transform-origin: 125px 180px;
    }}
    @keyframes xlr-tail-whip {{
        0%, 100% {{ transform: rotate(0deg); }}
        50% {{ transform: rotate(16deg); }}
    }}
    .xlr-speed-streaks line {{
        animation: xlr-streak 0.8s infinite linear;
    }}
    @keyframes xlr-streak {{
        0% {{ stroke-dashoffset: 0; opacity: 1; }}
        100% {{ stroke-dashoffset: -50; opacity: 0.3; }}
    }}

    /* Diamondhead Animations */
    .diamond-anim {{
        animation: dh-erupt 0.65s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    @keyframes dh-erupt {{
        0% {{ transform: scale(0.5) rotate(-8deg); opacity: 0; }}
        100% {{ transform: scale(1) rotate(0deg); opacity: 1; }}
    }}
    .dh-blade-left {{
        animation: dh-blade-l 2s infinite ease-in-out;
        transform-origin: 110px 115px;
    }}
    @keyframes dh-blade-l {{
        0%, 100% {{ transform: rotate(0deg); }}
        50% {{ transform: rotate(-8deg); }}
    }}
    .dh-blade-right {{
        animation: dh-blade-r 2s infinite ease-in-out;
        transform-origin: 170px 115px;
    }}
    @keyframes dh-blade-r {{
        0%, 100% {{ transform: rotate(0deg); }}
        50% {{ transform: rotate(8deg); }}
    }}
    .dh-sparkle-1, .dh-sparkle-2 {{
        animation: dh-glint 1.4s infinite ease-in-out;
    }}
    @keyframes dh-glint {{
        0%, 100% {{ opacity: 0.2; transform: scale(0.6) rotate(0deg); }}
        50% {{ opacity: 1; transform: scale(1.3) rotate(45deg); }}
    }}

    /* Upgrade Animations */
    .up-circuits path {{
        animation: up-circuit-flow 1.5s infinite alternate ease-in-out;
    }}
    @keyframes up-circuit-flow {{
        0% {{ stroke: #1a8a0a; filter: drop-shadow(0 0 2px #1a8a0a); }}
        100% {{ stroke: #39ff14; filter: drop-shadow(0 0 8px #39ff14); }}
    }}
    .up-eye-ring {{
        animation: up-eye-ripple 1.8s infinite ease-in-out;
        transform-origin: 140px 75px;
    }}
    @keyframes up-eye-ripple {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.18); }}
    }}

    /* Ghostfreak Animations */
    .gf-floating-body {{
        animation: gf-float 2.4s infinite ease-in-out;
    }}
    @keyframes gf-float {{
        0%, 100% {{ transform: translateY(0) rotate(0deg); }}
        50% {{ transform: translateY(-12px) rotate(2deg); }}
    }}
    .gf-tentacles path {{
        animation: gf-tentacle-wave 2s infinite alternate ease-in-out;
    }}
    @keyframes gf-tentacle-wave {{
        0% {{ transform: scaleY(1); }}
        100% {{ transform: scaleY(1.25) skewX(8deg); }}
    }}
    .gf-eye-slider {{
        animation: gf-eye-slide 3s infinite alternate ease-in-out;
    }}
    @keyframes gf-eye-slide {{
        0% {{ transform: translate(0, 0); }}
        100% {{ transform: translate(6px, 14px); }}
    }}

    /* Wildmutt Animations */
    .wm-sonic-waves path {{
        animation: wm-wave 1.2s infinite ease-out;
    }}
    @keyframes wm-wave {{
        0% {{ opacity: 1; transform: translateX(0) scale(0.8); }}
        100% {{ opacity: 0; transform: translateX(-30px) scale(1.3); }}
    }}

    /* Cannonbolt Animations */
    .cannonbolt-anim {{
        animation: cb-roll-slam 0.7s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    @keyframes cb-roll-slam {{
        0% {{ transform: translateX(-140px) rotate(-360deg) scale(0.6); opacity: 0; }}
        70% {{ transform: translateX(10px) rotate(15deg) scale(1.08); opacity: 1; }}
        100% {{ transform: translateX(0) rotate(0deg) scale(1); opacity: 1; }}
    }}
    .cb-shockwave {{
        animation: cb-impact 1.4s infinite ease-out;
    }}
    @keyframes cb-impact {{
        0% {{ rx: 40px; ry: 8px; opacity: 1; }}
        100% {{ rx: 95px; ry: 20px; opacity: 0; }}
    }}

    /* Stinkfly Animations */
    .sf-wings ellipse {{
        animation: sf-flutter 0.15s infinite alternate ease-in-out;
    }}
    @keyframes sf-flutter {{
        0% {{ transform: scaleY(1); }}
        100% {{ transform: scaleY(0.3) skewX(-15deg); }}
    }}
    .sf-slime-drop {{
        animation: sf-drop 1.4s infinite ease-in;
    }}
    @keyframes sf-drop {{
        0% {{ transform: translateY(0); opacity: 1; }}
        100% {{ transform: translateY(30px); opacity: 0; }}
    }}

    /* Ripjaws Animations */
    .rj-jaws {{
        animation: rj-chomp 1.6s infinite ease-in-out;
        transform-origin: 140px 95px;
    }}
    @keyframes rj-chomp {{
        0%, 100% {{ transform: rotate(0deg); }}
        40% {{ transform: rotate(-6deg); }}
        70% {{ transform: rotate(4deg); }}
    }}
    .rj-lure-group circle:first-of-type {{
        animation: rj-lure-pulse 1.4s infinite alternate ease-in-out;
    }}
    @keyframes rj-lure-pulse {{
        0% {{ opacity: 0.5; transform: scale(0.9); transform-origin: 180px 52px; }}
        100% {{ opacity: 1; transform: scale(1.3); transform-origin: 180px 52px; }}
    }}

    /* Grey Matter Animations */
    .gm-holo-rings ellipse {{
        animation: gm-spin 4s infinite linear;
        transform-origin: 140px 130px;
    }}
    @keyframes gm-spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    .gm-head {{
        animation: gm-think 2s infinite alternate ease-in-out;
        transform-origin: 140px 105px;
    }}
    @keyframes gm-think {{
        0% {{ transform: scale(1); }}
        100% {{ transform: scale(1.05); }}
    }}

    /* Wildvine Animations */
    .wv-vines-left {{
        animation: wv-whip-l 2s infinite alternate ease-in-out;
        transform-origin: 115px 130px;
    }}
    @keyframes wv-whip-l {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(-14deg) scale(1.08); }}
    }}
    .wv-vines-right {{
        animation: wv-whip-r 2s infinite alternate ease-in-out 0.2s;
        transform-origin: 165px 130px;
    }}
    @keyframes wv-whip-r {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(14deg) scale(1.08); }}
    }}
</style>
</head>
<body>
<div class="scene" id="scene">
    <!-- Floating particles -->
    <div class="particles" id="particles"></div>

    <!-- Omnitrix Watch -->
    <div class="watch-container" id="watch" onclick="activateOmnitrix()" title="Click to transform!">
        <div class="watch-strap"></div>
        <div class="watch-ring"></div>
        <div class="dial" id="dial">
            <svg class="hourglass" viewBox="0 0 60 70">
                <path d="M10,5 L50,5 L50,10 L35,30 L35,40 L50,60 L50,65 L10,65 L10,60 L25,40 L25,30 L10,10 Z"/>
            </svg>
            <div class="dial-silhouette-name">{alien['name']}</div>
        </div>
        <div class="flash-overlay" id="flash"></div>
        <div class="energy-ring" id="ring1"></div>
        <div class="energy-ring" id="ring2"></div>
        <div class="energy-ring" id="ring3"></div>
    </div>

    <div class="tap-hint" id="hint">⚡ TAP THE OMNITRIX TO TRANSFORM ⚡</div>

    <!-- Alien Result Card -->
    <div class="alien-result" id="alienCard">
        <div class="tf-banner">⚡ TRANSFORMATION COMPLETE ⚡</div>
        <div class="alien-graphic-box">
            {alien_svg}
        </div>
        <div class="ar-name">{alien['name'].upper()}</div>
        <div class="ar-meta">
            <span class="ar-type">⚡ {alien['power_type']}</span>
            <span class="ar-planet">🌍 {alien['planet']}</span>
        </div>
        <div class="ar-desc">{alien['description']}</div>
        <div class="tf-stats-container">
            {stats_html}
        </div>
        <button class="revert-btn" onclick="revertOmnitrix()">↩ REVERT TO WATCH</button>
    </div>
</div>

<script>
    // Generate floating ambient particles
    const particlesEl = document.getElementById('particles');
    for (let i = 0; i < 22; i++) {{
        const p = document.createElement('div');
        p.className = 'particle';
        p.style.left = Math.random() * 440 + 'px';
        p.style.top = Math.random() * 380 + 'px';
        p.style.animationDelay = (Math.random() * 3) + 's';
        p.style.animationDuration = (2 + Math.random() * 2) + 's';
        particlesEl.appendChild(p);
    }}

    let isAnimating = false;
    let autoRevertTimer = null;

    function activateOmnitrix() {{
        if (isAnimating) return;
        isAnimating = true;

        const watch = document.getElementById('watch');
        const flash = document.getElementById('flash');
        const alienCard = document.getElementById('alienCard');
        const hint = document.getElementById('hint');
        const rings = [document.getElementById('ring1'), document.getElementById('ring2'), document.getElementById('ring3')];

        // Step 1: Press down mechanically
        watch.classList.add('pressing');
        hint.style.opacity = '0';

        setTimeout(() => {{
            // Step 2: Spin dial + energy burst
            watch.classList.remove('pressing');
            watch.classList.add('transforming');
            flash.classList.add('active');
            rings.forEach(r => r.classList.add('active'));
        }}, 300);

        setTimeout(() => {{
            // Step 3: Hide watch dial and display the animated alien
            watch.style.opacity = '0';
            watch.style.pointerEvents = 'none';
            alienCard.classList.remove('timeout');
            alienCard.classList.add('show');
        }}, 850);

        // Step 4: Auto timeout back to watch after 12 seconds
        autoRevertTimer = setTimeout(() => {{
            revertOmnitrix();
        }}, 12000);
    }}

    function revertOmnitrix() {{
        if (autoRevertTimer) clearTimeout(autoRevertTimer);

        const watch = document.getElementById('watch');
        const flash = document.getElementById('flash');
        const alienCard = document.getElementById('alienCard');
        const hint = document.getElementById('hint');
        const rings = [document.getElementById('ring1'), document.getElementById('ring2'), document.getElementById('ring3')];

        alienCard.classList.remove('show');
        alienCard.classList.add('timeout');

        setTimeout(() => {{
            alienCard.classList.remove('timeout');
            alienCard.style.opacity = '0';
            alienCard.style.transform = 'scale(0.65) translateY(50px)';
            
            // Force reflow
            void alienCard.offsetWidth;
            alienCard.style.opacity = '';
            alienCard.style.transform = '';

            watch.style.opacity = '1';
            watch.style.pointerEvents = 'auto';
            watch.classList.remove('pressing', 'transforming');
            flash.classList.remove('active');
            rings.forEach(r => r.classList.remove('active'));
            hint.style.opacity = '1';
            isAnimating = false;
        }}, 650);
    }}
</script>
</body>
</html>
"""
