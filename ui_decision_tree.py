"""
Onglet de l'arbre de décision pour la classification du dispositif médical.
"""

import streamlit as st
from database import init_db, add_dispositif


def show_tab_decision_tree():
    """Affiche l'onglet de l'arbre de décision."""
    st.title("🏥 Quelle est la nature de votre dispositif médical ?")
    st.caption("Règlement (UE) 2017/745 — RDM 745")
    st.divider()
    
    # ─────────────────────────────────────────────
    # Q1
    # ─────────────────────────────────────────────
    q1 = st.radio(
        "**Q1 — La conception peut-elle exister AVANT de connaître le patient ?**",
        ["OUI", "NON"],
        key="q1",
        help="Le dispositif peut-il être conçu sans aucune information sur un patient spécifique ?"
    )
    
    # ─── Branche OUI → Q3
    if q1 == "OUI":
        st.info("✅ La conception est indépendante du patient → Passage à Q3")
        st.divider()
        
        q3 = st.radio(
            "**Q3 — L'anatomie/imagerie du patient ALIMENTE-T-ELLE un process de conception standardisé et reproductible ?**",
            [
                "NON — identique pour tous les patients",
                "OUI — workflow préexiste, données patient = input du process"
            ],
            key="q1_oui_q3",
            help="Le workflow de conception préexiste-t-il et les données patient ne font-elles que l'alimenter ?"
        )
        
        if q3 == "NON — identique pour tous les patients":
            st.success("## ✅ DM STANDARD")
            show_standard()
            
            # Formulaire pour ajouter à la base
            add_to_db_form("DM Standard", "standard")
        
        elif q3 == "OUI — workflow préexiste, données patient = input du process":
            st.success("## ✅ DM ADAPTÉ AU PATIENT (patient-matched)")
            show_patient_matched()
            
            # Formulaire pour ajouter à la base
            add_to_db_form("DM Adapté au Patient (patient-matched)", "patient-matched")
    
    # ─── Branche NON → Q2
    elif q1 == "NON":
        st.info("❌ La conception nécessite le patient → Passage à Q2")
        st.divider()
        
        q2 = st.radio(
            """**Q2 — Le prescripteur fournit-il une donnée
(prescription écrite, empreinte physique, scan nominatif)
qui IMPOSE intégralement la forme finale,
SANS qu'aucune règle préexistante du fabricant
ne vienne l'interpréter ou la compléter ?**""",
            ["NON", "OUI"],
            key="q2",
            help="Le prescripteur impose-t-il TOUTE la forme sans que le fabricant n'ajoute de règles préexistantes ?"
        )
        
        if q2 == "NON":
            st.info("⚠️ Le fabricant interprète/complète → Retour à Q3")
            st.divider()
            
            q3 = st.radio(
                "**Q3 — L'anatomie/imagerie du patient ALIMENTE-T-ELLE un process de conception standardisé et reproductible ?**",
                [
                    "NON — identique pour tous les patients",
                    "OUI — workflow préexiste, données patient = input du process"
                ],
                key="q2_non_q3"
            )
            
            if q3 == "NON — identique pour tous les patients":
                st.success("## ✅ DM STANDARD")
                show_standard()
                add_to_db_form("DM Standard", "standard")
            
            elif q3 == "OUI — workflow préexiste, données patient = input du process":
                st.success("## ✅ DM ADAPTÉ AU PATIENT (patient-matched)")
                show_patient_matched()
                add_to_db_form("DM Adapté au Patient (patient-matched)", "patient-matched")
        
        elif q2 == "OUI":
            st.info("✅ Le prescripteur impose intégralement → Passage à Q2b")
            st.divider()
            
            q2b = st.radio(
                "**Q2b — Le résultat est-il géométriquement UNIQUE, non reproductible à l'identique pour un autre patient ?**",
                ["NON", "OUI"],
                key="q2b",
                help="Chaque dispositif est-il géométriquement unique ?"
            )
            
            if q2b == "NON":
                st.info("⚠️ Reproductible → Retour à Q3")
                st.divider()
                
                q3 = st.radio(
                    "**Q3 — L'anatomie/imagerie du patient ALIMENTE-T-ELLE un process de conception standardisé et reproductible ?**",
                    [
                        "NON — identique pour tous les patients",
                        "OUI — workflow préexiste, données patient = input du process"
                    ],
                    key="q2b_non_q3"
                )
                
                if q3 == "NON — identique pour tous les patients":
                    st.success("## ✅ DM STANDARD")
                    show_standard()
                    add_to_db_form("DM Standard", "standard")
                
                elif q3 == "OUI — workflow préexiste, données patient = input du process":
                    st.success("## ✅ DM ADAPTÉ AU PATIENT (patient-matched)")
                    show_patient_matched()
                    add_to_db_form("DM Adapté au Patient (patient-matched)", "patient-matched")
            
            elif q2b == "OUI":
                st.success("## ✅ SUR MESURE (Art. 2§3)")
                show_custom()
                add_to_db_form("Dispositif SUR MESURE (Art. 2§3)", "sur-mesure")


