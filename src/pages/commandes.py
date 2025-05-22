import streamlit as st
import pandas as pd
from pages.sidebar import afficher_sidebar
from controllers.commande_controller import supprimer_commande, get_commandes, get_adresse_commande


afficher_sidebar()
st.title("Commandes")
st.write("Bienvenue sur la page de commandes de BIKEWORLD!")

#TODO récupérer l'id de l'utilisateur connecté
commandes = get_commandes(1)

data = []

for cmd in commandes:

    data.append({
        "ID": cmd.id,
        "Client": cmd.id_utilisateur,
        "Date": cmd.date_commande,
        "Frais de livraison (€)": f"{cmd.frais_livraison:.2f}",
        "Total (€)": f"{cmd.prix_total:.2f}",
        "Etat": cmd.etat
    })

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

commande_ids = [cmd.id for cmd in commandes]
selected_id = st.selectbox("Sélectionner une commande :", commande_ids)

if selected_id:
    cmd = next((c for c in commandes if c.id == selected_id), None)
    if cmd:
        st.subheader(f"🧾 Détails de la commande {cmd.id}")
        st.write(f"Date : {cmd.date_commande}")
        adresse = get_adresse_commande(cmd.id)
        st.write(f"Adresse : {adresse.numero} {adresse.type_voie} {adresse.nom_voie}, {adresse.code_postal} {adresse.ville}")
      
        ligne_df = pd.DataFrame([{
            "Produit": l.id_produit,
            "Quantité": l.quantite,
            "Prix unitaire (€)": f"{l.prix:.2f}",
            "Total (€)": f"{l.quantite * l.prix :.2f}"
        } for l in cmd.liste_produit_commande])
        st.table(ligne_df)

        if cmd.etat == "Validee":
            if st.button(f"🗑️ Supprimer la commande {cmd.id}", key=f"delete_{cmd.id}"):
                supprimer_commande(cmd.id)
                st.success(f"Commande {cmd.id} supprimée.")
                st.experimental_rerun()
