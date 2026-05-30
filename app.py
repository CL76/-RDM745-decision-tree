"""
RDM 745 - Outil de classification des dispositifs médicaux
Règlement (UE) 2017/745
"""

import streamlit as st

# Import des modules d'interface
from ui_decision_tree import show_tab_decision_tree
from ui_referentiel import show_tab_referentiel
from ui_comparatif import show_tab_comparatif
from ui_checklist import show_tab_checklist
from ui_database import show_tab_database

# ─────────────────────────────────────────────
# Configuration de la page
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="RDM 745 - Classification du Dispositif Médical",
    page_icon="🏥",
    layout="wide"
)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("📚 Référentiel RDM 745")
    st.markdown("""
    **Règlement (UE) 2017/745**

    - [Art. 2 — Définitions](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745#d1e1371-1-1)
    - [Art. 5 — Champ d'application](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745#d1e2235-1-1)
    - [Annexe XIII — Dispositifs sur mesure](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745#d1e32557-1-1)
    - [MDCG 2021-23 — Guidance](https://health.ec.europa.eu/system/files/2022-01/mdcg_2021-23_en.pdf)
    """)
    
    st.divider()
    
    st.warning("""
    ⚠️ **Avertissement**

    Cet outil est une **aide informative uniquement**.
    Il ne constitue pas un avis juridique ou réglementaire.
    Consultez un expert réglementaire pour toute classification officielle.
    """)
    
    st.divider()
    
    st.caption("Développé par C. Loiseau\nPhysicien Médical\nCentre François Baclesse, Caen")

# ─────────────────────────────────────────────
# ONGLETS PRINCIPAUX
# ─────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌳 Arbre de décision",
    "📖 Référentiel réglementaire",
    "📊 Comparatif des catégories",
    "✅ Checklist documentation",
    "💾 Ma base de données"
])

with tab1:
    show_tab_decision_tree()

with tab2:
    show_tab_referentiel()

with tab3:
    show_tab_comparatif()

with tab4:
    show_tab_checklist()

with tab5:
    show_tab_database()

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.divider()
st.warning("""
⚠️ **Avertissement légal**

Cet outil est fourni à titre **informatif uniquement**. Il ne constitue pas un avis juridique,
réglementaire ou médical. Pour toute classification officielle de dispositif médical,
**consultez un expert réglementaire qualifié**.
""")
