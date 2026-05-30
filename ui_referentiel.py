"""
Onglet du référentiel réglementaire (articles, annexes, guidance).
"""

import streamlit as st


def show_tab_referentiel():
    """Affiche l'onglet du référentiel réglementaire."""
    st.title("📖 Référentiel réglementaire — RDM 745")
    st.caption("Cliquez sur chaque article pour afficher les détails")
    st.divider()

    # ─────────────────────────────────────────────
    # Article 2§3 — Sur mesure
    # ─────────────────────────────────────────────
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

    # ─────────────────────────────────────────────
    # Article 5§5 — In-house
    # ─────────────────────────────────────────────
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

    # ─────────────────────────────────────────────
    # Annexe XIII — Sur mesure
    # ─────────────────────────────────────────────
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

    # ─────────────────────────────────────────────
    # Annexe I — EGSEP
    # ─────────────────────────────────────────────
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

    # ─────────────────────────────────────────────
    # MDCG 2021-23
    # ─────────────────────────────────────────────
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

    # ─────────────────────────────────────────────
    # Hors cadre
    # ─────────────────────────────────────────────
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
