"""
arena.py — Battle Arena page.
Turn-based battle game using alien stats and session state.
"""

import streamlit as st
import random
from utils.helpers import load_alien_data, render_section_title


# Villain roster (no official images — just names and stats)
VILLAINS = {
    "Vilgax": {"emoji": "👾", "hp": 300, "strength": 85, "speed": 40, "defense": 80, "intelligence": 75},
    "Kevin 11": {"emoji": "😈", "hp": 250, "strength": 75, "speed": 65, "defense": 60, "intelligence": 55},
    "Zs'Skayr": {"emoji": "💀", "hp": 200, "strength": 50, "speed": 70, "defense": 40, "intelligence": 90},
    "Hex": {"emoji": "🧙", "hp": 220, "strength": 45, "speed": 50, "defense": 55, "intelligence": 95},
}


def _init_battle_state():
    """Initialize battle session state variables."""
    defaults = {
        "battle_active": False,
        "player_hp": 0,
        "player_max_hp": 0,
        "villain_hp": 0,
        "villain_max_hp": 0,
        "player_alien": None,
        "villain_name": None,
        "villain_data": None,
        "battle_log": [],
        "battle_result": None,
        "player_defending": False,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val


def show():
    """Render the Battle Arena page."""
    render_section_title("⚔️ BATTLE ARENA")
    _init_battle_state()

    df = load_alien_data()

    # --- Setup Phase ---
    if not st.session_state.battle_active and st.session_state.battle_result is None:
        st.markdown(
            '<p style="color:#a0a0a0;">Choose your alien and a villain, then fight!</p>',
            unsafe_allow_html=True,
        )

        c1, c2 = st.columns(2)
        with c1:
            alien_name = st.selectbox("🦸 Your Alien", df["name"].tolist(), key="arena_alien")
        with c2:
            villain_name = st.selectbox("🦹 Villain", list(VILLAINS.keys()), key="arena_villain")

        if st.button("⚔️ START BATTLE", key="arena_start"):
            alien = df[df["name"] == alien_name].iloc[0]
            villain = VILLAINS[villain_name]

            # Compute HP from stats
            player_hp = 150 + alien["strength"] + alien["defense"]
            villain_hp = villain["hp"]

            st.session_state.battle_active = True
            st.session_state.player_hp = player_hp
            st.session_state.player_max_hp = player_hp
            st.session_state.villain_hp = villain_hp
            st.session_state.villain_max_hp = villain_hp
            st.session_state.player_alien = alien.to_dict()
            st.session_state.villain_name = villain_name
            st.session_state.villain_data = villain
            st.session_state.battle_log = [f"⚔️ {alien_name} vs {villain_name} — FIGHT!"]
            st.session_state.battle_result = None
            st.session_state.player_defending = False
            st.rerun()

    # --- Battle Phase ---
    elif st.session_state.battle_active:
        alien = st.session_state.player_alien
        villain = st.session_state.villain_data
        v_name = st.session_state.villain_name

        # Health bars
        _render_health_bars(alien, villain, v_name)

        # Action buttons
        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)

        with b1:
            if st.button("🗡️ ATTACK", key="arena_attack", use_container_width=True):
                _do_player_attack(alien, villain, v_name, is_special=False)
        with b2:
            if st.button("⚡ SPECIAL", key="arena_special", use_container_width=True):
                _do_player_attack(alien, villain, v_name, is_special=True)
        with b3:
            if st.button("🛡️ DEFEND", key="arena_defend", use_container_width=True):
                _do_defend(alien, villain, v_name)

        # Battle log
        st.markdown("---")
        render_section_title("📜 BATTLE LOG")
        for entry in reversed(st.session_state.battle_log[-8:]):
            st.markdown(f"<p style='color:#a0a0a0;font-size:0.9rem;margin:2px 0;'>{entry}</p>", unsafe_allow_html=True)

    # --- Result Phase ---
    if st.session_state.battle_result is not None:
        st.session_state.battle_active = False
        result = st.session_state.battle_result
        if result == "win":
            st.success("🏆 YOU WIN! Your alien defeated the villain!")
            st.balloons()
        else:
            st.error("💀 YOU LOST! The villain was too strong!")

        if st.button("🔄 PLAY AGAIN", key="arena_reset"):
            st.session_state.battle_active = False
            st.session_state.battle_result = None
            st.session_state.battle_log = []
            st.rerun()


