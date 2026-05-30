"""
Onglet de gestion de la base de données (import/export JSON, CSV).
"""

import streamlit as st
import json
from datetime import datetime
from database import Database

def show_tab_database():
    """Affiche l'onglet de gestion de la base de données."""
    st.title("💾 Ma base de données")
    st.caption("Gérez vos dispositifs, déclarations et tracabilité")
    st.divider()
    
    # Initialisation de la base
    if "db" not in st.session_state:
        st.session_state.db = Database()
    
    db = st.session_state.db
    stats = db.get_stats()
    
    # ─────────────────────────────────────────────
    # INFO BAR — ÉTABLISSEMENT
    # ─────────────────────────────────────────────
    st.subheader("🏥 Établissement")
    etablissement = st.text_input(
        "Nom de l'établissement",
        value=db.db["etablissement"],
        placeholder="Centre François Baclesse",
        key="etablissement_input"
    )
    if etablissement != db.db["etablissement"]:
        db.db["etablissement"] = etablissement
        st.success("✅ Établissement mis à jour !")
    
    # ─────────────────────────────────────────────
    # STATS
    # ─────────────────────────────────────────────
    st.divider()
    st.subheader("📊 Statistiques")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Dispositifs", stats["total_dispositifs"])
    with col2:
        st.metric("Déclarations", stats["total_declarations"])
    with col3:
        st.metric("Traçabilité", stats["total_tracabilite"])
    
    # ─────────────────────────────────────────────
    # IMPORT / EXPORT
    # ─────────────────────────────────────────────
    st.divider()
    st.subheader("📂 Import / Export")
    
    tab_imp_exp1, tab_imp_exp2 = st.tabs(["📥 Importer", "📤 Exporter"])
    
    with tab_imp_exp1:
        st.markdown("""
        **Importer une base existante**
        
        Téléversez votre fichier `.json` pour charger vos données.
        """)
        uploaded_file = st.file_uploader(
            "Choisir un fichier JSON",
            type=["json"],
            help="Fichier exporté précédemment depuis cet outil"
        )
        
        if uploaded_file is not None:
            try:
                content = uploaded_file.read().decode("utf-8")
                data = json.loads(content)
                if "version" not in data or "dispositifs" not in 
                    st.error("❌ Format JSON invalide")
                else:
                    db.from_json(content)
                    # ← PAS de st.rerun() ici !
                    st.success(f"✅ Base chargée avec succès !")
                    st.info(f"""
                    📊 **Contenu importé :**
                    - {len(data['dispositifs'])} dispositif(s)
                    - {len(data['declarations'])} déclaration(s)
                    - {len(data['tracabilite'])} entrée(s) de traçabilité
                    - Établissement : {data.get('etablissement', 'Non renseigné')}
                    """)
                    st.balloons()  # 🎈 petit effet visuel !
            except json.JSONDecodeError:
                st.error("❌ Fichier JSON invalide — vérifiez le contenu")
            except Exception as e:
                st.error(f"❌ Erreur inattendue : {e}")
            
    
    with tab_imp_exp2:
        st.markdown("""
        **Exporter vos données**
        
        Sauvegardez vos données pour les retrouver plus tard ou les partager.
        """)
        
        # Export JSON
        col_json1, col_json2 = st.columns([3, 1])
        with col_json1:
            st.markdown("**Sauvegarder en JSON** (fichier complet)")
        with col_json2:
            json_data = db.to_json()
            st.download_button(
                label="💾 Télécharger JSON",
                data=json_data,
                file_name=f"rdm745_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        st.divider()
        
        # Export CSV
        st.markdown("**Exporter en CSV** (tableaux individuels)")
        
        col_csv1, col_csv2, col_csv3 = st.columns(3)
        
        with col_csv1:
            csv_dispositifs = db.dispositifs_to_csv()
            if csv_dispositifs:
                st.download_button(
                    label="📥 Télécharger dispositifs.csv",
                    data=csv_dispositifs,
                    file_name="dispositifs.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            else:
                st.info("Aucun dispositif")
        
        with col_csv2:
            csv_declarations = db.declarations_to_csv()
            if csv_declarations:
                st.download_button(
                    label="📥 Télécharger declarations.csv",
                    data=csv_declarations,
                    file_name="declarations.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            else:
                st.info("Aucune déclaration")
        
        with col_csv3:
            csv_tracabilite = db.tracabilite_to_csv()
            if csv_tracabilite:
                st.download_button(
                    label="📥 Télécharger tracabilite.csv",
                    data=csv_tracabilite,
                    file_name="tracabilite.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            else:
                st.info("Aucune traçabilité")
    
    # ─────────────────────────────────────────────
    # LISTE DES DISPOSITIFS
    # ─────────────────────────────────────────────
    st.divider()
    st.subheader("📋 Mes dispositifs")
    
    if db.db["dispositifs"]:
        for dispo in db.db["dispositifs"]:
            with st.expander(f"🔹 {dispo['nom']} ({dispo['id']})"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Référence :** {dispo.get('reference', '-')}")
                    st.write(f"**Classe :** {dispo.get('classe', '-')}")
                    st.write(f"**Catégorie :** {dispo.get('categorie', '-')}")
                with col2:
                    st.write(f"**Matériau :** {dispo.get('materiau', '-')}")
                    st.write(f"**Créé le :** {dispo.get('date_creation', '-')}")
                st.write(f"**Description :** {dispo.get('description', '-')}")
    else:
        st.info("Aucun dispositif enregistré. Utilisez l'arbre de décision pour en ajouter.")
    
    # ─────────────────────────────────────────────
    # LISTE DES DÉCLARATIONS
    # ─────────────────────────────────────────────
    st.divider()
    st.subheader("📄 Mes déclarations")
    
    if db.db["declarations"]:
        for decl in db.db["declarations"]:
            with st.expander(f"📄 {decl['type_declaration']} - {decl['id']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Dispositif :** {decl.get('dispositif_id', '-')}")
                    st.write(f"**Praticien :** {decl.get('praticien', '-')}")
                with col2:
                    st.write(f"**Date :** {decl.get('date_declaration', '-')}")
                    st.write(f"**Responsable :** {decl.get('responsable', '-')}")
                st.write(f"**Observations :** {decl.get('observations', '-')}")
    else:
        st.info("Aucune déclaration enregistrée.")
    
    # ─────────────────────────────────────────────
    # LISTE DE LA TRAÇABILITÉ
    # ─────────────────────────────────────────────
    st.divider()
    st.subheader("🔍 Traçabilité")
    
    if db.db["tracabilite"]:
        for traq in db.db["tracabilite"]:
            with st.expander(f"🔍 {traq['numero_lot']} - {traq['id']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Dispositif :** {traq.get('dispositif_id', '-')}")
                    st.write(f"**Patient :** {traq.get('patient_id', '-')}")
                    st.write(f"**Fabrication :** {traq.get('date_fabrication', '-')}")
                with col2:
                    st.write(f"**Lot :** {traq.get('numero_lot', '-')}")
                    st.write(f"**Opérateur :** {traq.get('operateur', '-')}")
                    st.write(f"**Contrôle :** {traq.get('controle_qualite', '-')}")
    else:
        st.info("Aucune entrée de traçabilité enregistrée.")
