"""
Gestion de la base de données JSON pour l'outil RDM 745.
Sauvegarde et chargement des dispositifs, déclarations et tracabilité.
"""

import streamlit as st
import json
import csv
import io
from datetime import datetime


class Database:
    """Gestionnaire de base de données JSON pour RDM 745."""
    
    def __init__(self):
        """Initialise une base vide."""
        self.db = {
            "version": "1.0",
            "etablissement": "",
            "dispositifs": [],
            "declarations": [],
            "tracabilite": []
        }
    
    def to_json(self):
        """Convertit la base en JSON téléchargeable."""
        return json.dumps(self.db, ensure_ascii=False, indent=2)
    
    def from_json(self, json_str):
        """Charge un JSON dans la base."""
        try:
            self.db = json.loads(json_str)
            return True
        except Exception as e:
            raise ValueError(f"Erreur de chargement JSON : {e}")
    
    def add_dispositif(self, nom, reference, classe, categorie, materiau, description):
        """Ajoute un dispositif dans la base."""
        new_id = f"DM-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.db["dispositifs"].append({
            "id": new_id,
            "date_creation": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "nom": nom,
            "reference": reference,
            "classe": classe,
            "categorie": categorie,
            "materiau": materiau,
            "description": description
        })
        return new_id
    
    def add_declaration(self, dispositif_id, type_declaration, praticien, responsable, observations):
        """Ajoute une déclaration."""
        new_id = f"DECL-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.db["declarations"].append({
            "id": new_id,
            "dispositif_id": dispositif_id,
            "date_declaration": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "type_declaration": type_declaration,  # Art.5§5, Art.2§3, AnnexeXIII
            "praticien": praticien,
            "responsable": responsable,
            "observations": observations
        })
        return new_id
    
    def add_tracabilite(self, dispositif_id, patient_id, numero_lot, date_fabrication, operateur, controle_qualite):
        """Ajoute une entrée de traçabilité."""
        new_id = f"TRAQ-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.db["tracabilite"].append({
            "id": new_id,
            "dispositif_id": dispositif_id,
            "patient_id": patient_id,  # Anonymisé
            "numero_lot": numero_lot,
            "date_fabrication": date_fabrication,
            "operateur": operateur,
            "controle_qualite": controle_qualite  # OK/NOK
        })
        return new_id
    
    def get_dispositif_by_id(self, device_id):
        """Récupère un dispositif par son ID."""
        for d in self.db["dispositifs"]:
            if d["id"] == device_id:
                return d
        return None
    
    def dispositifs_to_csv(self):
        """Exporte les dispositifs en CSV."""
        output = io.StringIO()
        if not self.db["dispositifs"]:
            return ""
        writer = csv.DictWriter(output, fieldnames=[
            "id", "date_creation", "nom", "reference",
            "classe", "categorie", "materiau", "description"
        ])
        writer.writeheader()
        writer.writerows(self.db["dispositifs"])
        return output.getvalue()
    
    def declarations_to_csv(self):
        """Exporte les déclarations en CSV."""
        output = io.StringIO()
        if not self.db["declarations"]:
            return ""
        writer = csv.DictWriter(output, fieldnames=[
            "id", "dispositif_id", "date_declaration", "type_declaration",
            "praticien", "responsable", "observations"
        ])
        writer.writeheader()
        writer.writerows(self.db["declarations"])
        return output.getvalue()
    
    def tracabilite_to_csv(self):
        """Exporte la traçabilité en CSV."""
        output = io.StringIO()
        if not self.db["tracabilite"]:
            return ""
        writer = csv.DictWriter(output, fieldnames=[
            "id", "dispositif_id", "patient_id", "numero_lot",
            "date_fabrication", "operateur", "controle_qualite"
        ])
        writer.writeheader()
        writer.writerows(self.db["tracabilite"])
        return output.getvalue()
    
    def get_stats(self):
        """Récupère des statistiques sur la base."""
        return {
            "total_dispositifs": len(self.db["dispositifs"]),
            "total_declarations": len(self.db["declarations"]),
            "total_tracabilite": len(self.db["tracabilite"]),
            "etablissement": self.db["etablissement"]
        }


# ─────────────────────────────────────────────
# UTILITAIRES POUR STREAMLIT
# ─────────────────────────────────────────────
def init_db():
    """Initialise une base vide si elle n'existe pas dans la session."""
    if "db" not in st.session_state:
        st.session_state.db = Database()
    return st.session_state.db


def save_db_to_json(db):
    """Sauvegarde la base en JSON."""
    return db.to_json()


def load_db_from_json(db, json_str):
    """Charge la base depuis un JSON."""
    return db.from_json(json_str)


def export_csv(db, data_type):
    """Exporte une partie de la base en CSV."""
    if data_type == "dispositifs":
        return db.dispositifs_to_csv()
    elif data_type == "declarations":
        return db.declarations_to_csv()
    elif data_type == "tracabilite":
        return db.tracabilite_to_csv()
    else:
        return ""
