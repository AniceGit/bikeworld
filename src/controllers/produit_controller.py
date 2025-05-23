import streamlit as st
import sqlite3
from models.produit import Produit


def get_produits():
    #affiche tous les articles

    with sqlite3.connect("bikeworld.db") as conn:
            cur = conn.cursor()
            cur.execute(""" \
                    SELECT id,
                        nom,
                        desc,
                        spec_tech, 
                        couleur, 
                        image, 
                        prix, 
                        stock,
                        ventes
                    FROM produit 
                """
            )
            result = cur.fetchall()
            if result is None:
                raise Exception(f"Aucun articles")
            
            lignes = []
            for id, nom, desc, spec_tech, couleur, image, prix, stock, ventes in result:
                lignes.append(Produit(id, nom, desc, spec_tech, couleur, image, prix, stock, ventes)) 
            return lignes
    
#st.title("Liste des Produits")

def get_details_produit(id_produit):
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nom, desc, spec_tech, couleur, image, prix, stock, ventes
            FROM produit WHERE id = ?
        """, (id_produit,))
        result = cur.fetchone()

        if not result:
            raise Exception("Produit non trouvé")

        id, nom, desc, spec_tech, couleur, image, prix, stock, ventes = result
        produit = Produit(id, nom, desc, spec_tech, couleur, image, prix, stock, ventes)
        return produit
       

def get_top_3_ventes() -> list[Produit]:
     
     with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nom, desc, spec_tech, couleur, image, prix, stock, ventes
            FROM produit
            ORDER BY ventes DESC
            LIMIT 3
        """)
        result = cur.fetchall()

        if not result:
            raise Exception("Produit non trouvé")

        produits = []
        for id, nom, desc, spec_tech, couleur, image, prix, stock, ventes in result:
            produits.append(Produit(id, nom, desc, spec_tech, couleur, image, prix, stock, ventes)) 

        return produits
