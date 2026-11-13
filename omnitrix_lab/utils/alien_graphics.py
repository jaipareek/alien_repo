"""
alien_graphics.py — Animated SVG illustrations for all 12 Ben 10 aliens.
Built with pure SVG + CSS animations (no copyrighted image files).
"""

import re


def get_alien_svg(alien_name):
    """Return the complete animated SVG for the given Ben 10 alien, stripped of comments and minified."""
    name = str(alien_name).strip()

    if name == "Four Arms":
        raw = _svg_four_arms()
    elif name == "Heatblast":
        raw = _svg_heatblast()
    elif name == "XLR8":
        raw = _svg_xlr8()
    elif name == "Diamondhead":
        raw = _svg_diamondhead()
    elif name == "Upgrade":
        raw = _svg_upgrade()
    elif name == "Ghostfreak":
        raw = _svg_ghostfreak()
    elif name == "Wildmutt":
        raw = _svg_wildmutt()
    elif name == "Cannonbolt":
        raw = _svg_cannonbolt()
    elif name == "Stinkfly":
        raw = _svg_stinkfly()
    elif name == "Ripjaws":
        raw = _svg_ripjaws()
    elif name == "Grey Matter":
        raw = _svg_grey_matter()
    elif name == "Wildvine":
        raw = _svg_wildvine()
    else:
        raw = _svg_generic(name)

    # Strip all HTML comments (which break markdown parsers) and minify
    no_comments = re.sub(r'<!--.*?-->', '', raw, flags=re.DOTALL)
    return "".join(line.strip() for line in no_comments.splitlines())


def _svg_four_arms():
    """Four Arms — 4 red muscular arms, 4 yellow eyes, massive warrior build."""
    return """
    <svg class="alien-svg four-arms-anim" viewBox="0 0 280 280" width="240" height="240">
        <defs>
            <radialGradient id="faAura" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#ff2222" stop-opacity="0.5"/>
                <stop offset="100%" stop-color="#ff0000" stop-opacity="0"/>
            </radialGradient>
            <linearGradient id="faRed" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ff3b3b"/>
                <stop offset="100%" stop-color="#990000"/>
            </linearGradient>
            <linearGradient id="faDarkRed" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#b30000"/>
                <stop offset="100%" stop-color="#590000"/>
            </linearGradient>
        </defs>

        <!-- Red Power Aura -->
        <circle cx="140" cy="140" r="125" fill="url(#faAura)" class="fa-aura-pulse"/>
        
        <!-- Shockwave rings -->
        <circle cx="140" cy="230" r="30" fill="none" stroke="#ff3333" stroke-width="3" class="fa-ground-ring"/>
        <circle cx="140" cy="230" r="55" fill="none" stroke="#ff6666" stroke-width="2" class="fa-ground-ring" style="animation-delay:0.2s"/>

        <!-- Upper Left Arm (Flexed/Punching) -->
        <g class="fa-arm-top-left">
            <path d="M 115 110 Q 70 70 65 35 Q 90 25 110 70 Z" fill="url(#faRed)"/>
            <circle cx="65" cy="35" r="18" fill="url(#faDarkRed)"/>
            <!-- Knuckles -->
            <rect x="52" y="24" width="24" height="12" rx="4" fill="#ff4d4d"/>
        </g>

        <!-- Upper Right Arm (Flexed/Punching) -->
        <g class="fa-arm-top-right">
            <path d="M 165 110 Q 210 70 215 35 Q 190 25 170 70 Z" fill="url(#faRed)"/>
            <circle cx="215" cy="35" r="18" fill="url(#faDarkRed)"/>
            <!-- Knuckles -->
            <rect x="204" y="24" width="24" height="12" rx="4" fill="#ff4d4d"/>
        </g>

        <!-- Lower Left Arm (Forward Jab) -->
        <g class="fa-arm-bot-left">
            <path d="M 110 145 Q 60 145 40 170 Q 55 190 95 165 Z" fill="url(#faRed)"/>
            <circle cx="38" cy="172" r="16" fill="url(#faDarkRed)"/>
            <rect x="25" y="164" width="20" height="14" rx="4" fill="#ff4d4d"/>
        </g>

        <!-- Lower Right Arm (Forward Jab) -->
        <g class="fa-arm-bot-right">
            <path d="M 170 145 Q 220 145 240 170 Q 225 190 185 165 Z" fill="url(#faRed)"/>
            <circle cx="242" cy="172" r="16" fill="url(#faDarkRed)"/>
            <rect x="235" y="164" width="20" height="14" rx="4" fill="#ff4d4d"/>
        </g>

        <!-- Muscular Legs -->
        <path d="M 110 200 L 95 255 L 125 255 L 132 205 Z" fill="#0d0d0d"/>
        <path d="M 170 200 L 185 255 L 155 255 L 148 205 Z" fill="#0d0d0d"/>
        <!-- Boots -->
        <rect x="88" y="250" width="38" height="12" rx="4" fill="#1f1f1f"/>
        <rect x="154" y="250" width="38" height="12" rx="4" fill="#1f1f1f"/>

        <!-- Massive Torso -->
        <path d="M 105 105 L 175 105 L 168 200 L 112 200 Z" fill="url(#faRed)"/>
        <!-- White Tank Top Stripe -->
        <polygon points="128,105 152,105 146,200 134,200" fill="#ffffff"/>
        <!-- Black Center Line -->
        <line x1="140" y1="105" x2="140" y2="200" stroke="#000000" stroke-width="4"/>

        <!-- Broad Shoulders -->
        <ellipse cx="140" cy="110" rx="45" ry="18" fill="url(#faRed)"/>

        <!-- Omnitrix Badge on Left Shoulder -->
        <g transform="translate(112, 106) scale(0.7)">
            <circle cx="10" cy="10" r="12" fill="#111111" stroke="#39ff14" stroke-width="2"/>
            <polygon points="5,5 15,5 10,10" fill="#39ff14"/>
            <polygon points="5,15 15,15 10,10" fill="#39ff14"/>
        </g>

        <!-- Head -->
        <path d="M 125 72 Q 140 50 155 72 L 152 105 L 128 105 Z" fill="url(#faRed)"/>
        <!-- Black Forehead Stripe -->
        <line x1="140" y1="52" x2="140" y2="82" stroke="#000000" stroke-width="4"/>
        <!-- Black Chin Stripe -->
        <line x1="140" y1="92" x2="140" y2="105" stroke="#000000" stroke-width="3"/>

        <!-- 4 Eyes (Two Top, Two Bottom) -->
        <ellipse cx="132" cy="74" rx="4" ry="3" fill="#ffe600"/>
        <ellipse cx="148" cy="74" rx="4" ry="3" fill="#ffe600"/>
        <ellipse cx="134" cy="84" rx="3.5" ry="2.5" fill="#ffe600"/>
        <ellipse cx="146" cy="84" rx="3.5" ry="2.5" fill="#ffe600"/>
        
        <!-- Fierce Brow -->
        <path d="M 128 70 L 138 73 L 142 73 L 152 70" stroke="#400000" stroke-width="2" fill="none"/>
    </svg>
    """


