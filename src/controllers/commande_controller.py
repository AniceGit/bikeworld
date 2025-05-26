import sqlite3
import streamlit as st
from src.models.commande import Commande
from src.models.adresse import Adresse
from src.models.produit_commande import ProduitCommande


def supprimer_commande(id_commande: int) -> int | None:

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        cur.execute(
            """ \
                SELECT id,
                    date_commande,
                    etat,
                    prix_total,
                    frais_livraison,
                    id_utilisateur,
                    id_adresse
                FROM commande WHERE id = :id_commande
            """,
            {"id_commande": id_commande},
        )

        result = cur.fetchone()

        if result is None:
            raise Exception(f"Commande {id_commande} introuvable.")

        (
            id,
            date_commande,
            etat,
            prix_total,
            frais_livraison,
            id_utilisateur,
            id_adresse,
        ) = result
        commande = Commande(
            id,
            date_commande,
            etat,
            prix_total,
            frais_livraison,
            id_utilisateur,
            id_adresse,
        )

        if commande.etat == "Validee":
            # Récupération des produits / quantités / des produits de la commande pour remettre à jour les stocks/ventes sur le produit
            cur.execute(
                """
                SELECT id_produit, quantite
                FROM produit_commande 
                WHERE id_commande = :id_commande
            """,
                {"id_commande": id_commande},
            )
            result = cur.fetchall()

            if result is None:
                raise Exception(f"Commande {id_commande} introuvable.")

            for id_produit, quantite in result:
                cur.execute(
                    """
                    UPDATE produit
                    SET stock = stock + :quantite, ventes = ventes - :quantite
                    WHERE id = :id
                """,
                    {"quantite": quantite, "id": id_produit},
                )

            # Suppression des lignes (produit_commande) de la commande
            cur.execute(
                """
                DELETE FROM produit_commande WHERE id_commande = :id_commande
            """,
                {"id_commande": id_commande},
            )
            result = cur.fetchall()

            cur.execute(
                """
                DELETE FROM commande WHERE id = :id
            """,
                {"id": id_commande},
            )
        else:
            print("etat ne permet pas la suppression")


def calculer_total_commande(id_commande: int) -> float:

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        # Récupération des lignes de produits pour la commande
        cur.execute(
            """
            SELECT quantite, prix FROM commande_produit
            WHERE id_commande = ?
        """,
            (id_commande,),
        )
        lignes = cur.fetchall()

        total_produits = sum(quantite * prix for quantite, prix in lignes)

        # Récupération des frais de livraison
        cur.execute(
            """
            SELECT frais_livraison FROM commande
            WHERE id = ?
        """,
            (id_commande,),
        )
        result = cur.fetchone()
        if result is None:
            raise Exception(f"Commande {id_commande} introuvable.")

        # 0 pour éviter le None
        frais_livraison = float(result[0]) or 0.00

        total_commande = total_produits + frais_livraison

        return total_commande


def get_commandes_by_utilisateur(id_utilisateur: int) -> list[Commande]:

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        # Récupération des commandes du client
        cur.execute(
            """
            SELECT id, date_commande, etat, prix_total, frais_livraison, id_utilisateur, id_adresse
            FROM commande
            WHERE id_utilisateur = :id_utilisateur
        """,
            {"id_utilisateur": id_utilisateur},
        )
        entetes = cur.fetchall()

        commandes = []

        for (
            id_commande,
            date_commande,
            etat,
            prix_total,
            frais_livrason,
            id_utilisateur,
            id_adresse,
        ) in entetes:

            # Récupération des lignes de commande de chaque commande
            cur.execute(
                """
                SELECT id, quantite, prix, id_produit, id_commande
                FROM produit_commande
                WHERE id_commande = :id_commande
            """,
                {"id_commande": id_commande},
            )
            result_lignes = cur.fetchall()

            lignes = []

            for (
                id_produit_commande,
                quantite,
                prix,
                id_produit,
                id_commande,
            ) in result_lignes:
                lignes.append(
                    ProduitCommande(
                        id=id_produit_commande,
                        quantite=quantite,
                        prix=prix,
                        id_produit=id_produit,
                        id_commande=id_commande,
                    )
                )

            ma_commande = Commande(
                id=id_commande,
                date_commande=date_commande,
                etat=etat,
                prix_total=prix_total,
                frais_livraison=frais_livrason,
                id_utilisateur=id_utilisateur,
                id_adresse=id_adresse,
            )
            ma_commande.liste_produit_commande = lignes
            commandes.append(ma_commande)

    return commandes


