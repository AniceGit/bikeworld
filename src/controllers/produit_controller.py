import sqlite3
from models.produit import Produit


def get_produits() -> list[Produit]:
    # affiche tous les articles

    lignes = []
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute(
            """ \
                    SELECT id,
                        nom,
                        desc,
                        spec_tech, 
                        couleur, 
                        image, 
                        prix, 
                        stock,
                        ventes,
                        actif
                    FROM produit 
                """
        )
        result = cur.fetchall()
        if result is None:
            raise Exception(f"Aucun articles")

        for id, nom, desc, spec_tech, couleur, image, prix, stock, ventes, actif in result:
            lignes.append(
                Produit(id, nom, desc, spec_tech, couleur, image, prix, stock, ventes, actif)
            )
    return lignes


# st.title("Liste des Produits")


def get_details_produit(id_produit: int) -> Produit:
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT id, nom, desc, spec_tech, couleur, image, prix, stock, ventes, actif
            FROM produit
            WHERE id = ?
        """,
            (id_produit,),
        )
        result = cur.fetchone()

        if not result:
            raise Exception("Produit non trouvé")

        id, nom, desc, spec_tech, couleur, image, prix, stock, ventes, actif = result
        produit = Produit(id, nom, desc, spec_tech, couleur, image, prix, stock, ventes, actif)
        return produit


def get_top_3_ventes() -> list[Produit]:

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT id, nom, desc, spec_tech, couleur, image, prix, stock, ventes, actif
            FROM produit
            WHERE actif = 1
            ORDER BY ventes DESC
            LIMIT 3
        """
        )
        result = cur.fetchall()

        if not result:
            raise Exception("Produit non trouvé")

        produits = []
        for id, nom, desc, spec_tech, couleur, image, prix, stock, ventes, actif in result:
            produits.append(
                Produit(id, nom, desc, spec_tech, couleur, image, prix, stock, ventes, actif)
            )

        return produits


def get_produit_nom_by_id(id_produit: int) -> str:
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT nom
            FROM produit
            WHERE id = :id_produit
        """,
            {"id_produit": id_produit},
        )
        result = cur.fetchone()

        if not result:
            raise Exception("Produit non trouvé")

        nom_produit = result
        return nom_produit


def modifier_produit(id, nom, description, spec_tech, couleur, image, prix, stock, actif):

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE produit
            SET nom = :nom,
                desc = :desc,
                spec_tech = :spec_tech,
                couleur = :couleur,
                image = :image,
                prix = :prix,
                stock = :stock,
                actif = :actif
            WHERE id = :id
        """,
            {"id": id, "nom": nom, "desc": description, "spec_tech": spec_tech, "couleur": couleur, "image": image, "prix": prix, "stock": stock, "actif" :actif},
        )