def _svg_heatblast():
    """Heatblast — Magma rock body crowned with raging animated flames."""
    return """
    <svg class="alien-svg heatblast-anim" viewBox="0 0 280 280" width="240" height="240">
        <defs>
            <radialGradient id="hbGlow" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#ff7700" stop-opacity="0.6"/>
                <stop offset="100%" stop-color="#ff0000" stop-opacity="0"/>
            </radialGradient>
            <linearGradient id="magmaRock" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#3d1d11"/>
                <stop offset="100%" stop-color="#1a0a05"/>
            </linearGradient>
            <linearGradient id="fireGrad" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="#ff2200"/>
                <stop offset="50%" stop-color="#ff9900"/>
                <stop offset="100%" stop-color="#ffff55"/>
            </linearGradient>
        </defs>

        <circle cx="140" cy="140" r="120" fill="url(#hbGlow)" class="hb-heat-pulse"/>

        <!-- Flame Jets from Hands -->
        <g class="hb-hand-flames-left">
            <path d="M 50 140 Q 20 120 15 90 Q 40 105 55 130 Z" fill="url(#fireGrad)"/>
            <circle cx="25" cy="100" r="5" fill="#ffff88"/>
        </g>
        <g class="hb-hand-flames-right">
            <path d="M 230 140 Q 260 120 265 90 Q 240 105 225 130 Z" fill="url(#fireGrad)"/>
            <circle cx="255" cy="100" r="5" fill="#ffff88"/>
        </g>

        <!-- Head Fire Crown (Animated) -->
        <g class="hb-head-fire">
            <path d="M 120 90 Q 110 30 140 15 Q 170 30 160 90 Z" fill="url(#fireGrad)"/>
            <path d="M 130 85 Q 140 35 150 45 Q 155 70 145 85 Z" fill="#ffffff" opacity="0.8"/>
            <path d="M 112 80 Q 95 45 118 40 Q 128 60 122 80 Z" fill="url(#fireGrad)"/>
            <path d="M 168 80 Q 185 45 162 40 Q 152 60 158 80 Z" fill="url(#fireGrad)"/>
        </g>

        <!-- Arms (Magma Rock) -->
        <path d="M 115 110 Q 75 120 50 145 Q 70 160 105 130 Z" fill="url(#magmaRock)"/>
        <path d="M 165 110 Q 205 120 230 145 Q 210 160 175 130 Z" fill="url(#magmaRock)"/>

        <!-- Lava Fissures on Arms -->
        <path d="M 75 125 L 85 140 L 95 135" stroke="#ff9900" stroke-width="3" fill="none"/>
        <path d="M 205 125 L 195 140 L 185 135" stroke="#ff9900" stroke-width="3" fill="none"/>

        <!-- Legs (Magma Rock) -->
        <path d="M 115 190 L 100 250 L 125 250 L 132 195 Z" fill="url(#magmaRock)"/>
        <path d="M 165 190 L 180 250 L 155 250 L 148 195 Z" fill="url(#magmaRock)"/>

        <!-- Torso (Charred Lava Rock) -->
        <path d="M 110 100 L 170 100 L 160 195 L 120 195 Z" fill="url(#magmaRock)"/>

        <!-- Glowing Lava Fissures on Chest -->
        <path d="M 140 105 L 140 190" stroke="#ffaa00" stroke-width="5" stroke-linecap="round"/>
        <path d="M 125 120 L 155 135" stroke="#ff7700" stroke-width="4"/>
        <path d="M 155 150 L 125 165" stroke="#ff7700" stroke-width="4"/>

        <!-- Face Mask Plate -->
        <polygon points="126,75 154,75 148,105 132,105" fill="#1a0a05"/>
        <!-- Glowing White-Yellow Eyes -->
        <polygon points="132,84 138,84 136,88 133,88" fill="#ffffff" filter="drop-shadow(0 0 3px #ffff00)"/>
        <polygon points="142,84 148,84 147,88 144,88" fill="#ffffff" filter="drop-shadow(0 0 3px #ffff00)"/>

        <!-- Omnitrix Center Chest -->
        <circle cx="140" cy="145" r="10" fill="#111" stroke="#39ff14" stroke-width="2"/>
        <polygon points="136,140 144,140 140,145" fill="#39ff14"/>
        <polygon points="136,150 144,150 140,145" fill="#39ff14"/>
    </svg>
    """


