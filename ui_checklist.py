"""
Onglet comparatif des 3 catégories de dispositifs médicaux.
"""

import streamlit as st


def show_tab_comparatif():
    """Affiche l'onglet comparatif des 3 catégories."""
    st.title("📊 Comparatif des 3 catégories")
    st.caption("Tableau comparatif des obligations réglementaires selon la catégorie")
    st.divider()

    # ─────────────────────────────────────────────
    # TABLEAU COMPARATIF PRINCIPAL
    # ─────────────────────────────────────────────
    st.subheader("📋 Tableau comparatif")
    st.markdown("""
    | Critère | DM Standard | Patient-Matched (Art. 5§5) | Sur Mesure (Art. 2§3) |
    |---------|:-----------:|:-------------------------:|:--------------------:|
    | **Conception** | Indépendante du patient | Workflow standardisé + données patient | Dictée par le prescripteur |
    | **Unicité** | Identique pour tous | Adapté mais reproductible | Géométriquement unique |
    | **Marquage CE** | ✅ Obligatoire | ✅ ou dérogation Art. 5§5 | ❌ Non requis |
    | **Organisme Notifié** | Selon classe | Selon classe | Non (sauf IIb/III) |
    | **Déclaration fabricant** | Selon procédure | Selon procédure | ✅ Obligatoire |
    | **ID nominative patient** | ❌ Non | ❌ Non | ✅ Obligatoire |
    | **Dossier technique** | Annexe II/III | Annexe II/III | Annexe XIII |
    | **Évaluation clinique** | ✅ Requise | ✅ Requise | ✅ Requise |
    | **Notification ANSM** | Selon classe | ✅ Art. 5§5 | ❌ Non |
    | **EUDAMED** | ✅ Obligatoire | ✅ Obligatoire | ❌ Non requis |
    | **Annexe I (EGSEP)** | ✅ Obligatoire | ✅ Obligatoire | ✅ Obligatoire |
    """)

    st.info("""
    💡 **Rappel :** Quelle que soit la catégorie, les **Exigences Générales de Sécurité
    et de Performance (Annexe I)** restent toujours applicables.
    """)

    # ─────────────────────────────────────────────
    # TABLEAU PAR CLASSE
    # ─────────────────────────────────────────────
    st.divider()
    st.subheader("📋 Obligations selon la classe de risque")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### Classe I")
        st.markdown("""
        - Autocertification fabricant
        - Pas d'ON nécessaire
        - Dossier technique interne
        - Déclaration UE de conformité
        - Enregistrement EUDAMED
        """)

    with col2:
        st.markdown("#### Classe IIa / IIb")
        st.markdown("""
        - Intervention d'un ON obligatoire
        - Audit du système qualité (Annexe IX)
        - ou Examen de type CE (Annexe X)
        - RPAS (IIb uniquement)
        - Enregistrement EUDAMED
        """)

    with col3:
        st.markdown("#### Classe III")
        st.markdown("""
        - ON obligatoire
        - Examen de la conception (Annexe IX)
        - Évaluation clinique renforcée
        - Rapport de suivi clinique post-marché
        - Enregistrement EUDAMED
        """)

    # ─────────────────────────────────────────────
    # SCHÉMA DÉCISIONNEL RÉSUMÉ
    # ─────────────────────────────────────────────
    st.divider()
    st.subheader("🗺️ Résumé visuel")

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.success("""
        ### ✅ DM STANDARD

        **Conception indépendante**
        du patient

        → Marquage CE
        → Procédure normale
        → Annexe II/III

        **Exemples :**
        - Fletcher standard
        - Masque standard
        - Bolus commercial
        """)

    with col_b:
        st.warning("""
        ### ⚙️ PATIENT-MATCHED

        **Workflow standardisé**
        + données patient = input

        → Art. 5§5 (in-house)
        → Notification ANSM
        → Dossier technique

        **Exemples :**
        - Applicateur curie 3D
        - Bolus 3D personnalisé
        - Guide de perçage perso
        """)

    with col_c:
        st.error("""
        ### 🔒 SUR MESURE

        **Conception dictée**
        par le prescripteur

        → Art. 2§3
        → Annexe XIII
        → Pas de marquage CE
        → ID nominative

        **Exemples :**
        - Prothèse crânienne
        - Embout ORL
        - Couronne dentaire
        """)

    # ─────────────────────────────────────────────
    # AVERTISSEMENT HORS CADRE
    # ─────────────────────────────────────────────
    st.divider()
    st.error("""
    ⚠️ **Hors cadre Art. 5§5**

    Si votre dispositif ne rentre dans **aucune de ces catégories**
    ou s'il est destiné à la **commercialisation**,
    vous devez suivre la **procédure complète RDM 745**
    avec marquage CE et intervention d'un Organisme Notifié.

    **→ Consultez OBLIGATOIREMENT un expert réglementaire.**
    """)
