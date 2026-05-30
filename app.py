import streamlit as st
from ui_decision_tree import show_tab_decision_tree
from ui_referentiel import show_tab_referentiel
from ui_comparatif import show_tab_comparatif
from ui_checklist import show_tab_checklist
from ui_database import show_tab_database
# futures importations :
# from ui_art5s5 import show_tab_art5s5
# from ui_art2s3 import show_tab_art2s3

st.set_page_config(
    page_title="RDM 745 - Classification du Dispositif Médical",
    page_icon="🏥",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.header("📚 Référentiel RDM 745")
    st.markdown("""
    - [Art. 2 — Définitions](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745#d1e1371-1-1)
    - [Art. 5 — Champ d'application](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745#d1e2235-1-1)
    - [Annexe XIII](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745#d1e32557-1-1)
    - [MDCG 2021-23](https://health.ec.europa.eu/system/files/2022-01/mdcg_2021-23_en.pdf)
    """)
    st.divider()
    st.warning("⚠️ Aide informative uniquement.\nPas un avis juridique.")
    st.divider()
    st.caption("C. Loiseau — Physicien Médical\nCentre François Baclesse, Caen")

# Onglets
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌳 Arbre de décision",
    "📖 Référentiel",
    "📊 Comparatif",
    "✅ Checklist",
    "💾 Ma base de données"
])

with tab1: show_tab_decision_tree()
with tab2: show_tab_referentiel()
with tab3: show_tab_comparatif()
with tab4: show_tab_checklist()
with tab5: show_tab_database()