def _svg_xlr8():
    """XLR8 — Sleek raptor speedster with conical helmet and motion streaks."""
    return """
    <svg class="alien-svg xlr8-anim" viewBox="0 0 280 280" width="240" height="240">
        <defs>
            <linearGradient id="xlrBlue" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#00e5ff"/>
                <stop offset="100%" stop-color="#006699"/>
            </linearGradient>
        </defs>

        <!-- Speed streaks behind -->
        <g class="xlr-speed-streaks">
            <line x1="20" y1="80" x2="90" y2="80" stroke="#00e5ff" stroke-width="3" stroke-dasharray="15 5"/>
            <line x1="10" y1="130" x2="110" y2="130" stroke="#39ff14" stroke-width="4" stroke-dasharray="25 8"/>
            <line x1="30" y1="180" x2="80" y2="180" stroke="#00e5ff" stroke-width="3" stroke-dasharray="10 5"/>
            <line x1="5" y1="220" x2="95" y2="220" stroke="#39ff14" stroke-width="2" stroke-dasharray="20 6"/>
        </g>

        <!-- Tail (Swishing) -->
        <path d="M 125 180 Q 80 190 55 170 Q 75 205 130 195 Z" fill="#111111" class="xlr-tail"/>

        <!-- Legs with Roller-Balls -->
        <path d="M 125 175 L 110 240 L 125 240" stroke="#00e5ff" stroke-width="8" fill="none" stroke-linecap="round"/>
        <path d="M 155 175 L 170 240 L 155 240" stroke="#111111" stroke-width="8" fill="none" stroke-linecap="round"/>
        <!-- Spherical Feet (Wheel Orbs) -->
        <circle cx="118" cy="245" r="12" fill="#222222" stroke="#00e5ff" stroke-width="3"/>
        <circle cx="162" cy="245" r="12" fill="#222222" stroke="#00e5ff" stroke-width="3"/>

        <!-- Slender Aerodynamic Torso -->
        <path d="M 125 110 L 160 110 L 155 185 L 128 185 Z" fill="#111111"/>
        <path d="M 132 110 L 152 110 L 148 185 L 135 185 Z" fill="url(#xlrBlue)"/>

        <!-- Omnitrix Chest Emblem -->
        <circle cx="142" cy="130" r="9" fill="#000" stroke="#39ff14" stroke-width="2"/>
        <polygon points="138,126 146,126 142,130" fill="#39ff14"/>
        <polygon points="138,134 146,134 142,130" fill="#39ff14"/>

        <!-- Scythe-Clawed Arms -->
        <path d="M 125 120 Q 95 130 85 160 L 92 162 L 105 135 Z" fill="#111111"/>
        <path d="M 158 120 Q 185 130 195 160 L 188 162 L 175 135 Z" fill="#111111"/>
        <!-- Scythe Fingers -->
        <polygon points="85,160 80,180 90,165" fill="#00e5ff"/>
        <polygon points="195,160 200,180 190,165" fill="#00e5ff"/>

        <!-- Pointed Conical Helmet (Aerodynamic) -->
        <path d="M 125 90 L 160 90 L 175 40 Q 140 25 110 50 Z" fill="#111111"/>
        <path d="M 130 85 L 155 85 L 165 48 Q 140 38 120 55 Z" fill="url(#xlrBlue)"/>

        <!-- Glowing Green Visor Slit -->
        <path d="M 135 70 L 162 65" stroke="#39ff14" stroke-width="5" stroke-linecap="round" filter="drop-shadow(0 0 6px #39ff14)"/>
    </svg>
    """


