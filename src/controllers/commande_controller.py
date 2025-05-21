import sqlite3
from models.commande import Commande
from models.produit_commande import ProduitCommande


def creer_commande(commande: Commande, lignes: list[ProduitCommande]) -> int | None:

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        # Insertion de la commande
        cur.execute("""
            INSERT INTO commandes (date_commande, etat, prix_total, frais_livraison, id_utilisateur, id_adresse)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (commande.date_commande, commande.etat, commande.prix_total, commande.frais_livraison,
              commande.id_utilisateur, commande.id_adresse))

        # retour de l'id créé
        cmd_id = cur.lastrowid
        if cmd_id:
            commande.id = cmd_id

        # Insertion des lignes de commande
        for ligne in lignes:
            ligne.id_commande = commande.id
            cur.execute("""
                INSERT INTO commande_produit (id_commande, id_produit, quantite, prix)
                VALUES (?, ?, ?, ?)
            """, (ligne.id_commande, ligne.id_produit, ligne.quantite, ligne.prix))

    return commande.id if commande.id else None


def calculer_total_commande(id_commande: int) -> float:
    
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        # Récupération des lignes de produits pour la commande
        cur.execute("""
            SELECT quantite, prix FROM commande_produit
            WHERE id_commande = ?
        """, (id_commande,))
        lignes = cur.fetchall()

        total_produits = sum(quantite * prix for quantite, prix in lignes)

        # Récupération des frais de livraison
        cur.execute("""
            SELECT frais_livraison FROM commande
            WHERE id = ?
        """, (id_commande,))
        result = cur.fetchone()
        if result is None:
            raise Exception(f"Commande {id_commande} introuvable.")

        # 0 pour éviter le None
        frais_livraison = float(result[0]) or 0.00

        total_commande = total_produits + frais_livraison

        return total_commande