def _render_health_bars(alien, villain, v_name):
    """Render health bars for player and villain."""
    p_hp = st.session_state.player_hp
    p_max = st.session_state.player_max_hp
    v_hp = st.session_state.villain_hp
    v_max = st.session_state.villain_max_hp

    p_pct = max(0, (p_hp / p_max) * 100)
    v_pct = max(0, (v_hp / v_max) * 100)

    p_color = "health-green" if p_pct > 50 else ("health-yellow" if p_pct > 25 else "health-red")
    v_color = "health-green" if v_pct > 50 else ("health-yellow" if v_pct > 25 else "health-red")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f'<div class="glass-card" style="text-align:center;">'
            f'<div style="font-size:2.5rem;">{alien["emoji"]}</div>'
            f'<div style="font-family:\'Orbitron\',sans-serif;color:#39ff14;font-size:1.1rem;letter-spacing:2px;">{alien["name"]}</div>'
            f'<div style="color:#a0a0a0;font-size:0.85rem;">HP: {max(0, p_hp)} / {p_max}</div>'
            f'<div class="health-bar-outer"><div class="health-bar-inner {p_color}" style="width:{p_pct}%;">{int(p_pct)}%</div></div>'
            f'</div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="glass-card" style="text-align:center;">'
            f'<div style="font-size:2.5rem;">{villain["emoji"]}</div>'
            f'<div style="font-family:\'Orbitron\',sans-serif;color:#ff4444;font-size:1.1rem;letter-spacing:2px;">{v_name}</div>'
            f'<div style="color:#a0a0a0;font-size:0.85rem;">HP: {max(0, v_hp)} / {v_max}</div>'
            f'<div class="health-bar-outer"><div class="health-bar-inner {v_color}" style="width:{v_pct}%;">{int(v_pct)}%</div></div>'
            f'</div>',
            unsafe_allow_html=True,
        )


def _do_player_attack(alien, villain, v_name, is_special):
    """Execute a player attack, then a villain counter-attack."""
    # Calculate player damage
    base = alien["strength"]
    if is_special:
        # Special uses strength + intelligence, but has variance
        raw = base + alien["intelligence"] * 0.5
        damage = int(raw * random.uniform(0.6, 1.2)) - villain["defense"] // 4
        label = "SPECIAL ATTACK"
    else:
        raw = base * random.uniform(0.7, 1.1)
        damage = int(raw) - villain["defense"] // 5
        label = "ATTACK"

    damage = max(5, damage)  # Minimum 5 damage
    st.session_state.villain_hp -= damage
    st.session_state.battle_log.append(f"🗡️ {alien['name']} uses {label} → {damage} damage to {v_name}!")

    # Check if villain defeated
    if st.session_state.villain_hp <= 0:
        st.session_state.villain_hp = 0
        st.session_state.battle_result = "win"
        st.session_state.battle_log.append(f"💥 {v_name} is defeated!")
        st.rerun()
        return

    # Villain counter-attack
    _villain_attack(alien, villain, v_name)


def _do_defend(alien, villain, v_name):
    """Defend reduces incoming damage this turn, then villain attacks."""
    st.session_state.player_defending = True
    st.session_state.battle_log.append(f"🛡️ {alien['name']} takes a defensive stance!")
    _villain_attack(alien, villain, v_name)
    st.session_state.player_defending = False


def _villain_attack(alien, villain, v_name):
    """Villain attacks the player."""
    raw = villain["strength"] * random.uniform(0.6, 1.1)
    defense_mod = alien["defense"] // 4
    if st.session_state.player_defending:
        defense_mod += alien["defense"] // 2  # Extra defense when defending

    damage = max(3, int(raw) - defense_mod)
    st.session_state.player_hp -= damage
    st.session_state.battle_log.append(f"👾 {v_name} strikes back → {damage} damage to {alien['name']}!")

    if st.session_state.player_hp <= 0:
        st.session_state.player_hp = 0
        st.session_state.battle_result = "lose"
        st.session_state.battle_log.append(f"💀 {alien['name']} is knocked out!")

    st.rerun()