def _svg_diamondhead():
    """Diamondhead — Crystalline Petrosapien with back shards and blade arms."""
    return """
    <svg class="alien-svg diamond-anim" viewBox="0 0 280 280" width="240" height="240">
        <defs>
            <linearGradient id="crystalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#bbfbfb"/>
                <stop offset="50%" stop-color="#40e0d0"/>
                <stop offset="100%" stop-color="#008080"/>
            </linearGradient>
            <linearGradient id="crystalDark" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#00a896"/>
                <stop offset="100%" stop-color="#024545"/>
            </linearGradient>
        </defs>

        <!-- Crystal Back Spikes (Giant Shards) -->
        <polygon points="110,110 60,30 95,95" fill="url(#crystalGrad)" class="dh-shard-left"/>
        <polygon points="170,110 220,30 185,95" fill="url(#crystalGrad)" class="dh-shard-right"/>

        <!-- Sparkle Glints -->
        <g class="dh-sparkle-1" transform="translate(60, 30)">
            <polygon points="0,-12 3,-3 12,0 3,3 0,12 -3,3 -12,0 -3,-3" fill="#ffffff"/>
        </g>
        <g class="dh-sparkle-2" transform="translate(220, 30)">
            <polygon points="0,-10 2,-2 10,0 2,2 0,10 -2,2 -10,0 -2,-2" fill="#ffffff"/>
        </g>

        <!-- Crystal Blade Arms -->
        <polygon points="110,115 55,145 40,195 70,175 105,135" fill="url(#crystalGrad)" class="dh-blade-left"/>
        <polygon points="170,115 225,145 240,195 210,175 175,135" fill="url(#crystalGrad)" class="dh-blade-right"/>

        <!-- Legs (Faceted Crystal) -->
        <polygon points="110,190 95,255 125,255 132,195" fill="url(#crystalDark)"/>
        <polygon points="170,190 185,255 155,255 148,195" fill="url(#crystalDark)"/>

        <!-- Prismatic Torso -->
        <polygon points="105,105 175,105 160,195 120,195" fill="url(#crystalGrad)"/>
        <!-- Chest Facet Lines -->
        <polygon points="120,105 140,140 160,105" fill="#e0ffff" opacity="0.6"/>
        <polygon points="140,140 120,195 160,195" fill="#005a5a" opacity="0.5"/>

        <!-- Omnitrix Badge -->
        <circle cx="140" cy="155" r="9" fill="#000" stroke="#39ff14" stroke-width="2"/>
        <polygon points="136,151 144,151 140,155" fill="#39ff14"/>
        <polygon points="136,159 144,159 140,155" fill="#39ff14"/>

        <!-- Angular Crystal Head -->
        <polygon points="122,65 140,40 158,65 152,105 128,105" fill="url(#crystalGrad)"/>
        <!-- Glowing Yellow Eyes -->
        <polygon points="130,75 137,75 135,78 131,78" fill="#ffff00"/>
        <polygon points="143,75 150,75 149,78 145,78" fill="#ffff00"/>
    </svg>
    """


def _svg_upgrade():
    """Upgrade — Galvanic Mechamorph with pulsing green circuit network."""
    return """
    <svg class="alien-svg upgrade-anim" viewBox="0 0 280 280" width="240" height="240">
        <defs>
            <radialGradient id="upEyeGlow" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#39ff14"/>
                <stop offset="60%" stop-color="#1a8a0a"/>
                <stop offset="100%" stop-color="#000000"/>
            </radialGradient>
        </defs>

        <!-- Digital Grid Platform -->
        <ellipse cx="140" cy="250" rx="90" ry="18" fill="none" stroke="#39ff14" stroke-width="1.5" stroke-dasharray="8 4" opacity="0.6"/>

        <!-- Techno-organic Arms -->
        <path d="M 115 115 Q 75 135 60 175 Q 75 185 105 140 Z" fill="#0f141c"/>
        <path d="M 165 115 Q 205 135 220 175 Q 205 185 175 140 Z" fill="#0f141c"/>

        <!-- Legs -->
        <path d="M 115 195 L 105 250 L 125 250 L 132 200 Z" fill="#0f141c"/>
        <path d="M 165 195 L 175 250 L 155 250 L 148 200 Z" fill="#0f141c"/>

        <!-- Smooth Rounded Body -->
        <path d="M 110 105 Q 140 95 170 105 L 165 200 L 115 200 Z" fill="#0f141c"/>

        <!-- Circuit Trace Network (Animated Glow) -->
        <g class="up-circuits">
            <path d="M 140 120 L 140 185" stroke="#39ff14" stroke-width="3" fill="none"/>
            <path d="M 140 145 L 90 145 L 75 170" stroke="#39ff14" stroke-width="2" fill="none"/>
            <path d="M 140 145 L 190 145 L 205 170" stroke="#39ff14" stroke-width="2" fill="none"/>
            <path d="M 140 175 L 115 235" stroke="#39ff14" stroke-width="2" fill="none"/>
            <path d="M 140 175 L 165 235" stroke="#39ff14" stroke-width="2" fill="none"/>
            <!-- Circuit Nodes -->
            <circle cx="90" cy="145" r="4" fill="#39ff14"/>
            <circle cx="190" cy="145" r="4" fill="#39ff14"/>
            <circle cx="75" cy="170" r="3" fill="#39ff14"/>
            <circle cx="205" cy="170" r="3" fill="#39ff14"/>
        </g>

        <!-- Head Dome -->
        <path d="M 120 70 Q 140 45 160 70 L 155 105 L 125 105 Z" fill="#0f141c"/>

        <!-- Central Circular Optic Eye (Rippling concentric rings) -->
        <circle cx="140" cy="75" r="16" fill="url(#upEyeGlow)" class="up-eye-ring"/>
        <circle cx="140" cy="75" r="10" fill="#0f141c" stroke="#39ff14" stroke-width="2"/>
        <circle cx="140" cy="75" r="5" fill="#39ff14" class="up-eye-pupil"/>

        <!-- Omnitrix Chest Emblem -->
        <circle cx="140" cy="120" r="8" fill="#000" stroke="#39ff14" stroke-width="2"/>
        <polygon points="137,117 143,117 140,120" fill="#39ff14"/>
        <polygon points="137,123 143,123 140,120" fill="#39ff14"/>
    </svg>
    """


