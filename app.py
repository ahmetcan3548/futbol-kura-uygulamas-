import streamlit as st
import random
import time

# Sayfa Genişliği ve Tema Ayarları
st.set_page_config(page_title="2025-2026 Pro Kura", page_icon="⚽", layout="centered")

# --- 1. GÜNCEL VERİ SETİ ---
ligler_verisi = {
    "Süper Lig 🇹🇷": ["Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor", "Başakşehir", "Samsunspor", "Eyüpspor", "Göztepe", "Bodrum FK"],
    "Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿": ["Man City", "Arsenal", "Liverpool", "Aston Villa", "Tottenham", "Man United", "Chelsea", "Newcastle"],
    "La Liga 🇪🇸": ["Real Madrid", "Barcelona", "Atletico Madrid", "Girona", "Athletic Bilbao", "Real Sociedad", "Sevilla"],
    "Bundesliga 🇩🇪": ["Bayer Leverkusen", "Bayern Münih", "Stuttgart", "RB Leipzig", "Dortmund", "Frankfurt"],
    "Serie A 🇮🇹": ["Inter", "Milan", "Juventus", "Atalanta", "Napoli", "Roma", "Lazio"],
    "Ligue 1 🇫🇷": ["PSG", "Monaco", "Brest", "Lille", "Nice", "Lyon", "Marsilya"],
    "Portekiz 🇵🇹": ["Sporting CP", "Benfica", "Porto", "Braga", "Vitoria SC"]
}

# --- 2. DURUM YÖNETİMİ (Session State) ---
# Uygulamanın hangi aşamada olduğunu takip eder (0: Seçim, 1: Kura)
if 'asama' not in st.session_state:
    st.session_state.asama = 0
if 'secili_takimlar' not in st.session_state:
    st.session_state.secili_takimlar = []

# --- 3. EKRAN 1: LİG SEÇİMİ ---
if st.session_state.asama == 0:
    st.title("🏆 Lig Seçim Ekranı")
    st.write("Kura havuzuna dahil etmek istediğiniz ligleri işaretleyin.")
    
    secilenler = []
    # Ligleri 2 sütun halinde göster
    cols = st.columns(2)
    for i, lig in enumerate(ligler_verisi.keys()):
        with cols[i % 2]:
            if st.checkbox(lig, value=True, key=f"check_{lig}"):
                secilenler.append(lig)
    
    st.divider()
    
    if st.button("İLERLE 👉", use_container_width=True, type="primary"):
        if len(secilenler) == 0:
            st.warning("Lütfen en az bir lig seçin!")
        else:
            # Seçilen liglerdeki tüm takımları havuzla
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

    # Oyuncu Alanları (Yan Yana)
    col1, col2 = st.columns(2)
    
    # Boş kutucuklar veya önceki sonuçlar
    with col1:
        p1_placeholder = st.empty()
        p1_placeholder.info("### OYUNCU 1\n# ---")
    with col2:
        p2_placeholder = st.empty()
        p2_placeholder.warning("### OYUNCU 2\n# ---")

    if st.button("KURA ÇEK 🎲", use_container_width=True, type="primary"):
        # --- ANİMASYON EFEKTİ ---
        for _ in range(20): # 20 kez hızlıca isim değiştir
            t1 = random.choice(st.session_state.havuz)
            t2 = random.choice(st.session_state.havuz)
            
            p1_placeholder.info(f"### OYUNCU 1\n# {t1}")
            p2_placeholder.warning(f"### OYUNCU 2\n# {t2}")
            time.sleep(0.1) # Dönme hızı
        
        # --- FİNAL SEÇİMİ ---
        final_1, final_2 = random.sample(st.session_state.havuz, 2)
        p1_placeholder.info(f"### OYUNCU 1\n# {final_1}")
        p2_placeholder.warning(f"### OYUNCU 2\n# {final_2}")
        
        st.balloons()
        st.success(f"Eşleşme Tamamlandı: **{final_1}** vs **{final_2}**")
