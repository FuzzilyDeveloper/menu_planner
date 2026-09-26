from __future__ import annotations

import streamlit as st


st.set_page_config(page_title="Crumb & Bloom | Menu planner", page_icon="CB", layout="wide")

INVENTORY = [
    {"item": "All-purpose flour", "category": "Dry goods", "stock": "18 kg", "level": "Healthy"},
    {"item": "European butter", "category": "Chilled", "stock": "6 kg", "level": "Healthy"},
    {"item": "Free-range eggs", "category": "Chilled", "stock": "42 pcs", "level": "Healthy"},
    {"item": "Whole milk", "category": "Chilled", "stock": "9 L", "level": "Healthy"},
    {"item": "Wildflower honey", "category": "Pantry", "stock": "1.4 kg", "level": "Low"},
    {"item": "Cocoa nibs", "category": "Pantry", "stock": "0.8 kg", "level": "Low"},
    {"item": "Blueberries", "category": "Produce", "stock": "2.5 kg", "level": "Healthy"},
    {"item": "Blood oranges", "category": "Produce", "stock": "3 kg", "level": "Healthy"},
    {"item": "Pistachios", "category": "Pantry", "stock": "1.2 kg", "level": "Low"},
    {"item": "Sourdough starter", "category": "Ferments", "stock": "2 kg", "level": "Healthy"},
]

MENU_LIBRARY = {
    "Bright & botanical": [
        {"name": "Blood orange morning bun", "type": "Pastry", "price": "$5.50", "accent": "tangerine", "tag": "Best seller", "description": "Laminated butter pastry, blood orange sugar and a glossy citrus finish.", "uses": "Butter, flour, blood oranges"},
        {"name": "Blueberry cloud danish", "type": "Pastry", "price": "$6.00", "accent": "lilac", "tag": "Seasonal", "description": "Vanilla cream, jammy blueberries and a crisp pistachio crumb.", "uses": "Blueberries, pistachios, eggs"},
        {"name": "Honey oat sourdough", "type": "Bread", "price": "$9.00", "accent": "sage", "tag": "Pantry hero", "description": "Naturally leavened loaf with wildflower honey and a tender, toasty crumb.", "uses": "Starter, honey, flour"},
    ],
    "Chocolate comfort": [
        {"name": "Cocoa nib morning bun", "type": "Pastry", "price": "$5.50", "accent": "cocoa", "tag": "New", "description": "Buttery laminated layers, dark cocoa sugar and crunchy cacao nibs.", "uses": "Butter, cocoa nibs, flour"},
        {"name": "Brown butter chocolate loaf", "type": "Cake", "price": "$7.00", "accent": "plum", "tag": "Staff pick", "description": "Deep chocolate crumb, brown butter glaze and a pinch of flaky salt.", "uses": "Butter, eggs, cocoa nibs"},
        {"name": "Honey milk bun", "type": "Bread", "price": "$4.50", "accent": "sage", "tag": "Soft bake", "description": "Pillowy milk bread brushed with warm wildflower honey.", "uses": "Milk, honey, flour"},
    ],
    "Weekend brunch": [
        {"name": "Blueberry breakfast cake", "type": "Cake", "price": "$6.50", "accent": "lilac", "tag": "Weekend only", "description": "Buttermilk crumb, blueberry pockets and a bright lemon sugar crust.", "uses": "Blueberries, eggs, milk"},
        {"name": "Pistachio morning croissant", "type": "Pastry", "price": "$6.50", "accent": "sage", "tag": "Limited", "description": "Classic laminated croissant filled with pistachio frangipane.", "uses": "Pistachios, butter, eggs"},
        {"name": "Orange blossom loaf", "type": "Cake", "price": "$7.00", "accent": "tangerine", "tag": "Bright bite", "description": "Tender citrus loaf with a delicate orange blossom glaze.", "uses": "Blood oranges, milk, flour"},
    ],
}