def _svg_ghostfreak():
    """Ghostfreak — Swirling spectral phantom with track-sliding eye."""
    return """
    <svg class="alien-svg ghost-anim" viewBox="0 0 280 280" width="240" height="240">
        <defs>
            <radialGradient id="gfAura" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#9933ff" stop-opacity="0.4"/>
                <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
            </radialGradient>
        </defs>

        <circle cx="140" cy="140" r="120" fill="url(#gfAura)" class="gf-aura"/>

        <!-- Writhing Chest Tentacles -->
        <g class="gf-tentacles">
            <path d="M 130 150 Q 90 170 80 210 Q 95 190 135 160 Z" fill="#660099"/>
            <path d="M 150 150 Q 190 170 200 210 Q 185 190 145 160 Z" fill="#660099"/>
        </g>

        <!-- Wisping Phantom Body -->
        <g class="gf-floating-body">
            <!-- Tattered ghost tails -->
            <path d="M 110 90 Q 90 140 100 210 Q 115 240 120 200 Q 135 245 140 195 Q 155 240 160 205 Q 175 235 180 180 Q 190 140 170 90 Z" fill="#c4c9d1"/>
            
            <!-- Curving Black Eye Track Lines -->
            <path d="M 125 50 Q 145 75 130 115 Q 165 145 150 185" stroke="#222222" stroke-width="4" fill="none"/>

            <!-- Purple Cyclopic Eye (Moving on track) -->
            <g class="gf-eye-slider">
                <circle cx="138" cy="80" r="10" fill="#220033" stroke="#aa00ff" stroke-width="2"/>
                <circle cx="138" cy="80" r="5" fill="#ff00ff"/>
                <circle cx="139" cy="79" r="2" fill="#ffffff"/>
            </g>

            <!-- Omnitrix Chest Emblem -->
            <circle cx="140" cy="140" r="8" fill="#111" stroke="#39ff14" stroke-width="2"/>
            <polygon points="137,137 143,137 140,140" fill="#39ff14"/>
            <polygon points="137,143 143,143 140,140" fill="#39ff14"/>
        </g>
    </svg>
    """


def _svg_wildmutt():
    """Wildmutt — Eyeless orange quad beast with shoulder gills and fangs."""
    return """
    <svg class="alien-svg wildmutt-anim" viewBox="0 0 280 280" width="240" height="240">
        <!-- Roaring Sonic Waves -->
        <g class="wm-sonic-waves">
            <path d="M 80 120 Q 50 140 80 160" fill="none" stroke="#ffaa00" stroke-width="3" opacity="0.8"/>
            <path d="M 60 110 Q 25 140 60 170" fill="none" stroke="#ff7700" stroke-width="3" opacity="0.6"/>
            <path d="M 40 100 Q -5 140 40 180" fill="none" stroke="#ff4400" stroke-width="3" opacity="0.4"/>
        </g>

        <!-- Back Legs -->
        <path d="M 180 160 Q 220 180 210 240 L 195 240 Q 200 190 170 175 Z" fill="#cc5500"/>
        
        <!-- Beast Body (Orange Fur Spine) -->
        <path d="M 90 140 Q 140 110 210 135 Q 230 160 210 180 Q 150 185 90 170 Z" fill="#ff6600"/>

        <!-- Spine Quills -->
        <polygon points="140,118 145,100 150,118" fill="#993300"/>
        <polygon points="165,122 170,105 175,122" fill="#993300"/>
        <polygon points="190,130 195,115 200,130" fill="#993300"/>

        <!-- Front Muscular Legs -->
        <path d="M 115 155 Q 105 200 95 245 L 115 245 Q 130 200 135 160 Z" fill="#ff7711"/>

        <!-- Claws -->
        <rect x="90" y="240" width="8" height="12" rx="3" fill="#ffffff"/>
        <rect x="100" y="240" width="8" height="12" rx="3" fill="#ffffff"/>
        <rect x="190" y="235" width="8" height="12" rx="3" fill="#ffffff"/>

        <!-- Fierce Eyeless Head & Open Maw -->
        <path d="M 120 115 Q 80 105 70 135 L 115 155 Z" fill="#ff6600"/>
        <!-- Gills on Shoulder -->
        <line x1="125" y1="125" x2="135" y2="140" stroke="#662200" stroke-width="3"/>
        <line x1="130" y1="120" x2="140" y2="135" stroke="#662200" stroke-width="3"/>
        <line x1="135" y1="115" x2="145" y2="130" stroke="#662200" stroke-width="3"/>

        <!-- Open Mouth & Razor Fangs -->
        <polygon points="70,135 95,145 75,152" fill="#440000"/>
        <!-- Upper Fangs -->
        <polygon points="72,135 76,143 80,136" fill="#ffffff"/>
        <polygon points="82,137 86,145 90,139" fill="#ffffff"/>
        <!-- Lower Fangs -->
        <polygon points="74,151 78,144 82,150" fill="#ffffff"/>

        <!-- Omnitrix Badge on Shoulder -->
        <circle cx="150" cy="140" r="9" fill="#111" stroke="#39ff14" stroke-width="2"/>
        <polygon points="146,136 154,136 150,140" fill="#39ff14"/>
        <polygon points="146,144 154,144 150,140" fill="#39ff14"/>
    </svg>
    """