def get_adresse_commande(id_adresse: int) -> Adresse | None:

    adresse_commande = None
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        cur.execute(
            """
                SELECT id,
                    numero,
                    type_voie,
                    nom_voie,
                    code_postal,
                    ville,
                    pays,
                    defaut,
                    id_utilisateur
                FROM adresse WHERE id = :id_adresse
            """,
            {"id_adresse": id_adresse},
        )

        result = cur.fetchone()

        if result is None:
            raise Exception(f"Adresse de la commande {id_adresse} introuvable.")

        (
            id,
            numero,
            type_voie,
            nom_voie,
            code_postal,
            ville,
            pays,
            defaut,
            id_utilisateur,
        ) = result
        adresse_commande = Adresse(
            id,
            numero,
            type_voie,
            nom_voie,
            code_postal,
            ville,
            pays,
            defaut,
            id_utilisateur,
        )

    return adresse_commande


def transformer_panier() -> None:
    panier = st.session_state.panier

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        user = st.session_state["utilisateur"]

        # Insertion de la commande
        cur.execute(
            """
            INSERT INTO commande (date_commande, etat, prix_total, frais_livraison, id_utilisateur, id_adresse)
            VALUES (:date_commande,
                    :etat,
                    :prix_total,
                    :frais_livraison,
                    :id_utilisateur,
                    :id_adresse)
        """,
            {
                "date_commande": panier["date_panier"],
                "etat": "Validee",
                "prix_total": panier["total_panier"],
                "frais_livraison": (
                    panier["frais_livraison"] if panier["total_panier"] < 1500 else 0.00
                ),
                "id_utilisateur": user.id,
                "id_adresse": user.adresse.id
            },
        )

        # retour de l'id créé
        cmd_id = cur.lastrowid

        # Insertion des lignes de commande
        for ligne in panier["liste_produits_quantite"]:

            cur.execute(
                """
                INSERT INTO produit_commande (id_commande, id_produit, quantite, prix)
                VALUES (:id_commande,
                        :id_produit,
                        :quantite,
                        :prix)
            """,
                {
                    "id_commande": cmd_id,
                    "id_produit": ligne["produit_id"],
                    "quantite": ligne["quantite"],
                    "prix": ligne["prix"],
                },
            )

            cur.execute(
                """
                UPDATE produit
                SET stock = stock - :quantite, ventes = ventes + :quantite
                WHERE id = :id
            """,
                {"quantite": ligne["quantite"], "id": ligne["produit_id"]},
            )


def get_commandes() -> list[Commande]:

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        # Récupération des commandes du client
        cur.execute(
            """
            SELECT id, date_commande, etat, prix_total, frais_livraison, id_utilisateur, id_adresse
            FROM commande
        """)
        entetes = cur.fetchall()

        commandes = []

        for (
            id_commande,
            date_commande,
            etat,
            prix_total,
            frais_livrason,
            id_utilisateur,
            id_adresse,
        ) in entetes:

            # Récupération des lignes de commande de chaque commande
            cur.execute(
                """
                SELECT id, quantite, prix, id_produit, id_commande
                FROM produit_commande
                WHERE id_commande = :id_commande
            """,
                {"id_commande": id_commande},
            )
            result_lignes = cur.fetchall()

            lignes = []

            for (
                id_produit_commande,
                quantite,
                prix,
                id_produit,
                id_commande,
            ) in result_lignes:
                lignes.append(
                    ProduitCommande(
                        id=id_produit_commande,
                        quantite=quantite,
                        prix=prix,
                        id_produit=id_produit,
                        id_commande=id_commande,
                    )
                )

            ma_commande = Commande(
                id=id_commande,
                date_commande=date_commande,
                etat=etat,
                prix_total=prix_total,
                frais_livraison=frais_livrason,
                id_utilisateur=id_utilisateur,
                id_adresse=id_adresse,
            )
            ma_commande.liste_produit_commande = lignes
            commandes.append(ma_commande)

    return commandes


def modifier_etat_commande(id_commande: int, etat: str) -> int | None:

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        cur.execute(
            """
            UPDATE commande
            SET etat = :etat
            WHERE id = :id
        """,
            {"id": id_commande, "etat": etat},
        )

