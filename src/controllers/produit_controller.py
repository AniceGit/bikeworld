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
                        stock
                    
                    FROM produit 
                """
            )
            result = cur.fetchall()
            if result is None:
                raise Exception(f"Aucun articles")
            
            lignes = []
            for id, nom, desc, spec_tech, couleur, image, prix, stock in result:
                lignes.append(Produit(id, nom, desc, spec_tech, couleur, image, prix, stock)) 
            return lignes
    
#st.title("Liste des Produits")

def get_details_produit(id_produit):
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nom, desc, spec_tech, couleur, image, prix, stock
            FROM produit WHERE id = ?
        """, (id_produit,))
        result = cur.fetchone()

        if not result:
            raise Exception("Produit non trouvé")

        id, nom, desc, spec_tech, couleur, image, prix, stock = result
        produit = Produit(id, nom, desc, spec_tech, couleur, image, prix, stock)
        return produit
       