def _svg_cannonbolt():
    """Cannonbolt — Bulky yellow and white armored juggernaut."""
    return """
    <svg class="alien-svg cannonbolt-anim" viewBox="0 0 280 280" width="240" height="240">
        <!-- Impact Shockwave -->
        <ellipse cx="140" cy="245" rx="85" ry="18" fill="none" stroke="#f1c40f" stroke-width="3" class="cb-shockwave"/>

        <!-- Heavy Armored Shell Backing -->
        <path d="M 85 90 Q 140 50 195 90 Q 220 160 195 220 Q 140 240 85 220 Q 60 160 85 90 Z" fill="#d4ac0d"/>

        <!-- Claws / Thick Arms -->
        <path d="M 85 130 Q 50 150 45 190 Q 70 200 95 160 Z" fill="#f4f6f7"/>
        <path d="M 195 130 Q 230 150 235 190 Q 210 200 185 160 Z" fill="#f4f6f7"/>
        <!-- Claw tips -->
        <polygon points="40,185 30,195 45,198" fill="#2c3e50"/>
        <polygon points="240,185 250,195 235,198" fill="#2c3e50"/>

        <!-- Thick Plated Legs -->
        <path d="M 100 205 L 90 250 L 120 250 L 125 215 Z" fill="#f4f6f7"/>
        <path d="M 180 205 L 190 250 L 160 250 L 155 215 Z" fill="#f4f6f7"/>

        <!-- White Front Carapace -->
        <path d="M 95 105 Q 140 90 185 105 L 175 210 Q 140 220 105 210 Z" fill="#ffffff"/>

        <!-- Yellow Segmented Shoulder Pads -->
        <ellipse cx="90" cy="105" rx="22" ry="32" fill="#f1c40f" stroke="#b7950b" stroke-width="3"/>
        <ellipse cx="190" cy="105" rx="22" ry="32" fill="#f1c40f" stroke="#b7950b" stroke-width="3"/>

        <!-- Broad Sloped Head -->
        <path d="M 120 85 Q 140 70 160 85 L 155 115 L 125 115 Z" fill="#ffffff"/>
        <!-- Yellow Eyes -->
        <circle cx="132" cy="98" r="4" fill="#f39c12"/>
        <circle cx="148" cy="98" r="4" fill="#f39c12"/>

        <!-- Omnitrix Chest Emblem -->
        <circle cx="140" cy="140" r="10" fill="#111" stroke="#39ff14" stroke-width="2"/>
        <polygon points="136,135 144,135 140,140" fill="#39ff14"/>
        <polygon points="136,145 144,145 140,140" fill="#39ff14"/>
    </svg>
    """


def _svg_stinkfly():
    """Stinkfly — 4-eyed insectoid with fluttering translucent wings."""
    return """
    <svg class="alien-svg stinkfly-anim" viewBox="0 0 280 280" width="240" height="240">
        <defs>
            <linearGradient id="sfWing" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#a8e6cf" stop-opacity="0.7"/>
                <stop offset="100%" stop-color="#1abc9c" stop-opacity="0.3"/>
            </linearGradient>
        </defs>

        <!-- Rapid Fluttering Wings -->
        <g class="sf-wings">
            <ellipse cx="75" cy="80" rx="65" ry="22" fill="url(#sfWing)" stroke="#39ff14" stroke-width="1.5" transform="rotate(-30 75 80)"/>
            <ellipse cx="70" cy="115" rx="50" ry="18" fill="url(#sfWing)" stroke="#39ff14" stroke-width="1" transform="rotate(-15 70 115)"/>
            <ellipse cx="205" cy="80" rx="65" ry="22" fill="url(#sfWing)" stroke="#39ff14" stroke-width="1.5" transform="rotate(30 205 80)"/>
            <ellipse cx="210" cy="115" rx="50" ry="18" fill="url(#sfWing)" stroke="#39ff14" stroke-width="1" transform="rotate(15 210 115)"/>
        </g>

        <!-- Long Scorpion-like Stinger Tail -->
        <path d="M 140 180 Q 155 230 185 240 Q 180 260 155 245 Q 130 230 135 180 Z" fill="#2e4053"/>
        <polygon points="185,240 205,245 180,255" fill="#e74c3c"/>

        <!-- Dropping Slime Particles -->
        <circle cx="195" cy="255" r="3" fill="#39ff14" class="sf-slime-drop"/>
        <circle cx="190" cy="265" r="2" fill="#39ff14" class="sf-slime-drop" style="animation-delay:0.3s"/>

        <!-- Slender Insect Legs -->
        <path d="M 125 150 L 95 190 L 80 230" stroke="#1c2833" stroke-width="4" fill="none"/>
        <path d="M 155 150 L 185 190 L 200 230" stroke="#1c2833" stroke-width="4" fill="none"/>

        <!-- Bug Thorax & Abdomen -->
        <ellipse cx="140" cy="145" rx="26" ry="40" fill="#2e4053"/>

        <!-- 4 Eyestalks (Two left, Two right) -->
        <path d="M 130 90 Q 100 70 95 55" stroke="#1c2833" stroke-width="4" fill="none"/>
        <path d="M 130 95 Q 90 90 85 80" stroke="#1c2833" stroke-width="4" fill="none"/>
        <path d="M 150 90 Q 180 70 185 55" stroke="#1c2833" stroke-width="4" fill="none"/>
        <path d="M 150 95 Q 190 90 195 80" stroke="#1c2833" stroke-width="4" fill="none"/>

        <!-- Glowing Orange Eyes on Stalks -->
        <circle cx="95" cy="55" r="7" fill="#f39c12" stroke="#e67e22" stroke-width="2"/>
        <circle cx="85" cy="80" r="7" fill="#f39c12" stroke="#e67e22" stroke-width="2"/>
        <circle cx="185" cy="55" r="7" fill="#f39c12" stroke="#e67e22" stroke-width="2"/>
        <circle cx="195" cy="80" r="7" fill="#f39c12" stroke="#e67e22" stroke-width="2"/>

        <!-- Head & Mandibles -->
        <circle cx="140" cy="98" r="16" fill="#1c2833"/>
        <polygon points="135,110 130,122 138,114" fill="#ecf0f1"/>
        <polygon points="145,110 150,122 142,114" fill="#ecf0f1"/>

        <!-- Omnitrix Emblem -->
        <circle cx="140" cy="140" r="8" fill="#000" stroke="#39ff14" stroke-width="2"/>
        <polygon points="137,137 143,137 140,140" fill="#39ff14"/>
        <polygon points="137,143 143,143 140,140" fill="#39ff14"/>
    </svg>
    """


