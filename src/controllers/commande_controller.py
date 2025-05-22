import sqlite3
from models.commande import Commande
from models.produit_commande import ProduitCommande


# def creer_commande(commande: Commande, lignes: list[ProduitCommande]) -> int | None:

#     with sqlite3.connect("bikeworld.db") as conn:
#         cur = conn.cursor()

#         # Insertion de la commande
#         cur.execute("""
#             INSERT INTO commandes (date_commande, etat, prix_total, frais_livraison, id_utilisateur, id_adresse)
#             VALUES (:date_commande,
#                     :etat,
#                     :prix_total,
#                     :frais_livraison,
#                     :id_utilisateur,
#                     :id_adresse)
#         """, {"date_commande": commande.date_commande,
#               "etat": commande.etat,
#               "prix_total": commande.prix_total,
#               "frais_livraison": commande.frais_livraison,
#               "id_utilisateur": commande.id_utilisateur,
#               "id_adresse": commande.id_adresse
#             }
#         )

#         # retour de l'id créé
#         cmd_id = cur.lastrowid
#         if cmd_id:
#             commande.id = cmd_id

#         # Insertion des lignes de commande
#         for ligne in lignes:
#             ligne.id_commande = commande.id
#             cur.execute("""
#                 INSERT INTO produit_commande (id_commande, id_produit, quantite, prix)
#                 VALUES (?, ?, ?, ?)
#             """, (ligne.id_commande, ligne.id_produit, ligne.quantite, ligne.prix))

#     return commande.id if commande.id else None


def supprimer_commande(id_commande: int) -> int | None:

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        cur.execute(""" \
                SELECT id,
                    date_commande,
                    etat,
                    prix_total,
                    frais_livraison,
                    id_utilisateur,
                    id_adresse
                FROM commande WHERE id = :id_commande
            """, { "id_commande": id_commande }
        )

        result = cur.fetchone()

        if result is None:
            raise Exception(f"Commande {id_commande} introuvable.")
        
        commande = Commande(result[0], result[1], result[2], result[3], result[4], result[5], result[6])

        if commande.etat == "Validee":
            # Suppression des lignes (produit_commande) de la commande
            cur.execute("""
                DELETE FROM produit_commande WHERE id_commande = :id_commande
            """, { "id_commande": id_commande }
            )

            cur.execute("""
                DELETE FROM commande WHERE id = :id
            """, { "id": id_commande }
            )
        else:
            print("etat ne permet pas la suppression")


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


def get_commandes(id_utilisateur: int) -> list[Commande]:

    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        # Récupération des commandes du client
        cur.execute("""
            SELECT id, date_commande, etat, prix_total, frais_livraison, id_utilisateur, id_adresse
            FROM commande
            WHERE id_utilisateur = :id_utilisateur
        """, { "id_utilisateur": id_utilisateur }
        )
        entetes = cur.fetchall()

        commandes = []

        for id_commande, date_commande, etat, prix_total, frais_livrason, id_utilisateur, id_adresse in entetes:

            # Récupération des lignes de commande de chaque commande
            cur.execute("""
                SELECT id, quantite, prix, id_produit, id_commande
                FROM produit_commande
                WHERE id_commande = :id_commande
            """, { "id_commande": id_commande }
            )
            result_lignes = cur.fetchall()

            lignes = [ProduitCommande(id_produit_commande, quantite, prix, id_produit, id_commande) for id_produit_commande, quantite, prix, id_produit, id_commande in result_lignes]

            commandes.append(Commande(id=id_commande, 
                                      date_commande=date_commande,
                                      etat=etat,
                                      prix_total=prix_total,
                                      frais_livraison=frais_livrason,
                                      id_utilisateur=id_utilisateur,
                                      id_adresse=id_adresse,
                                      liste_produit_commande=lignes
                                      )
            )

    return commandes