# ─────────────────────────────────────────────
# FONCTIONS D'AFFICHAGE
# ─────────────────────────────────────────────
def show_standard():
    """Affiche les détails pour DM Standard."""
    st.markdown("""
    #### 📋 Caractéristiques :
    - **Marquage CE obligatoire**
    - **Procédure normale** selon la classe du dispositif
    - Pas de dérogation nécessaire

    #### 🔬 Exemples :
    - Applicateur Fletcher standard
    - Masque thermoformé standard
    - Bolus commercial

    #### 📚 Réglementation :
    - RDM 745 — Champ d'application normal
    - Annexe I — Exigences générales de sécurité et de performance
    - Annexe II & III — Dossier technique et surveillance
    """)


def show_patient_matched():
    """Affiche les détails pour DM Patient-Matched."""
    st.markdown("""
    #### 📋 Caractéristiques :
    - **DM standard** ou **in-house Art. 5§5**
    - Marquage CE **ou dérogation Art. 5§5**
    - Workflow préexiste, données patient = input

    #### 🔬 Exemples :
    - Applicateur curiethérapie perso 3D (scan → CAO → impression)
    - Bolus 3D (scan → épaisseur standard → impression)
    - Guide de perçage interstitiel perso
    - Masque thermoformé sur moulage patient

    #### 📚 Réglementation :
    - **RDM 745 Art. 5§5** — Fabrication in-house
    - MDCG 2021-23 — Guidance patient-matched
    - Annexe I — EGSEP toujours applicables
    """)


def show_custom():
    """Affiche les détails pour Sur Mesure."""
    st.markdown("""
    #### 📋 Caractéristiques :
    - **Annexe XIII** du RDM 745
    - **Pas de marquage CE** nécessaire
    - **Déclaration de conformité** fabricant obligatoire
    - **Identification nominative** obligatoire
    - **Notification ON** si classe IIb/III

    #### 🔬 Exemples :
    - Couronne dentaire (empreinte → laboratoire)
    - Embout ORL (empreinte → laboratoire)
    - Prothèse hanche (cotes → fabricant)
    - Plaque crânienne (scan → reconstitution manuelle exclusive)

    #### 📚 Réglementation :
    - **RDM 745 Art. 2§3** — Définition « sur mesure »
    - **Annexe XIII** — Procédure spécifique sur mesure
    - **MDCG 2021-23** — Guidance sur mesure vs patient-matched
    """)


def add_to_db_form(categorie_nom, categorie_code):
    """Formulaire pour ajouter le dispositif à la base de données."""
    st.divider()
    with st.expander("💾 Ajouter ce dispositif à ma base de données", expanded=False):
        st.markdown(f"**Catégorie détectée :** {categorie_nom}")
        
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom du dispositif", placeholder="Ex: Applicateur curiethérapie 3D")
            reference = st.text_input("Référence interne", placeholder="Ex: REF-APP-001")
            classe = st.selectbox("Classe", ["I", "IIa", "IIb", "III"])
        
        with col2:
            materiau = st.text_input("Matériau", placeholder="Ex: Résine biocompatible SLA")
            description = st.text_area("Description courte", placeholder="Brève description du dispositif")
        
        if st.button("🔹 Ajouter à la base", use_container_width=True):
            if nom:
                db = init_db()
                device_id = add_dispositif(
                    nom=nom,
                    reference=reference,
                    classe=classe,
                    categorie=categorie_code,
                    materiau=materiau,
                    description=description
                )
                st.success(f"✅ Dispositif ajouté avec ID : `{device_id}`")
            else:
                st.warning("⚠️ Le nom du dispositif est obligatoire")