def _svg_ripjaws():
    """Ripjaws — Menacing deep sea predator with glowing lure and snapping jaws."""
    return """
    <svg class="alien-svg ripjaws-anim" viewBox="0 0 280 280" width="240" height="240">
        <defs>
            <radialGradient id="rjLure" cx="50%" cy="50%" r="50%">
                <stop offset="0%" stop-color="#ffff55"/>
                <stop offset="70%" stop-color="#00ffcc"/>
                <stop offset="100%" stop-color="#006666" stop-opacity="0"/>
            </radialGradient>
        </defs>

        <!-- Bioluminescent Angler Lure (Dangling & Pulsing) -->
        <g class="rj-lure-group">
            <path d="M 140 60 Q 140 20 170 25 Q 185 30 180 50" stroke="#004d4d" stroke-width="3" fill="none"/>
            <circle cx="180" cy="52" r="14" fill="url(#rjLure)"/>
            <circle cx="180" cy="52" r="5" fill="#ffffff"/>
        </g>

        <!-- Dorsal Fin -->
        <polygon points="140,80 145,35 160,85" fill="#004d4d"/>

        <!-- Webbed Claws -->
        <path d="M 105 125 Q 65 140 50 180 Q 75 185 100 155 Z" fill="#006666"/>
        <path d="M 175 125 Q 215 140 230 180 Q 205 185 180 155 Z" fill="#006666"/>

        <!-- Tail Fin / Legs -->
        <path d="M 115 190 L 105 255 L 130 255 L 135 200 Z" fill="#004d4d"/>
        <path d="M 165 190 L 175 255 L 150 255 L 145 200 Z" fill="#004d4d"/>

        <!-- Aquatic Scaled Torso -->
        <path d="M 110 110 L 170 110 L 160 195 L 120 195 Z" fill="#006666"/>

        <!-- Snapping Razor Jaws (Animated) -->
        <g class="rj-jaws">
            <!-- Upper Jaw -->
            <path d="M 115 85 Q 140 65 165 85 L 160 105 L 120 105 Z" fill="#004d4d"/>
            <!-- Lower Jaw -->
            <path d="M 118 105 L 162 105 Q 140 130 118 105 Z" fill="#003333"/>
            <!-- Razor Sharp Teeth -->
            <polygon points="122,105 125,96 128,105" fill="#ffffff"/>
            <polygon points="130,105 133,94 136,105" fill="#ffffff"/>
            <polygon points="138,105 141,92 144,105" fill="#ffffff"/>
            <polygon points="146,105 149,94 152,105" fill="#ffffff"/>
            <polygon points="154,105 157,96 160,105" fill="#ffffff"/>
        </g>

        <!-- Black Cold Eyes -->
        <circle cx="128" cy="82" r="4" fill="#000000"/>
        <circle cx="152" cy="82" r="4" fill="#000000"/>

        <!-- Omnitrix Badge -->
        <circle cx="140" cy="140" r="9" fill="#000" stroke="#39ff14" stroke-width="2"/>
        <polygon points="136,136 144,136 140,140" fill="#39ff14"/>
        <polygon points="136,144 144,144 140,140" fill="#39ff14"/>
    </svg>
    """


