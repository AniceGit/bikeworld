import streamlit as st
import sqlite3
from models.produit import Produit
def afficher_produits():
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
            
            lignes = [Produit(id, desc, spec_tech, couleur, image, prix, stock) 
                      for id, desc, spec_tech, couleur, image, prix, stock in result]
            return lignes
    
# def afficher_image_produit(id_produit):
#       with sqlite3.connect("bikeworld.db") as conn:
#             cur = conn.cursor()

#             cur.execute(""" \
#                     SELECT id,
#                         nom, 
#                         image, 
                        
#                     FROM produit WHERE id = :id_produit
#                 """, { "id_produit": id_produit }
#             )

#             result = cur.fetchone()

#             if result is None:
#                 raise Exception(f"Article {id_produit} introuvable.")
            
#             image = afficher_image_produit(result[5])

