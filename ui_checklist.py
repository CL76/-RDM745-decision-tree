"""
Onglet comparatif des 3 catégories de dispositifs médicaux.
"""

import streamlit as st


def show_tab_checklist():
    st.title("✅ Checklist documentation par catégorie")
    st.divider()

    categorie = st.selectbox(
        "Sélectionnez votre catégorie :",
        ["DM Standard", "Patient-Matched (Art. 5§5)", "Sur Mesure (Art. 2§3)"]
    )

    st.divider()

    if categorie == "DM Standard":
        st.subheader("📋 DM Standard")
        for item in [
            "Description et spécification du dispositif",
            "Informations fournies par le fabricant (étiquetage, notice)",
            "Vérification EGSEP (Annexe I)",
            "Analyse des bénéfices/risques",
            "Évaluation clinique (Annexe XIV)",
            "Plan de surveillance après commercialisation (PSAC)",
            "Rapport de surveillance (RSAC)",
            "Enregistrement EUDAMED",
            "Marquage CE apposé",
            "Déclaration UE de conformité signée"
        ]:
            st.checkbox(item, key=f"std_{item}")

    elif categorie == "Patient-Matched (Art. 5§5)":
        st.subheader("📋 Patient-Matched Art. 5§5")
        tab_a, tab_b, tab_c = st.tabs(["✅ Conditions", "📄 Documentation", "🔍 Traçabilité"])
        with tab_a:
            for item in [
                "Fabrication dans l'établissement de santé",
                "Absence d'alternative commerciale équivalente",
                "Système de management de la qualité (SMQ)",
                "Notification à l'ANSM",
                "Désignation d'un responsable qualité"
            ]:
                st.checkbox(item, key=f"pm_pre_{item}")
        with tab_b:
            for item in [
                "Description générale du dispositif",
                "Workflow de conception documenté",
                "Vérification Annexe I (EGSEP)",
                "Évaluation clinique / revue littérature",
                "Analyse des risques",
                "Certificats de biocompatibilité",
                "Fiches de données de sécurité (FDS)"
            ]:
                st.checkbox(item, key=f"pm_tech_{item}")
        with tab_c:
            for item in [
                "Système de traçabilité interne",
                "Registre des dispositifs fabriqués",
                "Fiche de fabrication par dispositif",
                "Fiche de contrôle qualité",
                "Archivage 10 ans"
            ]:
                st.checkbox(item, key=f"pm_traj_{item}")

    elif categorie == "Sur Mesure (Art. 2§3)":
        st.subheader("📋 Sur Mesure Art. 2§3")
        tab_a, tab_b, tab_c = st.tabs(["📄 Déclaration", "📚 Dossier technique", "🏷️ Étiquetage"])
        with tab_a:
            for item in [
                "Nom et adresse du fabricant",
                "Identification du dispositif",
                "Nom du patient destinataire",
                "Nom du praticien prescripteur",
                "Confirmation conformité EGSEP (Annexe I)",
                "Classe de risque",
                "Signature du responsable"
            ]:
                st.checkbox(item, key=f"sm_decl_{item}")
        with tab_b:
            for item in [
                "Description générale",
                "Prescription écrite originale",
                "Méthodes de fabrication et contrôle",
                "Évaluation clinique",
                "Analyse des risques",
                "Certificats de biocompatibilité"
            ]:
                st.checkbox(item, key=f"sm_tech_{item}")
        with tab_c:
            for item in [
                "Identification nominative du patient",
                "Mention « Dispositif sur mesure »",
                "Nom et adresse du fabricant",
                "Date de fabrication",
                "Classe du dispositif"
            ]:
                st.checkbox(item, key=f"sm_etiq_{item}")
        st.warning("⚠️ Classes IIb/III : notification ON obligatoire")