def _svg_grey_matter():
    """Grey Matter — Tiny Galvan genius with huge intellect eyes & holographic rings."""
    return """
    <svg class="alien-svg greymatter-anim" viewBox="0 0 280 280" width="240" height="240">
        <!-- Holographic Data Rings -->
        <g class="gm-holo-rings">
            <ellipse cx="140" cy="130" rx="90" ry="35" fill="none" stroke="#39ff14" stroke-width="1.5" stroke-dasharray="10 5" opacity="0.6"/>
            <ellipse cx="140" cy="130" rx="70" ry="70" fill="none" stroke="#00e5ff" stroke-width="1" stroke-dasharray="4 8" opacity="0.5"/>
            <!-- Floating Data Dots -->
            <circle cx="65" cy="115" r="3" fill="#39ff14"/>
            <circle cx="215" cy="145" r="3" fill="#00e5ff"/>
        </g>

        <!-- Tiny Galvan Body in Green/White Suit -->
        <path d="M 125 155 L 155 155 L 150 220 L 130 220 Z" fill="#2c3e50"/>
        <!-- Thin Legs -->
        <path d="M 132 220 L 125 255 L 135 255" stroke="#7f8c8d" stroke-width="5" fill="none"/>
        <path d="M 148 220 L 155 255 L 145 255" stroke="#7f8c8d" stroke-width="5" fill="none"/>

        <!-- Thin Arms with 3-fingered hands -->
        <path d="M 125 160 Q 105 180 95 205" stroke="#7f8c8d" stroke-width="5" fill="none"/>
        <path d="M 155 160 Q 175 180 185 205" stroke="#7f8c8d" stroke-width="5" fill="none"/>

        <!-- Giant Bulging Galvan Cranium -->
        <g class="gm-head">
            <ellipse cx="140" cy="105" rx="42" ry="36" fill="#95a5a6"/>
            <!-- Cranial Wrinkles -->
            <path d="M 130 75 Q 140 70 150 75" stroke="#7f8c8d" stroke-width="2" fill="none"/>
            <path d="M 125 82 Q 140 78 155 82" stroke="#7f8c8d" stroke-width="2" fill="none"/>

            <!-- Gigantic Frog Eyes with Horizontal Pupils -->
            <circle cx="118" cy="105" r="16" fill="#2ecc71" stroke="#27ae60" stroke-width="2"/>
            <circle cx="162" cy="105" r="16" fill="#2ecc71" stroke="#27ae60" stroke-width="2"/>
            <!-- Horizontal Rectangular Slit Pupils -->
            <rect x="108" y="102" width="20" height="6" rx="2" fill="#000000"/>
            <rect x="152" y="102" width="20" height="6" rx="2" fill="#000000"/>
            <!-- Eye Glints -->
            <circle cx="124" cy="98" r="3" fill="#ffffff"/>
            <circle cx="168" cy="98" r="3" fill="#ffffff"/>
        </g>

        <!-- Omnitrix on Back / Chest -->
        <circle cx="140" cy="170" r="7" fill="#000" stroke="#39ff14" stroke-width="1.5"/>
        <polygon points="137,167 143,167 140,170" fill="#39ff14"/>
        <polygon points="137,173 143,173 140,170" fill="#39ff14"/>
    </svg>
    """


def _svg_wildvine():
    """Wildvine — One-eyed plant warrior with stretching thorny vines and flytrap cowl."""
    return """
    <svg class="alien-svg wildvine-anim" viewBox="0 0 280 280" width="240" height="240">
        <!-- Sprouting Thorny Vines (Swaying) -->
        <g class="wv-vines-left">
            <path d="M 115 130 Q 60 110 40 60 Q 30 110 90 145 Z" fill="#1e824c"/>
            <!-- Thorns -->
            <polygon points="50,80 35,70 52,90" fill="#d35400"/>
            <polygon points="70,110 55,100 72,120" fill="#d35400"/>
        </g>
        <g class="wv-vines-right">
            <path d="M 165 130 Q 220 110 240 60 Q 250 110 190 145 Z" fill="#1e824c"/>
            <!-- Thorns -->
            <polygon points="230,80 245,70 228,90" fill="#d35400"/>
            <polygon points="210,110 225,100 208,120" fill="#d35400"/>
        </g>

        <!-- Vine Roots / Legs -->
        <path d="M 120 190 Q 100 230 80 255 Q 110 245 130 200 Z" fill="#196f3d"/>
        <path d="M 160 190 Q 180 230 200 255 Q 170 245 150 200 Z" fill="#196f3d"/>
        <path d="M 140 195 L 140 255" stroke="#196f3d" stroke-width="8" stroke-linecap="round"/>

        <!-- Plant Stem Torso with Seed Pods -->
        <path d="M 115 110 L 165 110 L 155 195 L 125 195 Z" fill="#27ae60"/>
        <!-- Seed Pods on Back -->
        <circle cx="120" cy="140" r="8" fill="#e67e22"/>
        <circle cx="160" cy="140" r="8" fill="#e67e22"/>
        <circle cx="140" cy="165" r="8" fill="#e67e22"/>

        <!-- Venus Flytrap Head Cowl (Petals) -->
        <g class="wv-flytrap">
            <path d="M 105 95 Q 100 40 140 30 Q 180 40 175 95 Z" fill="#229954"/>
            <!-- Inside Purple Flytrap Cavity -->
            <path d="M 115 88 Q 112 48 140 42 Q 168 48 165 88 Z" fill="#8e44ad"/>
            <!-- Cowl Teeth/Spikes -->
            <polygon points="120,48 125,58 130,50" fill="#ffffff"/>
            <polygon points="135,44 140,55 145,44" fill="#ffffff"/>
            <polygon points="150,50 155,58 160,48" fill="#ffffff"/>
        </g>

        <!-- Giant Single Cyclopic Blue Eye -->
        <circle cx="140" cy="72" r="14" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
        <circle cx="140" cy="72" r="6" fill="#000000"/>
        <circle cx="143" cy="69" r="2.5" fill="#ffffff"/>

        <!-- Omnitrix Chest Emblem -->
        <circle cx="140" cy="130" r="9" fill="#000" stroke="#39ff14" stroke-width="2"/>
        <polygon points="136,126 144,126 140,130" fill="#39ff14"/>
        <polygon points="136,134 144,134 140,130" fill="#39ff14"/>
    </svg>
    """


def _svg_generic(name):
    """Fallback stylized alien emblem."""
    return f"""
    <svg class="alien-svg generic-anim" viewBox="0 0 280 280" width="240" height="240">
        <circle cx="140" cy="140" r="100" fill="#112211" stroke="#39ff14" stroke-width="4"/>
        <polygon points="90,70 190,70 140,140" fill="#39ff14"/>
        <polygon points="90,210 190,210 140,140" fill="#39ff14"/>
        <text x="140" y="145" font-family="'Orbitron', sans-serif" font-size="14" fill="#ffffff" text-anchor="middle">{name}</text>
    </svg>
    """