def inject_styles() -> None:
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Fraunces:opsz,wght@9..144,500;9..144,650;9..144,700&family=Manrope:wght@400;500;600;700;800&display=swap');
    :root { --ink:#27221e; --muted:#776d64; --paper:#fcf8f2; --line:#ded1c1; --coral:#e86f51; }
    .stApp { background:radial-gradient(circle at 100% 0%, #f4d8bd 0, #fcf8f2 32rem), var(--paper); color:var(--ink); }
    [data-testid="stSidebar"] { background:#27221e; border-right:0; }
    [data-testid="stSidebar"] * { color:#f9eee3; }
    h1,h2,h3 { font-family:'Fraunces', Georgia, serif !important; color:var(--ink); letter-spacing:0 !important; }
    h1 { font-size:3.2rem !important; line-height:1.03 !important; margin:.2rem 0 .4rem !important; }
    h2 { font-size:1.65rem !important; }
    p, label, .stMarkdown { font-family:'Manrope', sans-serif; }
    .eyebrow { color:var(--coral); font:700 .72rem 'DM Mono', monospace; letter-spacing:.09em; text-transform:uppercase; }
    .topline { display:flex; justify-content:space-between; align-items:flex-end; gap:1rem; margin-bottom:1.5rem; }
    .date-stamp { color:var(--muted); font:500 .75rem 'DM Mono', monospace; text-align:right; }
    .hero { background:#e9dfd0; border:1px solid #d9c9b5; padding:1.4rem 1.6rem; border-radius:16px; margin:1.2rem 0 1.4rem; position:relative; overflow:hidden; }
    .hero:after { content:'BAKE\\A WITH\\A INTENT'; white-space:pre; position:absolute; right:1.8rem; top:1.1rem; color:#c8b8a5; font:700 2.6rem/.9 'DM Mono', monospace; text-align:right; }
    .hero p { max-width:38rem; color:#685d53; margin:0; position:relative; z-index:1; }
    .metric { background:#fffaf4; border:1px solid var(--line); border-radius:12px; padding:1rem 1.1rem; min-height:6.7rem; }
    .metric-label { color:var(--muted); font:500 .68rem 'DM Mono',monospace; text-transform:uppercase; letter-spacing:.06em; }
    .metric-value { font:700 1.7rem 'Fraunces',serif; margin:.45rem 0 .15rem; }
    .metric-note { font-size:.75rem; color:#5f8462; }
    .menu-card { background:#fffaf4; border:1px solid var(--line); border-radius:14px; overflow:hidden; height:100%; box-shadow:0 8px 22px rgba(67,45,26,.05); }
    .menu-card .colour { height:8px; }
    .menu-card .body { padding:1rem 1.1rem 1.1rem; }
    .menu-card .type { color:var(--muted); font:500 .66rem 'DM Mono',monospace; text-transform:uppercase; }
    .menu-card h3 { font-size:1.3rem !important; margin:.55rem 0 .45rem !important; }
    .menu-card p { color:#645a52; font-size:.79rem; line-height:1.5; min-height:3.6rem; }
    .pill { display:inline-block; border-radius:99px; padding:.26rem .55rem; background:#efe3d3; color:#6d4f38; font:600 .64rem 'DM Mono',monospace; }
    .uses { border-top:1px solid #eee3d7; margin-top:.75rem; padding-top:.7rem; color:#8b7c6d; font-size:.68rem; }
    .section-label { color:var(--muted); font:700 .7rem 'DM Mono',monospace; text-transform:uppercase; letter-spacing:.08em; margin:1.5rem 0 .7rem; }
    .insight { background:#dce8d7; border-radius:12px; padding:1rem 1.1rem; color:#37523a; font-size:.82rem; line-height:1.5; }
    .small-copy { color:var(--muted); font-size:.83rem; }
    .stButton > button { border-radius:8px; font-family:'Manrope',sans-serif; font-weight:700; border:1px solid #c9b9a8; color:var(--ink); background:#fffaf4; }
    .stButton > button[kind="primary"] { background:var(--coral); border-color:var(--coral); color:#fffaf4; }
    div[data-testid="stDataFrame"] { border:1px solid var(--line); border-radius:10px; overflow:hidden; }
    </style>
    """, unsafe_allow_html=True)


def menu_card(item: dict[str, str]) -> None:
    st.markdown(f"""
    <div class="menu-card"><div class="colour" style="background:var(--{item['accent']}, #e86f51)"></div>
    <div class="body"><span class="type">{item['type']}</span><h3>{item['name']}</h3>
    <span class="pill">{item['tag']}</span><p>{item['description']}</p>
    <div class="uses">Built from inventory: {item['uses']} <strong style="float:right;color:#27221e">{item['price']}</strong></div>
    </div></div>""", unsafe_allow_html=True)


def show_inventory() -> None:
    st.markdown("<div class='eyebrow'>Stock room / live view</div>", unsafe_allow_html=True)
    st.markdown("# Your inventory, in full colour")
    st.markdown("<p class='small-copy'>The planner checks these ingredients before it suggests a menu, so every idea has a real path to the oven.</p>", unsafe_allow_html=True)
    healthy = sum(row["level"] == "Healthy" for row in INVENTORY)
    low = len(INVENTORY) - healthy
    st.markdown("<div class='section-label'>Stock signals</div>", unsafe_allow_html=True)
    for column, label, value, note in zip(st.columns(3), ["Tracked ingredients", "Ready to use", "Watch list"], [len(INVENTORY), healthy, low], ["Across 4 categories", "Enough for today's plan", "Restock before Monday"]):
        with column:
            st.markdown(f"<div class='metric'><div class='metric-label'>{label}</div><div class='metric-value'>{value}</div><div class='metric-note'>{note}</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Ingredient ledger</div>", unsafe_allow_html=True)
    st.dataframe(INVENTORY, use_container_width=True, hide_index=True, height=430)
    st.markdown("<div class='insight'><strong>Planner note:</strong> Honey, cocoa nibs and pistachios are the only ingredients trending low. The current menu uses each lightly, keeping the weekend plan comfortable.</div>", unsafe_allow_html=True)


inject_styles()
if "theme" not in st.session_state:
    st.session_state.theme = "Bright & botanical"
if "generated" not in st.session_state:
    st.session_state.generated = False

with st.sidebar:
    st.markdown("<div style='font:700 1.35rem Fraunces,serif; margin:.4rem 0 2.2rem'>Crumb <span style='color:#e86f51'>&</span> Bloom</div>", unsafe_allow_html=True)
    st.markdown("<div class='eyebrow' style='color:#d9b99d'>Workspace</div>", unsafe_allow_html=True)
    view = st.radio("Navigation", ["Menu overview", "Menu studio", "Inventory"], label_visibility="collapsed")
    st.divider()
    st.markdown("<div class='eyebrow' style='color:#d9b99d'>Today's bake window</div>", unsafe_allow_html=True)
    st.markdown("<p style='font:500 .9rem Manrope;margin:.6rem 0 1.6rem'>Friday, 25 September<br><span style='color:#b9a99b'>Prep starts at 04:30</span></p>", unsafe_allow_html=True)
    st.progress(0.72, text="72% of prep planned")
    st.markdown("<div style='height:7rem'></div><div style='font:.68rem DM Mono;color:#9b8d82'>AI MENU PLANNER / DEMO 01</div>", unsafe_allow_html=True)

if view == "Inventory":
    show_inventory()
else:
    st.markdown("<div class='topline'><div><div class='eyebrow'>Friday bake plan / 01</div><h1>A menu that starts<br>with what you have.</h1></div><div class='date-stamp'>25.09.2026<br>04:30 AM prep</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='hero'><div class='eyebrow' style='color:#b85e42'>AI kitchen brief</div><p>Good morning. I found a balanced menu in your current stock: bright fruit, a comforting chocolate note, and one beautiful loaf to anchor the counter.</p></div>", unsafe_allow_html=True)
    if view == "Menu studio":
        st.markdown("<div class='section-label'>Shape today's menu</div>", unsafe_allow_html=True)
        studio_left, studio_right = st.columns([1, 1.3])
        with studio_left:
            st.session_state.theme = st.selectbox("Menu mood", list(MENU_LIBRARY), index=list(MENU_LIBRARY).index(st.session_state.theme))
            st.selectbox("Customer moment", ["Morning regulars", "Weekend brunch crowd", "Office treat run"])
            servings = st.slider("Target covers", 24, 120, 72, step=12)
            with st.expander("Advanced preferences"):
                st.checkbox("Prioritize low-stock ingredients", value=True)
                st.checkbox("Keep one vegan option visible", value=False)
            if st.button("Generate menu", type="primary", use_container_width=True):
                st.session_state.generated = True
                st.toast(f"{st.session_state.theme} menu drafted for {servings} covers")
        with studio_right:
            st.markdown("<div class='insight'><strong>What the planner sees</strong><br>10 ingredients available, 3 low-stock signals, and enough butter, flour and eggs for a generous pastry mix. The menu below is composed from those signals.</div>", unsafe_allow_html=True)
            st.markdown("<div class='section-label'>Composition logic</div>", unsafe_allow_html=True)
            st.markdown("<p class='small-copy'>A varied counter needs one familiar favourite, one seasonal surprise and one higher-value anchor. This brief keeps all three in balance.</p>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='section-label'>Today's snapshot</div>", unsafe_allow_html=True)

    active_menu = MENU_LIBRARY[st.session_state.theme]
    st.markdown(f"<div class='topline' style='margin-top:1.8rem;margin-bottom:.8rem'><div><h2 style='margin:0 !important'>{st.session_state.theme}</h2><span class='small-copy'>{'Freshly generated' if st.session_state.generated else 'Suggested from your inventory'} for the front counter</span></div><div class='date-stamp'>3 items / 1 prep list</div></div>", unsafe_allow_html=True)
    for column, item in zip(st.columns(3, gap="medium"), active_menu):
        with column:
            menu_card(item)
    st.markdown("<div class='section-label'>Menu health</div>", unsafe_allow_html=True)
    for column, label, value, note in zip(st.columns(4), ["Inventory match", "Est. gross margin", "Prep load", "Menu balance"], ["100%", "68%", "Medium", "Strong"], ["All items trace back to stock", "Healthy for a Friday", "24 portions / item", "Sweet, bright, grounded"]):
        with column:
            st.markdown(f"<div class='metric'><div class='metric-label'>{label}</div><div class='metric-value'>{value}</div><div class='metric-note'>{note}</div></div>", unsafe_allow_html=True)