import streamlit as st
import random
import time

# Sayfa Ayarları
st.set_page_config(page_title="2025-2026 Pro Kura", page_icon="⚽", layout="centered")

# --- 1. VERİ SETİ ---
ligler_verisi = {
    "Süper Lig": ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor", "Başakşehir", "Samsunspor", "Eyüpspor", "Göztepe", "Alanyaspor", "Gaziantep Fk", "Antalyaspor", "Kasımpaşa", "Kocaelispor", "Karagümrük", "Gençlerbirliği", "Konyaspor", "Kayserispor", "Rizespor"],
    "Premier League": ["Man City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Man United", "Chelsea", "Newcastle", "Brentford", "Everton", "Fulham", "Brighton", "Sunderland", "Bournemouth", "Crystal Palace", "Leeds United", "Nottingham Forrest", "West Ham United", "Burnley", "Wolverhampton"],
    "La Liga": ["Real Madrid", "Barcelona", "Atletico Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Sevilla", "Villareal", "Real Betis", "Celta", "Osasuna", "Getafe", "Espanyol", "Valencia", "Rayo Vallecano", "Sevilla", "Alaves", "Elche", "Mallorca", "Levente", "Oviedo"],
    "Bundesliga": ["Bayer Leverkusen", "Bayern Münih", "Stuttgart", "RB Leipzig", " Borussia Dortmund", "Eintracht Frankfurt", "Hoffenheim", "Freiburg", "Union Berlin", "Ausburg", "Mainz 05", "Hamburg", "Borussia Mönchengladbach", "Werder Bremen", "Köln", "St. Pauli", "Wolfsburg", "Hiedenheim"],
    "Serie A": ["Inter", "Milan", "Juventus", "Atalanta", "Napoli", "Roma", "Lazio", "Como", "Bologna", "Sassuolo", "Udinese", "Parma", "Genoa", "Torino", "Cagliari", "Fiorentina", "Cremonese", "Lecce", "Hellas Verona FC", "Pisa SC"],
    "Ligue 1": ["PSG", "Monaco", "Brest", "Lille", "Nice", "Lyon", "Marsilya", "Lens", "Rennes", "Rc Strasbourg", "Toulouse", "Lorient", "Angers", "Paris FC", "Le Havre", "Nice", "Auxerre", "Nantes", "Metz"],
    "Portekiz": ["Sporting CP", "Benfica", "Porto", "Braga",],
    "Eredivisie": ["PSV", "Feyenoord", "Ajax", "Twente", "Az Alkmaar"],
    "Arjantin": ["Boca Juniors", "River Plate"]
}

# --- 2. DURUM YÖNETİMİ ---
if 'asama' not in st.session_state:
    st.session_state.asama = 0

# --- 3. EKRAN 1: LİG SEÇİMİ ---
if st.session_state.asama == 0:
    st.title("🏆 Lig Seçim Ekranı")
    st.write("Kura havuzuna dahil etmek istediğiniz ligleri işaretleyin.")
    
    secilenler = []
    cols = st.columns(2)
    for i, lig in enumerate(ligler_verisi.keys()):
        with cols[i % 2]:
            if st.checkbox(lig, value=True, key=f"check_{lig}"):
                secilenler.append(lig)
    
    st.divider()
    
    if st.button("İLERLE 👉", use_container_width=True, type="primary"):
        if not secilenler:
            st.warning("Lütfen en az bir lig seçin!")
        else:
            havuz = []
            for l in secilenler:
                havuz.extend(ligler_verisi[l])
            st.session_state.havuz = havuz
            st.session_state.asama = 1
            st.rerun()

# --- 4. EKRAN 2: KURA PANELİ ---
elif st.session_state.asama == 1:
    st.title("🎮 Kura Paneli")
    
    if st.button("⬅ Ligleri Yeniden Düzenle"):
        st.session_state.asama = 0
        st.rerun()
    
    st.divider()

    col1, col2 = st.columns(2)
    
    with col1:
        p1_placeholder = st.empty()
        p1_placeholder.info("### OYUNCU 1\n# ---")
    with col2:
        p2_placeholder = st.empty()
        p2_placeholder.warning("### OYUNCU 2\n# ---")

    if st.button("KURA ÇEK 🎲", use_container_width=True, type="primary"):
        # --- ANİMASYON ---
        for _ in range(15): 
            t1 = random.choice(st.session_state.havuz)
            t2 = random.choice(st.session_state.havuz)
            p1_placeholder.info(f"### OYUNCU 1\n# {t1}")
            p2_placeholder.warning(f"### OYUNCU 2\n# {t2}")
            time.sleep(0.1)
        
        # --- FİNAL SEÇİMİ ---
        final_1, final_2 = random.sample(st.session_state.havuz, 2)
        p1_placeholder.info(f"### OYUNCU 1\n# {final_1}")
        p2_placeholder.warning(f"### OYUNCU 2\n# {final_2}")
        
        # Balonlar (st.balloons()) buradan kaldırıldı.
        st.success(f"Eşleşme Tamamlandı!")
