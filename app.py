import streamlit as st

# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="RDM 745 - Classification du Dispositif Médical",
    page_icon="🏥",
    layout="wide"
)

# ─────────────────────────────────────────────
# FONCTIONS D'AFFICHAGE DES RÉSULTATS
# ─────────────────────────────────────────────
def show_standard():
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
    - [MDCG 2021-23 — Guidance patient-matched](https://health.ec.europa.eu/system/files/2022-01/mdcg_2021-23_en.pdf)
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
tab1, tab2, tab3, tab4 = st.tabs([
    "🌳 Arbre de décision",
    "📖 Référentiel réglementaire",
    "📊 Comparatif des catégories",
    "✅ Checklist documentation"
])

# ═══════════════════════════════════════════════
# TAB 1 — ARBRE DE DÉCISION
# ═══════════════════════════════════════════════
with tab1:
    st.title("🏥 Quelle est la nature de votre dispositif médical ?")
    st.caption("Règlement (UE) 2017/745 — RDM 745")
    st.divider()

    q1 = st.radio(
        "**Q1 — La conception peut-elle exister AVANT de connaître le patient ?**",
        ["OUI", "NON"],
        key="q1",
        help="Le dispositif peut-il être conçu sans aucune information sur un patient spécifique ?"
    )

    if q1 == "OUI":
        st.info("✅ La conception est indépendante du patient → Passage à Q3")
        st.divider()

        q3 = st.radio(
            "**Q3 — L'anatomie/imagerie du patient ALIMENTE-T-ELLE un process de conception standardisé et reproductible ?**",
            [
                "NON — identique pour tous les patients",
                "OUI — workflow préexiste, données patient = input du process"
            ],
            key="q1_oui_q3"
        )

        if q3 == "NON — identique pour tous les patients":
            st.success("## ✅ DM STANDARD")
            show_standard()

        elif q3 == "OUI — workflow préexiste, données patient = input du process":
            st.success("## ✅ DM ADAPTÉ AU PATIENT (patient-matched)")
            show_patient_matched()

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
            key="q2"
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

            elif q3 == "OUI — workflow préexiste, données patient = input du process":
                st.success("## ✅ DM ADAPTÉ AU PATIENT (patient-matched)")
                show_patient_matched()

        elif q2 == "OUI":
            st.info("✅ Le prescripteur impose intégralement → Passage à Q2b")
            st.divider()

            q2b = st.radio(
                "**Q2b — Le résultat est-il géométriquement UNIQUE, non reproductible à l'identique pour un autre patient ?**",
                ["NON", "OUI"],
                key="q2b"
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

                elif q3 == "OUI — workflow préexiste, données patient = input du process":
                    st.success("## ✅ DM ADAPTÉ AU PATIENT (patient-matched)")
                    show_patient_matched()

            elif q2b == "OUI":
                st.success("## ✅ SUR MESURE (Art. 2§3)")
                show_custom()

# ═══════════════════════════════════════════════
# TAB 2 — RÉFÉRENTIEL RÉGLEMENTAIRE
# ═══════════════════════════════════════════════
with tab2:
    st.title("📖 Référentiel réglementaire — RDM 745")
    st.caption("Cliquez sur chaque article pour afficher les détails")
    st.divider()

    with st.expander("📌 Article 2§3 — Définition : Dispositif sur mesure", expanded=False):
        st.markdown("""
        **Texte de référence :**
        > *« Dispositif sur mesure : tout dispositif fabriqué spécifiquement selon une prescription écrite
        > d'un praticien dûment qualifié, donnant sous sa responsabilité des caractéristiques de conception
        > spécifiques et destiné à n'être utilisé que pour un patient déterminé. »*

        **Points clés :**
        - Prescription **écrite** d'un praticien qualifié
        - Caractéristiques de conception **spécifiques** dictées par le prescripteur
        - Destiné à **un seul patient**
        - Exclut les dispositifs fabriqués en série, même adaptés ensuite

        **⚠️ Limite :**
        Les dispositifs fabriqués selon des **méthodes industrielles standardisées** ne sont pas
        considérés comme sur mesure, même si adaptés à un patient.

        🔗 [Voir texte officiel EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745#d1e1371-1-1)
        """)

    with st.expander("📌 Article 5§5 — Fabrication in-house (patient-matched)", expanded=False):
        st.markdown("""
        **Texte de référence :**
        > *« Les États membres peuvent autoriser que des établissements de santé fabriquent,
        > modifient et utilisent des dispositifs au sein de l'établissement. »*

        **Conditions d'application :**
        - Fabrication **au sein de l'établissement de santé**
        - Aucune alternative commerciale équivalente disponible
        - Système de gestion de la qualité en place
        - Documentation technique disponible
        - Notification à l'autorité compétente (ANSM en France)

        **Obligations :**
        - Déclaration à l'autorité compétente nationale
        - Dossier technique équivalent Annexe II/III
        - Évaluation clinique documentée
        - Système de traçabilité interne

        **⚠️ Ce n'est PAS une dérogation totale :**
        Les exigences générales de sécurité et de performance (Annexe I) restent applicables.

        🔗 [Voir texte officiel EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745#d1e2235-1-1)
        """)

    with st.expander("📌 Annexe XIII — Procédure pour dispositifs sur mesure", expanded=False):
        st.markdown("""
        **§1 — Déclaration de conformité :**
        - Nom et adresse du fabricant
        - Données nécessaires pour identifier le dispositif (dont nom du patient)
        - Confirmation de conformité aux exigences générales de sécurité (Annexe I)
        - Classe de risque du dispositif

        **§2 — Documentation technique :**
        - Description générale du dispositif
        - Instructions de conception (plan, schéma, prescription)
        - Description des méthodes de fabrication et de contrôle
        - Évaluation clinique (données de littérature)

        **Obligations selon la classe :**
        | Classe | Obligations supplémentaires |
        |--------|----------------------------|
        | I | Déclaration fabricant uniquement |
        | IIa | Déclaration + dossier technique |
        | IIb | Déclaration + dossier technique + notification ON |
        | III | Déclaration + dossier technique + notification ON |

        🔗 [Voir texte officiel EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745#d1e32557-1-1)
        """)

    with st.expander("📌 Annexe I — Exigences générales de sécurité et de performance (EGSEP)", expanded=False):
        st.markdown("""
        **Applicable à TOUS les dispositifs médicaux sans exception**

        **Exigences générales :**
        - Ne pas compromettre la sécurité ou la santé du patient
        - Performances attendues selon la destination prévue
        - Niveau de sécurité et de performance acceptable au regard de l'état de l'art

        **Exigences relatives à la conception et à la fabrication :**
        - Propriétés chimiques, physiques et biologiques
        - Infection et contamination microbienne
        - Propriétés relatives à la fabrication et à l'environnement
        - Protection contre les rayonnements

        **⚠️ Rappel :**
        Ces exigences s'appliquent même aux dispositifs sur mesure (Art. 2§3)
        et aux dispositifs in-house (Art. 5§5).

        🔗 [Voir texte officiel EUR-Lex](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32017R0745)
        """)

    with st.expander("📌 MDCG 2021-23 — Guidance patient-matched vs sur mesure", expanded=False):
        st.markdown("""
        **Document de référence de la Commission Européenne**

        | Critère | Sur mesure (Art. 2§3) | Patient-matched (Art. 5§5) |
        |---------|----------------------|--------------------------|
        | Conception | Dictée par prescripteur | Workflow standardisé |
        | Reproductibilité | Non reproductible | Reproductible pour autres patients |
        | Marquage CE | Non requis | Requis ou dérogation Art. 5§5 |
        | Unicité | Géométriquement unique | Adapté mais non unique |

        **⚠️ Point critique :**
        Si le fabricant applique des **règles préexistantes** pour interpréter les données patient,
        le dispositif n'est plus « sur mesure » mais « patient-matched ».

        🔗 [Télécharger MDCG 2021-23 (PDF)](https://health.ec.europa.eu/system/files/2022-01/mdcg_2021-23_en.pdf)
        """)

    with st.expander("📌 Hors cadre Art. 5§5 — Que faire ?", expanded=False):
        st.error("""
        **Si votre dispositif ne rentre pas dans le cadre Art. 5§5 :**

        ❌ Vous n'êtes pas un établissement de santé qui fabrique pour ses propres patients
        ❌ Votre dispositif est destiné à être commercialisé
        ❌ Votre dispositif ne répond pas aux critères de la dérogation

        **→ Vous devez suivre la procédure complète RDM 745**
        et consulter OBLIGATOIREMENT un expert réglementaire.
        """)
        st.markdown("""
        **Contacts utiles :**
        - [ANSM (Autorité française)](https://ansm.sante.fr)
        - [SNITEM (Syndicat national)](https://www.snitem.fr)
        - [Commission Européenne - DG SANTE](https://health.ec.europa.eu)
        """)

# ═══════════════════════════════════════════════
# TAB 3 — COMPARATIF
# ═══════════════════════════════════════════════
with tab3:
    st.title("📊 Comparatif des 3 catégories")
    st.divider()

    st.markdown("""
    | Critère | DM Standard | Patient-Matched (Art. 5§5) | Sur Mesure (Art. 2§3) |
    |---------|-------------|--------------------------|----------------------|
    | **Conception** | Indépendante du patient | Workflow standardisé + données patient | Dictée par le prescripteur |
    | **Unicité** | Identique pour tous | Adapté mais reproductible | Géométriquement unique |
    | **Marquage CE** | ✅ Obligatoire | ✅ ou dérogation Art. 5§5 | ❌ Non requis |
    | **Organisme Notifié** | Selon classe | Selon classe | Non (sauf IIb/III) |
    | **Déclaration fabricant** | Selon procédure | Selon procédure | ✅ Obligatoire |
    | **ID nominative** | ❌ Non | ❌ Non | ✅ Obligatoire |
    | **Dossier technique** | Annexe II/III | Annexe II/III | Annexe XIII |
    | **Évaluation clinique** | ✅ Requise | ✅ Requise | ✅ Requise |
    | **Notification ANSM** | Selon classe | ✅ Art. 5§5 | ❌ Non |
    | **Exemples** | Fletcher, Bolus commercial | Applicateur curie 3D, Bolus 3D | Prothèse crânienne, Embout ORL |
    """)

    st.divider()
    st.info("""
    💡 **Rappel :** Quelle que soit la catégorie, les **Exigences Générales de Sécurité
    et de Performance (Annexe I)** restent toujours applicables.
    """)

# ═══════════════════════════════════════════════
# TAB 4 — CHECKLIST DOCUMENTATION
# ═══════════════════════════════════════════════
with tab4:
    st.title("✅ Checklist documentation par catégorie")
    st.divider()

    cat = st.selectbox(
        "Sélectionnez votre catégorie :",
        ["DM Standard", "Patient-Matched (Art. 5§5)", "Sur Mesure (Art. 2§3)"]
    )

    if cat == "DM Standard":
        st.subheader("📋 DM Standard — Documentation requise")
        st.markdown("""
        **Dossier technique (Annexe II) :**
        - [ ] Description et spécification du dispositif
        - [ ] Informations fournies par le fabricant (étiquetage, notice)
        - [ ] Informations relatives à la conception et à la fabrication
        - [ ] Exigences générales de sécurité et de performance (Annexe I)
        - [ ] Analyse des bénéfices/risques et gestion des risques
        - [ ] Vérification et validation du produit
        - [ ] Évaluation clinique (Annexe XIV)
        - [ ] Informations sur les dispositifs similaires disponibles

        **Dossier de surveillance après commercialisation (Annexe III) :**
        - [ ] Plan de surveillance après commercialisation (PSAC)
        - [ ] Rapport de surveillance après commercialisation (RSAC)
        - [ ] Rapport périodique actualisé de sécurité (RPAS) — classes IIa, IIb, III

        **Autres :**
        - [ ] Enregistrement EUDAMED
        - [ ] Marquage CE apposé
        - [ ] Déclaration UE de conformité
        """)

    elif cat == "Patient-Matched (Art. 5§5)":
        st.subheader("📋 Patient-Matched Art. 5§5 — Documentation requise")
        st.markdown("""
        **Conditions préalables :**
        - [ ] Confirmer que le dispositif est fabriqué dans l'établissement de santé
        - [ ] Confirmer l'absence d'alternative commerciale équivalente
        - [ ] Système de management de la qualité (SMQ) en place

        **Documentation technique :**
        - [ ] Description générale du dispositif et de son utilisation prévue
        - [ ] Workflow de conception documenté (CAO, paramètres impression, etc.)
        - [ ] Caractéristiques techniques et spécifications
        - [ ] Exigences Annexe I (EGSEP) — vérification point par point
        - [ ] Évaluation clinique / revue de littérature

        **Traçabilité :**
        - [ ] Système de traçabilité interne (numéro de lot, patient, date)
        - [ ] Procédures de contrôle qualité (contrôle dimensionnel, etc.)
        - [ ] Procédures de maintenance des équipements (imprimante 3D, etc.)

        **Notification :**
        - [ ] Notification à l'ANSM (autorité compétente française)
        - [ ] Mise à jour annuelle si modifications significatives

        **Matières premières :**
        - [ ] Certificats de conformité des matériaux (biocompatibilité Annexe I §10)
        - [ ] Fiches de données de sécurité (FDS)
        - [ ] Traçabilité des lots de résine/filament
        """)

    elif cat == "Sur Mesure (Art. 2§3)":
        st.subheader("📋 Sur Mesure Art. 2§3 — Documentation requise")
        st.markdown("""
        **Déclaration de conformité fabricant (Annexe XIII §1) :**
        - [ ] Nom et adresse du fabricant
        - [ ] Données d'identification du dispositif
        - [ ] Nom du patient destinataire
        - [ ] Nom du praticien prescripteur
        - [ ] Caractéristiques spécifiques du dispositif (prescription)
        - [ ] Confirmation de conformité aux EGSEP (Annexe I)
        - [ ] Classe de risque du dispositif

        **Documentation technique (Annexe XIII §2) :**
        - [ ] Description générale du dispositif
        - [ ] Instructions de conception (prescription écrite originale)
        - [ ] Description des méthodes de fabrication et contrôle
        - [ ] Évaluation clinique (revue de littérature, données cliniques)
        - [ ] Analyse des risques

        **Étiquetage :**
        - [ ] Identification nominative du patient
        - [ ] Mention « Dispositif sur mesure »
        - [ ] Nom et adresse du fabricant
        - [ ] Date de fabrication
        - [ ] Classe du dispositif

        **Obligations supplémentaires (classes IIb/III) :**
        - [ ] Notification à l'Organisme Notifié (ON)
        - [ ] Rapport annuel récapitulatif disponible sur demande

        **⚠️ Rappel :**
        Le marquage CE n'est **pas requis** pour les dispositifs sur mesure.
        """)

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
